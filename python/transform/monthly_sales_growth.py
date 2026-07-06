"""
Transform "monthly sales growth" query results into structured records.
"""


def transform_monthly_sales_growth(rows):
    result = []

    for SalesYear, SalesMonth, TotalSales, PreviousMonthSales, GrowthAmount in rows:
        result.append(
            {
                "SalesYear": SalesYear,
                "SalesMonth": SalesMonth,
                "TotalSales": TotalSales,
                "PreviousMonthSales": PreviousMonthSales,
                "GrowthAmount": GrowthAmount,
            }
        )

    return result
