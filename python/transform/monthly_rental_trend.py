"""
Transform "03-monthly-rental-trend.sql" query results into DataFrame.
"""

import pandas as pd


def transform_monthly_rental_trend(rows, columns):
    df = pd.DataFrame(rows, columns=columns)
    return df
