"""
Transform "top 10 customers" query results into structured records.
"""


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
