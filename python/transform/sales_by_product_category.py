"""
Transform "07-sales-by-product-category.sql" query results into DataFrame.
"""

import pandas as pd


def transform_sales_by_product_category(rows, columns):
    df = pd.DataFrame(rows, columns=columns)
    return df
