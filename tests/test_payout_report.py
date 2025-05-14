import pytest
from reports.payout_report import PayoutReport

def test_generate_payout():
    report = PayoutReport()
    data = [
        {"name": "Alice", "department": "Marketing", "hours_worked": 160, "hourly_rate": 50},
        {"name": "Bob", "department": "Design", "hours_worked": 150, "hourly_rate": 40}
    ]
    result = report.generate(data)
    assert "Alice" in result
    assert "Bob" in result
    assert "8000" in result  # 160 * 50
    assert "6000" in result  # 150 * 40
