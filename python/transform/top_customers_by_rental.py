"""
Transform "04-top-customers-by-rental.sql" query results into DataFrame.
"""

import pandas as pd


def transform_top_customers_by_rental(rows, columns):
    df = pd.DataFrame(rows, columns=columns)
    return df
