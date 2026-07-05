"""
Export yearly order statistics from AdventureWorks to CSV.
"""

from database import get_connection
from queries import load_query
from transform import transform_orders_per_year
from export_csv import export_to_csv

# import csv

# Connect to odbc , using cursor and fetch data
with get_connection() as connection:
    cursor = connection.cursor()
    cursor.execute(load_query("01-orders-per-year"))
    rows = cursor.fetchall()

    # Transforming records
    transformed_rows = transform_orders_per_year(rows)

    # Export query results to CSV
    output_file_path = "data/orders_per_year.csv"
    export_to_csv(transformed_rows, output_file_path)
