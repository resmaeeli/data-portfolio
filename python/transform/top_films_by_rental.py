"""
Transform "08-top-films-by-rental.sql" query results into structured records.
"""


def transform_top_films_by_rental(rows):
    result = []

    for film_id, title, rental_count , total_revenue in rows:
        result.append({
            "Customer ID": film_id,
            "First Name": title,            
            "Rental Count":rental_count,
            "Total Revenue" : total_revenue
            })

    return result
