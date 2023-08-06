import os
import logging
import sqlite3
from PySide6.QtSql import QSql, QSqlDatabase, QSqlQuery
from PySide6.QtWidgets import QApplication, QMessageBox
from PySide6.QtGui import QIcon
from jal.constants import Setup
from jal.db.settings import JalSettings


# No translation of the file because these routines might be used before QApplication initialization
class LedgerInitError:
    DbInitSuccess = 0
    DbInitFailure = 1
    EmptyDbInitialized = 2
    OutdatedDbSchema = 3
    NewerDbSchema = 4
    DbDriverFailure = 5
    NoDeltaFile = 6
    SQLFailure = 7
    _messages = {
        0: "No error",
        1: "Database initialization failure.",
        2: "Database was initialized. You need to start application again.",
        3: "Database schema version is outdated. Please update it or use older application version.",
        4: "Unsupported database schema. Please update the application.",
        5: "Sqlite driver initialization failed.",
        6: "DB delta file not found.",
        7: "SQL command was executed with error."
    }

    def __init__(self, code, details=''):
        self.code = code
        self.message = self._messages[code]
        self.details = details


# -------------------------------------------------------------------------------------------------------------------
# Returns absolute path to a folder from where application was started
def get_app_path() -> str:
    return os.path.dirname(os.path.dirname(os.path.realpath(__file__))) + os.sep


# -------------------------------------------------------------------------------------------------------------------
def get_dbfilename(app_path):
    return app_path + Setup.DB_PATH


# -------------------------------------------------------------------------------------------------------------------
# returns QIcon loaded from the file with icon_name located in folder Setup.ICONS_PATH
def load_icon(icon_name) -> QIcon:
    return QIcon(get_app_path() + Setup.ICONS_PATH + os.sep + icon_name)


# -------------------------------------------------------------------------------------------------------------------
# This function returns SQLite connection used by JAL or fails with RuntimeError exception
def db_connection():
    db = QSqlDatabase.database(Setup.DB_CONNECTION)
    if not db.isValid():
        raise RuntimeError(f"DB connection '{Setup.DB_CONNECTION}' is invalid")
    if not db.isOpen():
        logging.fatal(f"DB connection '{Setup.DB_CONNECTION}' is not open")
    return db


# -------------------------------------------------------------------------------------------------------------------
def db_triggers_disable():
    _ = executeSQL("UPDATE settings SET value=0 WHERE name='TriggersEnabled'", commit=True)

# -------------------------------------------------------------------------------------------------------------------
def db_triggers_enable():
    _ = executeSQL("UPDATE settings SET value=1 WHERE name='TriggersEnabled'", commit=True)

# -------------------------------------------------------------------------------------------------------------------
# prepares SQL query from given sql_text
# params_list is a list of tuples (":param", value) which are used to prepare SQL query
# Current transactin will be commited if 'commit' set to true
# Parameter 'forward_only' may be used for optimization
# return value - QSqlQuery object (to allow iteration through result)
def executeSQL(sql_text, params=[], forward_only=True, commit=False):
    db = db_connection()
    query = QSqlQuery(db)
    query.setForwardOnly(forward_only)
    if not query.prepare(sql_text):
        logging.error(f"SQL prep: '{query.lastError().text()}' for query '{sql_text}' with params '{params}'")
        return None
    for param in params:
        query.bindValue(param[0], param[1])
    if not query.exec():
        logging.error(f"SQL exec: '{query.lastError().text()}' for query '{sql_text}' with params '{params}'")
        return None
    if commit:
        db.commit()
    return query


# -------------------------------------------------------------------------------------------------------------------
# the same as executeSQL() but after query execution it takes first line of query result and:
# - returns None if no records were fetched by query
# - otherwise returns first row of the query result:
# named = False: result is packed into a list of field values
# named = True: result is packet into a dictionary with field names as keys
# - check_unique = True: checks that only 1 record was returned by query, otherwise returns None
def readSQL(sql_text, params=None, named=False, check_unique=False):
    if params is None:
        params = []
    query = QSqlQuery(db_connection())   # TODO reimplement via ExecuteSQL() call in order to get rid of duplicated code
    query.setForwardOnly(True)
    if not query.prepare(sql_text):
        logging.error(f"SQL prep: '{query.lastError().text()}' for query '{sql_text}' | '{params}'")
        return None
    for param in params:
        query.bindValue(param[0], param[1])
    if not query.exec():
        logging.error(f"SQL exec: '{query.lastError().text()}' for query '{sql_text}' | '{params}'")
        return None
    if query.next():
        res = readSQLrecord(query, named=named)
        if check_unique and query.next():
            return None  # More then one record in result when only one expected
        return res
    else:
        return None


def readSQLrecord(query, named=False):
    if named:
        values = {}
    else:
        values = []
    for i in range(query.record().count()):
        if named:
            values[query.record().fieldName(i)] = query.value(i)
        else:
            values.append(query.value(i))
    if values:
        if len(values) == 1:
            return values[0]
        else:
            return values
    else:
        return None

# -------------------------------------------------------------------------------------------------------------------
# This function:
# 1) checks that DB file is present and contains some data
#    if not - it will initialize DB with help of SQL-script
# 2) checks that DB looks like a valid one:
#    if schema version is invalid it will close DB
# Returns: LedgerInitError(code = 0 if db was initialized successfully)
def init_and_check_db(db_path):
    db = QSqlDatabase.addDatabase("QSQLITE", Setup.DB_CONNECTION)
    if not db.isValid():
        return LedgerInitError(LedgerInitError.DbDriverFailure)
    db.setDatabaseName(get_dbfilename(db_path))
    db.setConnectOptions("QSQLITE_ENABLE_REGEXP=1")
    db.open()
    tables = db.tables(QSql.Tables)
    if not tables:
        db.close()
        connection_name = db.connectionName()
        init_db_from_sql(get_dbfilename(db_path), db_path + Setup.INIT_SCRIPT_PATH)
        QSqlDatabase.removeDatabase(connection_name)
        return LedgerInitError(LedgerInitError.EmptyDbInitialized)

    schema_version = JalSettings().getValue('SchemaVersion')
    if schema_version < Setup.TARGET_SCHEMA:
        db.close()
        return LedgerInitError(LedgerInitError.OutdatedDbSchema)
    elif schema_version > Setup.TARGET_SCHEMA:
        db.close()
        return LedgerInitError(LedgerInitError.NewerDbSchema)

    _ = executeSQL("PRAGMA foreign_keys = ON")
    db_triggers_enable()

    return LedgerInitError(LedgerInitError.DbInitSuccess)


# -------------------------------------------------------------------------------------------------------------------
def init_db_from_sql(db_file, sql_file):
    with open(sql_file, 'r', encoding='utf-8') as sql_file:
        sql_text = sql_file.read()
    db = sqlite3.connect(db_file)
    cursor = db.cursor()
    cursor.executescript(sql_text)
    db.commit()
    db.close()


# -------------------------------------------------------------------------------------------------------------------
def update_db_schema(db_path):
    if QMessageBox().warning(None, QApplication.translate('DB', "Database format is outdated"),
                             QApplication.translate('DB', "Do you agree to upgrade your data to newer format?"),
                             QMessageBox.Yes, QMessageBox.No) == QMessageBox.No:
        return LedgerInitError(LedgerInitError.OutdatedDbSchema)

    db = sqlite3.connect(get_dbfilename(db_path))
    cursor = db.cursor()
    try:
        cursor.execute("SELECT value FROM settings WHERE name='SchemaVersion'")
    except:
        return LedgerInitError(LedgerInitError.DbInitFailure)

    schema_version = cursor.fetchone()[0]
    for step in range(schema_version, Setup.TARGET_SCHEMA):
        delta_file = db_path + Setup.UPDATES_PATH + os.sep + Setup.UPDATE_PREFIX + f"{step+1}.sql"
        logging.info(f"Applying delta schema {step}->{step+1} from {delta_file}")
        try:
            with open(delta_file) as delta_sql:
                try:
                    cursor.executescript(delta_sql.read())
                except sqlite3.OperationalError as e:
                    return LedgerInitError(LedgerInitError.SQLFailure, e.args[0])
        except FileNotFoundError:
            return LedgerInitError(LedgerInitError.NoDeltaFile, delta_file)
    db.close()
    return LedgerInitError(LedgerInitError.DbInitSuccess)

# -------------------------------------------------------------------------------------------------------------------
def get_category_name(category_id):
    return readSQL("SELECT c.name FROM categories AS c WHERE c.id=:category_id", [(":category_id", category_id)])

# -------------------------------------------------------------------------------------------------------------------
def get_account_name(account_id):
    return readSQL("SELECT name FROM accounts WHERE id=:account_id", [(":account_id", account_id)])

# -------------------------------------------------------------------------------------------------------------------
def get_country_by_code(country_code):
    if not country_code:
        return 0
    country_id = readSQL("SELECT id FROM countries WHERE code=:code", [(":code", country_code)], check_unique=True)
    if country_id is None:
        country_id = 0
        logging.warning(QApplication.translate('DB', "Unknown country code: ") + f"'{country_code}'")
    return country_id

# -------------------------------------------------------------------------------------------------------------------
def account_last_date(account_id):
    last_timestamp = readSQL("SELECT MAX(o.timestamp) FROM operation_sequence AS o "
                             "LEFT JOIN accounts AS a ON o.account_id=a.id WHERE a.id=:account_id",
                             [(":account_id", account_id)])
    last_timestamp = 0 if last_timestamp == '' else last_timestamp
    return last_timestamp
