"""
Run export jobs from the command line.
"""

import sys
import transform
from config import load_jobs
from export import run_export
from config.loader import load_app_settings


def run_job(job_name, file_format):
    """Run an export job by name."""

    job_list = load_jobs()

    for job in job_list:
        if job["name"] == job_name:
            transformer = getattr(transform, job["transformer"])

            if file_format is not None:
                output_format = file_format

            elif job.get("file_format") is not None:
                output_format = job["file_format"]

            else:
                settings = load_app_settings()
                output_format = settings["default_output_format"]

            run_export(
                query_name=job["query"],
                transformer=transformer,
                output_file=job["output"],
                file_format=output_format,
            )

            return

    raise ValueError(f"Unknown job: {job_name}")


if __name__ == "__main__":
    try:

        if len(sys.argv) < 2 or len(sys.argv) > 3:
            raise ValueError(
                "Usage: python run_job.py <job_name> | <file_format> (optional)"
            )

        _file_format = None
        if len(sys.argv) > 2:
            _file_format = sys.argv[2]
            if not _file_format in ("csv", "json"):
                raise ValueError("File format is not acceptable.")

        job_name = sys.argv[1]
        run_job(job_name, _file_format)

    except ValueError as ex:
        print(ex)
        sys.exit(1)
