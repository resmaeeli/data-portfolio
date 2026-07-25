"""
Transform "09-film-length-analysis.sql" query results into structured records.
"""


def transform_film_length_analysis(rows):
    result = []

    for length_category, film_count, average_length in rows:
        result.append({
            "Lenght Category": length_category,
            "Film Count": film_count,            
            "Average Length":average_length
            })

    return result
