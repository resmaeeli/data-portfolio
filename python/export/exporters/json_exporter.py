"""
Export structured records to a JSON file.
"""

import json


def export(records, output_file):

    if not records:
        raise ValueError("No records to export.")

    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(records, file, indent=4, default=str)
