"""
Database connection factory.
"""

import importlib
from config.loader import get_database_config


# get sql connection
def get_connection(db_type):

    strategy_name = f"{db_type}_strategy"

    try:
        strategy = importlib.import_module(
            f".strategies.{strategy_name}", package=__package__
        )
    except ModuleNotFoundError:
        raise ModuleNotFoundError(f"Database strategy '{strategy_name}' not found.")

    # get db_config
    db_config = get_database_config(db_type)

    # get connection based on strategy
    connection = strategy.get_connection(db_config)

    return connection
