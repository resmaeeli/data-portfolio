"""
Run the export pipeline from query execution to CSV output.
"""

from database import get_connection
from queries import load_query
from export_csv import export_to_csv
from config_loader import load_jobs
import transform
from pathlib import Path


def run_export(
    query_name,
    transformer,
    output_file,
):

    output_path = Path(__file__).parent.parent / "data" / output_file
    # Connect to odbc , using cursor and fetch data
    with get_connection() as connection:
        cursor = connection.cursor()
        cursor.execute(load_query(query_name))
        rows = cursor.fetchall()

    # Transforming records
    transformed_rows = transformer(rows)

    # Export query results to CSV
    export_to_csv(transformed_rows, output_path)


def run_job(job_name):

    job_list = load_jobs()

    for job in job_list:
        if job["name"] == job_name:

            transformer = getattr(transform, job["transformer"])

            run_export(
                query_name=job["query"],
                transformer=transformer,
                output_file=job["output"],
            )

            break
