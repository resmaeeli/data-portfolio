"""
Generate all datasets required by the Power BI dashboard.
"""

from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "python"))

from utils import logger_pipeline, logger_error
from config import load_app_settings
from config import load_jobs
from run import run_job


def main(output_format=None):
    try:
        jobs = load_jobs()

        print(f"Generating {len(jobs)} datasets...\n")

        for job in jobs:
            fmt = (
                output_format
                or job.get("file_format")
                or load_app_settings()["default_output_format"]
            )

            print(f"Running: {job['name']}.{fmt}")
            run_job(job["name"], fmt)

        print("\nDone.")
    except Exception as ex:
        logger_error.exception("Build_DataSet failed")
        raise


if __name__ == "__main__":
    cli_format = sys.argv[1] if len(sys.argv) > 1 else None
    main(cli_format)
