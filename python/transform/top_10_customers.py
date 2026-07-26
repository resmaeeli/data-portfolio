"""
Transform "02-top-10-customers.sql" query results into DataFrame.
"""

import pandas as pd

def transform_top_10_customers(rows, columns):
    df = pd.DataFrame(rows , columns=columns)
    return df    
