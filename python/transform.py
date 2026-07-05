"""
Transform database query results into structured records.
"""


def transform_orders_per_year(rows):
    result = []

    for year, count in rows:
        result.append({"Year": year, "Count": count})

    return result


def transform_top_10_customers(rows):
    result = []

    for StoreName, PersonName, TotalPurchasedAmount in rows:
        result.append(
            {
                "StoreName": StoreName,
                "PersonName": PersonName,
                "TotalPurchasedAmount": TotalPurchasedAmount,
            }
        )

    return result
