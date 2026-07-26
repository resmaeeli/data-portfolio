"""
Transform "08-top-films-by-rental.sql" query results into DataFrame.
"""

import pandas as pd


def transform_top_films_by_rental(rows, columns):
    df = pd.DataFrame(rows, columns=columns)
    return df
