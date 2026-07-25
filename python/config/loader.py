"""
Provides functions for loading export job configurations.
"""

from pathlib import Path
import json


def _load_json(file_name):    
    """Load JSON configuration file."""

    with open(file_name, "r", encoding="utf-8-sig") as file:
        records = json.load(file)    
    return records


def load_jobs():
    """Load export jobs from configuration file."""

    json_file = Path(__file__).parent.parent.parent / "config/export_jobs.json"
    records = _load_json(json_file)
    return records["jobs"]


def load_app_settings():
    """Load items from system configuration file."""

    json_file = Path(__file__).parent.parent.parent / "config/app_settings.json"
    settings = _load_json(json_file)
    return settings


def load_db_config():
    """Load settings from database config file."""

    json_file = Path(__file__).parent.parent.parent/"config/db_config.json"
    db_settings = _load_json(json_file)
    return db_settings

    
def get_database_config(db_type):
    """ Load databse config from config file. """
    config = load_db_config()
    return config["databases"][db_type]