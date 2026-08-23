"""
SqlServer connection provider strategy
"""

import pyodbc


def _get_odbc_driver():
    """finding appropriate odbc driver"""

    drivers = pyodbc.drivers()
    odbc_drivers = [
        driver
        for driver in drivers
        if driver.startswith("ODBC Driver") and "SQL Server" in driver
    ]

    if not odbc_drivers:
        raise Exception("No supported SQL Server ODBC driver found.")

    odbc_drivers.sort(
        key=lambda x: int(x.split()[2]), reverse=True  ## sort by int value
    )
    return odbc_drivers[0]


def _get_dsn(db_config):
    """Create DSN"""
    dsn = f"""
        DRIVER={{{_get_odbc_driver()}}};
        SERVER={db_config["server"]};
        DATABASE={db_config["database"]};
        UID={db_config["username"]};
        PWD={db_config["password"]};
        TrustServerCertificate={db_config["trust_server_certificate"]};        
        Encrypt={db_config.get("Encrypt", "yes")};
        """
    return dsn


def get_connection(db_config):
    """Get SQL Server connection"""
    connection = pyodbc.connect(_get_dsn(db_config))
    return connection
