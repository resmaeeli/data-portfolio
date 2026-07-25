
#from .db_config import DB_SERVER, DB_NAME, DB_USER, DB_PASSWORD
import pyodbc


# finding appropriate odbc driver
def _get_odbc_driver():
    drivers = pyodbc.drivers()

    odbc_drivers = [
        driver for driver in drivers
        if driver.startswith("ODBC Driver") and "SQL Server" in driver
    ]

    if not odbc_drivers:
        raise Exception("No supported SQL Server ODBC driver found.")

    odbc_drivers.sort(
        key=lambda x: int(x.split()[2]), ## sort by int value
        reverse=True
    )
    return odbc_drivers[0]


# get connection string
def get_connection_string(db_config):
    
    #creating connection_string
    _connection_string = f"""
        DRIVER={{{_get_odbc_driver()}}};
        SERVER={db_config["server"]};
        DATABASE={db_config["database"]};
        UID={db_config["username"]};
        PWD={db_config["password"]};
        TrustServerCertificate={db_config["trust_server_certificate"]};
        """
    return _connection_string


def get_connection(db_config):
    connection = pyodbc.connect(get_connection_string(db_config))
    return connection