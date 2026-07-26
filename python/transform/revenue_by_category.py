"""
Transform "05-revenue-by-category.sql" query results into DataFrame.
"""

import pandas as pd


def transform_revenue_by_category(rows, columns):
    df = pd.DataFrame(rows, columns=columns)
    return df
