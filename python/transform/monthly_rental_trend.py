"""
Transform "03-monthly-rental-trend.sql" query results into structured records.
"""


def transform_monthly_rental_trend(rows):
    result = []

    for rental_month, rental_count, total_revenue in rows:
        result.append({
            "Rental Month": rental_month,
            "Rental Count": rental_count,
            "Total Revenue": total_revenue             
            })

    return result
