import requests
from config import JIRA_DOMAIN, auth, headers

MAX_RESULTS_PER_PAGE = 50

def extract_comment_text(comment_obj):
    if not comment_obj:
        return ""

    try:
        content = comment_obj.get("content", [])
        text_parts = []

        for block in content:
            if block.get("type") == "paragraph":
                for inner in block.get("content", []):
                    if inner.get("type") == "text":
                        text_parts.append(inner.get("text", ""))
        return " ".join(text_parts).strip()
    except Exception as e:
        return ""


def get_issues_with_worklogs(target_user):
    start_at = 0
    all_issues = []

    while True:
        params = {
            "jql": f'worklogAuthor = "{target_user}"',
            "fields": "key",
            "maxResults": MAX_RESULTS_PER_PAGE,
            "startAt": start_at
        }

        response = requests.get(
            f"https://{JIRA_DOMAIN}/rest/api/3/search",
            headers=headers,
            auth=auth,
            params=params
        )
        response.raise_for_status()
        issues = response.json().get("issues", [])
        if not issues:
            break

        all_issues.extend(issues)
        if len(issues) < MAX_RESULTS_PER_PAGE:
            break
        start_at += MAX_RESULTS_PER_PAGE

    return all_issues

def fetch_user_worklogs(issues, target_user, date_from, date_to):
    filtered_logs = []

    for issue in issues:
        issue_key = issue["key"]
        worklog_url = f"https://{JIRA_DOMAIN}/rest/api/3/issue/{issue_key}/worklog"
        response = requests.get(worklog_url, headers=headers, auth=auth)
        response.raise_for_status()
        worklogs = response.json().get("worklogs", [])

        for log in worklogs:
            author = log["author"]
            author_email = author.get("emailAddress", "unknown")
            account_id = author.get("accountId")

            if target_user != author_email and target_user != account_id:
                continue

            started = log["started"]
            if date_from <= started < date_to:
                filtered_logs.append({
                    "started": started,
                    "issue": issue_key,
                    "timeSpent": log["timeSpent"],
                    "comment": extract_comment_text(log.get("comment", {})),
                    "author": author_email
                })

    filtered_logs.sort(key=lambda x: x["started"], reverse=True)
    return filtered_logs
