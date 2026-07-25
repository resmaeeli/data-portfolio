"""
Transform "04-top-customers-by-rental.sql" query results into structured records.
"""


def transform_top_customers_by_rental(rows):
    result = []

    for customer_id, first_name, last_name , rental_count in rows:
        result.append({
            "Customer ID": customer_id,
            "First Name": first_name,
            "Last Name":last_name, 
            "Rental Count":rental_count
            })

    return result
