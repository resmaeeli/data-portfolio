"""
Transform "08-sales-by-territory.sql" query results into DataFrame.
"""

import pandas as pd


def transform_sales_by_territory(rows, columns):
    df = pd.DataFrame(rows, columns=columns)
    return df
