from cli import parse_args
from date_utils import get_date_range_from_preset
from jira_api import get_issues_with_worklogs, fetch_user_worklogs
from exporter import export_to_excel

def main():
    args = parse_args()
    date_from, date_to = get_date_range_from_preset(args.date_range)
    print(f"🔍 Fetching logs for {args.user} since {date_from} to {date_to}...")

    issues = get_issues_with_worklogs(args.user)
    logs = fetch_user_worklogs(issues, args.user, date_from, date_to)
    export_to_excel(logs, args.user, args.date_range, date_from)

if __name__ == "__main__":
    main()
