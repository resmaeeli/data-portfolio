"""
Transform "sales by product category" query results into structured records.
"""


def transform_sales_by_product_category(rows):
    result = []

    for CategoryName, TotalQuantitySold, TotalSalesAmount in rows:
        result.append(
            {
                "CategoryName": CategoryName,
                "TotalQuantitySold": TotalQuantitySold,
                "TotalSalesAmount": TotalSalesAmount,
            }
        )

    return result
