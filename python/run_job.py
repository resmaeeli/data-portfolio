"""
Run export jobs from the command line.
"""

import sys
import transform
from config_loader import load_jobs
from export_runner import run_export


def run_job(job_name):
    """Run an export job by name."""

    job_list = load_jobs()

    for job in job_list:
        if job["name"] == job_name:
            transformer = getattr(transform, job["transformer"])

            run_export(
                query_name=job["query"],
                transformer=transformer,
                output_file=job["output"],
            )
            return

    raise ValueError(f"Unknown job: {job_name}")


if __name__ == "__main__":
    try:

        if len(sys.argv) != 2:
            raise ValueError("Usage: python run_job.py <job_name>")

        job_name = sys.argv[1]
        run_job(job_name)

    except ValueError as ex:
        print(ex)
        sys.exit(1)
