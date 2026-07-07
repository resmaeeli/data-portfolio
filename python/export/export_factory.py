"""
Choosing fit exporter using selected file format.
"""

from .exporters import csv_export
from .exporters import json_export


def get_exporter(file_format):

    if file_format == "csv":
        return csv_export

    elif file_format == "json":
        return json_export

    else:
        raise ValueError(f"Unsupported export format: {file_format}")
