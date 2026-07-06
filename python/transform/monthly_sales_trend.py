"""
Transform "monthly sales trend" query results into structured records.
"""


def transform_monthly_sales_trend(rows):
    result = []

    for SalesYear, SalesMonth, OrderCount, TotalSales in rows:
        result.append(
            {
                "SalesYear": SalesYear,
                "SalesMonth": SalesMonth,
                "OrderCount": OrderCount,
                "TotalSales": TotalSales,
            }
        )

    return result
