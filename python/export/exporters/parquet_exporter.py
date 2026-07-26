"""
Export DataFrame to Parquet file.
"""


def export(df, output_file):

    if df.empty:
        raise ValueError("No records to export.")

    df.to_parquet(output_file, index=False)
