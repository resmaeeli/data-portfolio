"""
Transform "03-top-10-products-by-sales-amount.sql" query results into DataFrame.
"""

import pandas as pd


def transform_top_10_products_by_sales_amount(rows, columns):
    df = pd.DataFrame(rows, columns=columns)
    return df
