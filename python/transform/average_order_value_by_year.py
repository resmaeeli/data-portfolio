"""
Transform "09-average-order-value-by-year.sql" query results into DataFrame.
"""

import pandas as pd

def transform_average_order_value_by_year(rows , columns):
    df = pd.DataFrame(rows , columns=columns)
    return df