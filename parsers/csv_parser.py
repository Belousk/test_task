from utils.column_mapper import map_columns


def parse_csv_file(filepath: str) -> list[dict]:
    with open(filepath, encoding='utf-8') as f:
        lines = [line.strip() for line in f if line.strip()]

    headers = lines[0].split(",")
    headers = map_columns(headers)
    data = []

    for line in lines[1:]:
        values = line.split(",")
        entry = dict(zip(headers, values))
        entry["hours_worked"] = int(entry["hours_worked"])
        entry["hourly_rate"] = float(entry["hourly_rate"])
        data.append(entry)

    return data
