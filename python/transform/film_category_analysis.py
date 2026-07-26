"""
Transform "02-film-category-analysis.sql" query results into DataFrame.
"""

import pandas as pd


def transform_film_category_analysis(rows, columns):
    df = pd.DataFrame(rows, columns=columns)
    return df
