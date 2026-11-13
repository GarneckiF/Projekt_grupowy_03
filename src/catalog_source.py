"""Minimal local CSV preview infrastructure; semantic validation is student work."""
import csv
from pathlib import Path

REQUIRED_COLUMNS = ['OBJECT_NAME', 'OBJECT_ID', 'NORAD_CAT_ID', 'OBJECT_TYPE', 'OPS_STATUS_CODE', 'OWNER', 'LAUNCH_DATE', 'LAUNCH_SITE', 'DECAY_DATE', 'PERIOD', 'INCLINATION', 'APOGEE', 'PERIGEE', 'RCS', 'DATA_STATUS_CODE', 'ORBIT_CENTER', 'ORBIT_TYPE']


def read_catalog(path):
    """Read the complete assigned CSV as strings, without changing the input."""
    with Path(path).open(encoding="utf-8-sig", newline="") as stream:
        reader = csv.DictReader(stream)
        if reader.fieldnames is None:
            raise ValueError("CSV is empty or has no header.")
        if len(set(reader.fieldnames)) != len(reader.fieldnames):
            raise ValueError("CSV contains duplicate column names.")
        missing = set(REQUIRED_COLUMNS) - set(reader.fieldnames)
        if missing:
            raise ValueError("Missing required columns: " + ", ".join(sorted(missing)))
        records = []
        for line_number, row in enumerate(reader, 2):
            if None in row or any(value is None for value in row.values()):
                raise ValueError(f"Wrong CSV field count near record {line_number}.")
            records.append(row)
    return records
