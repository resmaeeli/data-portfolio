"""
Transform database query results into structured records.
"""


def transform_orders_per_year(rows):
    result = []

    for year, count in rows:
        result.append({"Year": year, "Count": count})

    return result
