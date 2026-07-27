"""
Run the export pipeline from query execution to selected output format.
"""

import time
from pathlib import Path
from database import get_connection, load_query
from .export_factory import get_exporter
from utils import logger_pipeline, logger_error


def run_export(query_name, db_type, transformer, output_file, file_format):
    """Run the export pipeline and write the output using the selected exporter."""
    output_file = Path(output_file).stem
    output_path = (
        Path(__file__).parent.parent.parent / "data" / f"{output_file}.{file_format}"
    )

    query = load_query(db_type, query_name)

    start_time = time.time()

    with get_connection(db_type) as connection:
        cursor = connection.cursor()
        cursor.execute(query)
        columns = [column[0] for column in cursor.description]
        rows = cursor.fetchall()

    rows = [tuple(row) for row in rows]
    transformed_df = transformer(rows, columns)

    logger_pipeline.info(f"Export completed: {output_path}")

    exporter = get_exporter(file_format)
    exporter(transformed_df, output_path)

    duration = time.time() - start_time

    logger_pipeline.info(
        f"Job Completed : Duration: {duration:.2f} | Records : {len(rows)} | Query Name: {query_name}"
    )
