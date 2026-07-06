"""
Transform "top 10 products by quantity sold" query results into structured records.
"""


def transform_top_10_products_by_quantity_sold(rows):
    result = []

    for ProductName, TotalQuantitySold in rows:
        result.append(
            {
                "ProductName": ProductName,
                "TotalQuantitySold": TotalQuantitySold,
            }
        )

    return result
