"""
Provides functions for loading export job configurations.
"""

from pathlib import Path
import json


def load_jobs():
    """Load export jobs from configuration file."""

    json_file = Path(__file__).parent.parent.parent / "config/export_jobs.json"

    with open(json_file, "r", encoding="utf-8") as file:
        records = json.load(file)

    return records["jobs"]
