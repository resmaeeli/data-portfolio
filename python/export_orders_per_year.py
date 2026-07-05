"""
Configure and run the yearly orders export job.
"""

# lib imports
from transform import transform_orders_per_year
from export_runner import run_export

# values
query_name = "01-orders-per-year"
transformer = transform_orders_per_year
output_file = "data/orders_per_year.csv"

# exporting data
run_export(query_name, transformer, output_file)
