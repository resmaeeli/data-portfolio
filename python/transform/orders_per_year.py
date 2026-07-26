"""
Transform "01-orders-per-year.sql" query results into DataFrame.
"""

import pandas as pd

def transform_orders_per_year(rows, columns):    
    df = pd.DataFrame(rows , columns=columns)
    return df
