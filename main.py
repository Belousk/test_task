import argparse
from parsers.csv_parser import parse_csv_file
from reports import get_report

def main():
    parser = argparse.ArgumentParser(description="Generate employee reports from CSV files")
    parser.add_argument("files", nargs="+", help="Paths to CSV files")
    parser.add_argument("--report", required=True, help="Type of report to generate")
    args = parser.parse_args()
    try:
        all_data = []
        for file_path in args.files:
            all_data.extend(parse_csv_file(file_path))

        report = get_report(args.report)
        output = report.generate(all_data)
        print(output)

    except Exception as e:
        print(f"Error: {e}")
        exit(1)

if __name__ == "__main__":
    main()
