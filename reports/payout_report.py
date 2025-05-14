DEPARTMENT_FIELD_MAX_LEN = 15
NAME_FIELD_MAX_LEN = 25
HOURS_FIELD_MAX_LEN = 5
RATE_FIELD_MAX_LEN = 5
PAYOUT_FIELD_MAX_LEN = 6
PADDING = 1
class PayoutReport:
    def generate(self, data: list[dict]) -> str:
        departments = {}

        for emp in data:
            dept = emp["department"]
            if dept not in departments:
                departments[dept] = []
            departments[dept].append(emp)

        lines = []
        lines.append(f"{' '*15} {'name':<25} {'hours':<5} {'rate':<5} payout")

        for dept, employees in departments.items():
            lines.append(f"{dept}")
            total_hours = 0
            total_payout = 0

            for emp in employees:
                name = emp["name"]
                name = name[:NAME_FIELD_MAX_LEN- 4] + "..." if len(name) > NAME_FIELD_MAX_LEN else name

                hours = emp["hours_worked"]
                total_hours += hours
                rate = emp["hourly_rate"]
                payout = int(hours * rate)
                total_payout += payout

                hours = str(hours)
                hours = hours[:HOURS_FIELD_MAX_LEN - 4] + "..." if len(hours) > HOURS_FIELD_MAX_LEN else hours

                rate = str(rate)
                rate = rate[:RATE_FIELD_MAX_LEN - 4] + "..." if len(rate) > RATE_FIELD_MAX_LEN else rate


                payout = str(payout)
                payout = payout[:PAYOUT_FIELD_MAX_LEN - 4] + "..." if len(payout) > PAYOUT_FIELD_MAX_LEN else payout




                lines.append(f"{'-'*DEPARTMENT_FIELD_MAX_LEN}{'':>{PADDING}}{name:<{NAME_FIELD_MAX_LEN}}{'':>{PADDING}}{hours:<{HOURS_FIELD_MAX_LEN}}{'':>{PADDING}}{rate:<{RATE_FIELD_MAX_LEN}}{'':>{PADDING}}${payout:<{PAYOUT_FIELD_MAX_LEN}}")


            lines.append(f"{'':>{DEPARTMENT_FIELD_MAX_LEN + PADDING + NAME_FIELD_MAX_LEN + PADDING}}{total_hours:<{HOURS_FIELD_MAX_LEN}}{'':>{PADDING}}{'':>{RATE_FIELD_MAX_LEN}}{'':>{PADDING}}${total_payout}\n")

        return "\n".join(lines)


def get_report(report_type: str):
    if report_type == "payout":
        return PayoutReport()
    else:
        raise ValueError(f"Unsupported report type: {report_type}")
