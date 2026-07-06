"""
Transform "average order value by year" query results into structured records.
"""


def transform_average_order_value_by_year(rows):
    result = []

    for OrderYear, OrderCount, AverageOrderValue in rows:
        result.append(
            {
                "OrderYear": OrderYear,
                "OrderCount": OrderCount,
                "AverageOrderValue": AverageOrderValue,
            }
        )

    return result
