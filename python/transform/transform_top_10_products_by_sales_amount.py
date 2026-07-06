"""
Transform "top 10 products by sales amount" query results into structured records.
"""


def transform_top_10_products_by_sales_amount(rows):
    result = []

    for ProductID, ProductName, TotalSalesAmount in rows:
        result.append(
            {
                "ProductID": ProductID,
                "ProductName": ProductName,
                "TotalSalesAmount": TotalSalesAmount,
            }
        )

    return result
