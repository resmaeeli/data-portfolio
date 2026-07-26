"""
Transform "04-monthly-sales-trend.sql" query results into DataFrame.
"""

import pandas as pd


def transform_monthly_sales_trend(rows, columns):
    df = pd.DataFrame(rows, columns=columns)
    return df
