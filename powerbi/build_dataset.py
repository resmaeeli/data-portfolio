"""
Generate all datasets required by the Power BI dashboard.
"""

from config import load_app_settings
from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parent.parent

sys.path.insert(0, str(PROJECT_ROOT / "python"))

from run import run_job
from config import load_jobs


def main():
    jobs = load_jobs()

    print(f"Generating {len(jobs)} datasets...\n")

    for job in jobs:
        output_format = (
            sys.argv[1]
            if len(sys.argv) > 1
            else (
                job.get("file_format") or load_app_settings()["default_output_format"]
            )
        )

        print(f"Running: {job['name']}.{output_format}")
        run_job(job["name"], output_format)

    print("\nDone.")


if __name__ == "__main__":
    main()
