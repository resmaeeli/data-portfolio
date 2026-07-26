"""
Transform "10-customer-activity-analysis.sql" query results into DataFrame.
"""

import pandas as pd


def transform_customer_activity_analysis(rows, columns):
    df = pd.DataFrame(rows, columns=columns)
    return df
