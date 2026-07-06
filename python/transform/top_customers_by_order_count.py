"""
Transform "top customers by order count" query results into structured records.
"""


def transform_top_customers_by_order_count(rows):
    result = []

    for CustomerName, CustomerID, OrderCount in rows:
        result.append(
            {
                "CustomerName": CustomerName,
                "CustomerID": CustomerID,
                "OrderCount": OrderCount,
            }
        )

    return result
