"""
Load SQL queries from the repository.
"""

from pathlib import Path


# get base folder of sql queries
def _get_query_folder(db_type):
    return Path(__file__).parent.parent.parent /"db" / db_type


# loading sql queries dynamically
def load_query(db_type , query_name):
    query_path = _get_query_folder(db_type) / f"{query_name}" 
    with open(query_path, encoding="utf-8-sig") as query:
        return query.read()


def list_queries(db_type):
    query_names = []
    for sqlfile in _get_query_folder(db_type).glob("*.sql"):
        query_names.append(sqlfile.stem)
    return query_names
