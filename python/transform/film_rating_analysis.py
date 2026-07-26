"""
Transform "06-film-rating-analysis.sql" query results into DataFrame.
"""

import pandas as pd


def transform_film_rating_analysis(rows, columns):
    df = pd.DataFrame(rows, columns=columns)
    return df
