"""
Transform "05-revenue-by-category.sql" query results into structured records.
"""


def transform_revenue_by_category(rows):
    result = []

    for category_id, category_name, payment_count, total_revenue in rows:
        result.append({
            "Category ID": category_id,
            "Category Name": category_name,
            "Payment Count": payment_count,
            "Total Revenue": total_revenue
            })

    return result
