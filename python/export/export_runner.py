"""
Run the export pipeline from query execution to CSV output.
"""

from pathlib import Path
from database import get_connection, load_query
from .export_factory import get_exporter


def run_export(query_name, transformer, output_file, file_format):
    """Run the export pipeline and write the output using the selected exporter."""
    output_file = Path(output_file).stem
    output_path = (
        Path(__file__).parent.parent.parent / "data" / f"{output_file}.{file_format}"
    )

    query = load_query(query_name)

    with get_connection() as connection:
        cursor = connection.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()

    transformed_rows = transformer(rows)

    exporter = get_exporter(file_format)
    exporter(transformed_rows, output_path)
