"""
Transform "10-customer-activity-analysis.sql" query results into structured records.
"""


def transform_customer_activity_analysis(rows):
    result = []

    for customer_id, first_name, last_name , rental_count , last_rental_date in rows:
        result.append({
            "Customer ID": customer_id,
            "First Name": first_name,
            "Last Name":last_name, 
            "Rental Count":rental_count,
            "Last Rental Date" : last_rental_date
            })

    return result
