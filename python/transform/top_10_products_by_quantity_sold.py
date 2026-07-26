"""
Transform "06-top-10-products-by-quantity-sold.sql" query results into DataFrame.
"""

import pandas as pd


def transform_top_10_products_by_quantity_sold(rows, columns):
    df = pd.DataFrame(rows, columns=columns)
    return df
