def map_columns(headers: list[str]) -> list[str]:
    mapping = {
        "rate": "hourly_rate",
        "salary": "hourly_rate"
    }
    return [mapping.get(h, h) for h in headers]
