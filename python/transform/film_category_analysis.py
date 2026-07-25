"""
Transform "02-film-category-analysis.sql" query results into structured records.
"""


def transform_film_category_analysis(rows):
    result = []

    for category_id, category_name, film_count , average_length in rows:
        result.append({
            "Category ID": category_id,
            "Category Name": category_name,
            "Film Count":film_count, 
            "Average Length":average_length
            })

    return result
