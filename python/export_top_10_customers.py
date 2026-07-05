"""
Configure and run the top 10 customers export job.
"""

# lib imports
from transform import transform_top_10_customers
from export_runner import run_export

# values
query_name = "02-top-10-customers"
transformer = transform_top_10_customers
output_file = "data/top_10_customers.csv"

# exporting data
run_export(query_name, transformer, output_file)
