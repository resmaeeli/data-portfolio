"""
Export yearly order statistics from AdventureWorks to CSV.
"""

from database import get_connection
from queries import load_query
from transform import transform_orders_per_year
import csv

# Connect to odbc , using cursor and fetch data
with get_connection() as connection:
    cursor = connection.cursor()
    cursor.execute(load_query("01-orders-per-year"))
    rows = cursor.fetchall()

    # transforming records
    transformed_rows = transform_orders_per_year(rows)

    # Export query results to CSV
    output_file_path = "data/orders_per_year.csv"

    with open(output_file_path, "w", newline="", encoding="utf-8") as file:
        csv_writer = csv.DictWriter(file, fieldnames=["Year", "Count"])
        csv_writer.writeheader()
        csv_writer.writerows(transformed_rows)

        # csv_writer.writerow(["Year", "Count"])

        # csv_writer.writerows(rows)
        # for year, count in rows:
        #     csv_writer.writerow([year, count])

    ## closing objects
    # cursor.close()
