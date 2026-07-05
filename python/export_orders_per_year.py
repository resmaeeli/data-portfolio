"""
Configure and run the yearly orders export job.
"""

from export_runner import run_job

run_job("orders_per_year")
