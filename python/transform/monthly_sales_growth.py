"""
Transform "10-monthly-sales-growth.sql" query results into DataFrame.
"""

import pandas as pd


def transform_monthly_sales_growth(rows, columns):
    df = pd.DataFrame(rows, columns=columns)
    return df
