"""
Run the export pipeline from query execution to CSV output.
"""

from pathlib import Path
from database import get_connection, load_query
from .export_csv import export_to_csv


def run_export(
    query_name,
    transformer,
    output_file,
):

    output_path = Path(__file__).parent.parent.parent / "data" / output_file
    query = load_query(query_name)

    # Connect to odbc , using cursor and fetch data
    with get_connection() as connection:
        cursor = connection.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()

    # Transforming records
    transformed_rows = transformer(rows)

    # Export query results to CSV
    export_to_csv(transformed_rows, output_path)
