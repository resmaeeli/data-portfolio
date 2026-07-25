"""
Transform "06-film-rating-analysis.sql" query results into structured records.
"""


def transform_film_rating_analysis(rows):
    result = []

    for rating, film_count, average_length in rows:
        result.append({
            "Rating": rating,
            "Film Count": film_count,            
            "Average Length":average_length
            })

    return result
