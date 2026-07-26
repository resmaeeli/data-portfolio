"""
Choosing fit exporter using selected file format.
"""

from config import load_app_settings
from .exporters import csv_export
from .exporters import json_export
from .exporters import parquet_export

EXPORTERS = {
    "csv": csv_export,
    "json": json_export,
    "parquet": parquet_export,
}


def get_exporter(file_format):

    supported_formats = load_app_settings()["supported_output_formats"]

    if file_format not in supported_formats:
        raise ValueError(f"Unsupported export format: {file_format}")

    try:
        return EXPORTERS[file_format]
    except KeyError:
        raise RuntimeError(f"No exporter registered for '{file_format}'.")
