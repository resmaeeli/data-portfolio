"""
Load query by name from sql query repo.
"""

# importing libs
# import os
from pathlib import Path


# get base folder of sql queries
def _get_sql_folder():
    # print(Path(__file__))
    # print(Path(__file__).parent)
    return Path(__file__).parent.parent / "sql"


# loading sql queries dynamically
def load_query(query_name):
    query_path = _get_sql_folder() / f"{query_name}"  # .sql"
    with open(query_path, encoding="utf-8") as query:
        return query.read()


def list_queries():
    query_names = []
    for sqlfile in _get_sql_folder().glob("*.sql"):
        query_names.append(sqlfile.stem)
    return query_names
