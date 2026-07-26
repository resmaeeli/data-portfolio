"""
Transform "07-store-performance.sql" query results into DataFrame.
"""

import pandas as pd


def transform_store_performance(rows, columns):
    df = pd.DataFrame(rows, columns=columns)
    return df
