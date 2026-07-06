"""
Load SQL queries from the repository.
"""

from pathlib import Path


# get base folder of sql queries
def _get_sql_folder():
    return Path(__file__).parent.parent.parent / "sql"


# loading sql queries dynamically
def load_query(query_name):
    query_path = _get_sql_folder() / f"{query_name}"  # .sql"
    with open(query_path, encoding="utf-8-sig") as query:
        return query.read()


def list_queries():
    query_names = []
    for sqlfile in _get_sql_folder().glob("*.sql"):
        query_names.append(sqlfile.stem)
    return query_names
