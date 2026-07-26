"""
Transform "09-film-length-analysis.sql" query results into DataFrame.
"""

import pandas as pd


def transform_film_length_analysis(rows, columns):
    df = pd.DataFrame(rows, columns=columns)
    return df
