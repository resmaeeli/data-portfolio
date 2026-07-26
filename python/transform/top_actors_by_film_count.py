"""
Transform "01-top-actors-by-film-count.sql" query results into DataFrame.
"""

import pandas as pd


def transform_top_actors_by_film_count(rows, columns):
    df = pd.DataFrame(rows, columns=columns)
    return df
