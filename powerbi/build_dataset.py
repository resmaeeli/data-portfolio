"""
Generate all datasets required by the Power BI dashboard.
"""

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
        print(f"Running: {job['name']}")
        run_job(job["name"], "csv")

    print("\nDone.")


if __name__ == "__main__":
    main()