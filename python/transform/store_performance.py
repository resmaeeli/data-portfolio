"""
Transform "07-store-performance.sql" query results into structured records.
"""


def transform_store_performance(rows):
    result = []

    for store_id, city, country, rental_count, total_revenue in rows:
        result.append({
            "Store ID": store_id,
            "City": city,
            "Country": country,
            "Rental Count" : rental_count,
            "Total Revenue": total_revenue            
            })

    return result
