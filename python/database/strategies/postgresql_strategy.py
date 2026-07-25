"""
PostGreSql connection provider strategy
"""

import psycopg2

def _get_dsn(db_config):
    """ Create DSN """
    dsn = (
        f"host={db_config['server']} "
        f"port={db_config['port']} "
        f"dbname={db_config['database']} "
        f"user={db_config['username']} "
        f"password={db_config['password']}"
    )
    return dsn

def get_connection(db_config):
    """ Get PostgreSQL connection """
    connection = psycopg2.connect(_get_dsn(db_config))
    return connection