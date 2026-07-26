"""
Transform "05-top-customers-by-order-count.sql" query results into DataFrame.
"""

import pandas as pd


def transform_top_customers_by_order_count(rows, columns):
    df = pd.DataFrame(rows, columns=columns)
    return df
