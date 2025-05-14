from .payout_report import PayoutReport

def get_report(report_type: str):
    if report_type == "payout":
        return PayoutReport()
    else:
        raise ValueError(f"Unsupported report type: {report_type}")