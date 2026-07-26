"""
Export DataFrame to CSV file.
"""

def export(df, output_file):

    if df.empty:
        raise ValueError("No records to export.")

    df.to_csv(
        output_file,
        index=False,
        encoding="utf-8"
    )