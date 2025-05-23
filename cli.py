import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Export Jira work logs.")
    parser.add_argument("--user", required=True, help="User email or accountId to filter logs")
    parser.add_argument("--date-range", required=True,
                        choices=["This Week", "Last Week", "This Month", "Last Month", "This Year"],
                        help="Date range preset")
    return parser.parse_args()
