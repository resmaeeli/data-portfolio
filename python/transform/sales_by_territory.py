"""
Transform "sales by territory" query results into structured records.
"""


def transform_sales_by_territory(rows):
    result = []

    for TerritoryName, OrderCount, TotalSalesAmount in rows:
        result.append(
            {
                "TerritoryName": TerritoryName,
                "OrderCount": OrderCount,
                "TotalSalesAmount": TotalSalesAmount,
            }
        )

    return result
