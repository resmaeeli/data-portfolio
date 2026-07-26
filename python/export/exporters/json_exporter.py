"""
Export DataFrame to JSON file.
"""

def export(df, output_file):

    if df.empty:
        raise ValueError("No records to export.")

    df.to_json(
        output_file,
        orient="records",
        indent=4,
        date_format="iso"
    )