"""
Database connection factory.
"""

from db_config import DB_SERVER, DB_NAME, DB_USER, DB_PASSWORD
import pyodbc

# check if server is localhost
_trust_server_cert = "yes" if DB_SERVER == "localhost" else "no"


# finding appropriate odbc driver
def _get_odbc_driver():
    drivers = pyodbc.drivers()
    if "ODBC Driver 18 for SQL Server" in drivers:
        return "ODBC Driver 18 for SQL Server"
    if "ODBC Driver 17 for SQL Server" in drivers:
        return "ODBC Driver 17 for SQL Server"
    raise Exception("No supported SQL Server ODBC driver found.")


# get connection string
def get_connection_string():
    _connection_string = f"""
        DRIVER={{{_get_odbc_driver()}}};
        SERVER={DB_SERVER};
        DATABASE={DB_NAME};
        UID={DB_USER};
        PWD={DB_PASSWORD};
        TrustServerCertificate={_trust_server_cert};
        """
    return _connection_string


# get sql connection
def get_connection():
    connection = pyodbc.connect(get_connection_string())
    return connection
