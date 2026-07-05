"""
Run the export pipeline from query execution to CSV output.
"""

from database import get_connection
from queries import load_query
from export_csv import export_to_csv


def run_export(
    query_name,
    transformer,
    output_file,
):
    # Connect to odbc , using cursor and fetch data
    with get_connection() as connection:
        cursor = connection.cursor()
        cursor.execute(load_query(query_name))
        rows = cursor.fetchall()

    # Transforming records
    transformed_rows = transformer(rows)

    # Export query results to CSV
    export_to_csv(transformed_rows, output_file)
