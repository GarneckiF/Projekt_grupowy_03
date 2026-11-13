"""Preview the assigned CSV; extend this entry point with the team's features."""
import argparse
from pathlib import Path
from src.catalog_source import read_catalog

BASE = Path(__file__).resolve().parent


def main():
    parser = argparse.ArgumentParser(description='Space Debris Population Analyzer: local CSV starter.')
    parser.add_argument("--data", type=Path, default=BASE / "data" / 'satcat.csv',
                        help="Path to the team's assigned local CSV, with the same schema.")
    parser.add_argument("--preview", type=int, default=10,
                        help="Rows to print; 0 prints all. Reading always covers the full CSV.")
    args = parser.parse_args()
    if args.preview < 0:
        parser.error("--preview must be nonnegative.")
    try:
        records = read_catalog(args.data)
    except (OSError, ValueError, UnicodeError) as error:
        parser.exit(1, f"Input error: {error}\n")
    print('Space Debris Population Analyzer')
    print(f"Dataset: {args.data.name} | Loaded {len(records)} records.")
    selected = records if args.preview == 0 else records[:args.preview]
    for row in selected:
        print(f"{row['NORAD_CAT_ID']:>7}  {row['OBJECT_NAME']}")
    print(f"Displayed {len(selected)} of {len(records)} records; all rows remain available for analysis.")


if __name__ == "__main__":
    main()
