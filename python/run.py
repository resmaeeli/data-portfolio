"""
Run export jobs from the command line.
"""

import sys
import transform
from config import load_jobs
from export import run_export
from config.loader import load_app_settings


def run_job(job_name, file_format):
    """Run the selected export job using the requested or configured output format."""

    job_list = load_jobs()

    for job in job_list:
        if job["name"] == job_name:
            transformer = getattr(transform, job["transformer"])

            if file_format is not None:
                output_format = file_format

            elif job.get("file_format") is not None:
                output_format = job["file_format"]

            else:
                output_format = load_app_settings()["default_output_format"]

            run_export(
                query_name=job["query"],
                db_type=job["database"],
                transformer=transformer,
                output_file=job["output"],
                file_format=output_format,
            )

            return

    raise ValueError(f"Unknown job: {job_name}")


# run_job("orders_per_year" , 'csv')


if __name__ == "__main__":
    try:

        if len(sys.argv) < 2 or len(sys.argv) > 3:
            raise ValueError(
                "Usage: python run_job.py <job_name> | <file_format> (optional)"
            )

        _file_format = None
        if len(sys.argv) > 2:
            _file_format = sys.argv[2]

        job_name = sys.argv[1]
        run_job(job_name, _file_format)

    except ValueError as ex:
        print(ex)
        sys.exit(1)
