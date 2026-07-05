"""
Export structured records to a CSV file.
"""

import csv


def export_to_csv(records, output_file):

    with open(output_file, "w", newline="", encoding="utf-8") as file:
        csv_writer = csv.DictWriter(file, fieldnames=["Year", "Count"])
        csv_writer.writeheader()
        csv_writer.writerows(records)
