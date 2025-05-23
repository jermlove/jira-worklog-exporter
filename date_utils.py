from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import pytz

def get_date_from_preset(preset):
    now = datetime.now(pytz.utc)

    if preset == "This Week":
        start = now - timedelta(days=now.weekday())
    elif preset == "Last Week":
        start = now - timedelta(days=now.weekday() + 7)
    elif preset == "This Month":
        start = now.replace(day=1)
    elif preset == "Last Month":
        first_day_this_month = now.replace(day=1)
        start = first_day_this_month - relativedelta(months=1)
        start = start.replace(day=1)
    elif preset == "This Year":
        start = now.replace(month=1, day=1)
    else:
        raise ValueError("Invalid preset.")
    return start.strftime("%Y-%m-%dT00:00:00.000+0000")

def get_safe_range_name(preset, date_from_str):
    now = datetime.now(pytz.utc)
    date_from = datetime.strptime(date_from_str, "%Y-%m-%dT%H:%M:%S.000+0000")

    def format_week(date):
        first_of_month = date.replace(day=1)
        week_num = ((date - first_of_month).days // 7) + 1
        return f"{date.strftime('%b%Y')}-Week{week_num}"

    if preset in ["This Week", "Last Week"]:
        return format_week(date_from)
    elif preset in ["This Month", "Last Month"]:
        return date_from.strftime("%b%Y")
    elif preset == "This Year":
        return date_from.strftime("%Y")
    else:
        end_date = now
        return f"{date_from.strftime('%b%d%Y')}-{end_date.strftime('%b%d%Y')}"

def get_date_range_from_preset(preset):
    now = datetime.now(pytz.utc)

    if preset == "This Week":
        start = now - timedelta(days=now.weekday())
        end = start + timedelta(days=7)
    elif preset == "Last Week":
        end = now - timedelta(days=now.weekday())
        start = end - timedelta(days=7)
    elif preset == "This Month":
        start = now.replace(day=1)
        end = start + relativedelta(months=1)
    elif preset == "Last Month":
        end = now.replace(day=1)
        start = (end - relativedelta(months=1)).replace(day=1)
    elif preset == "This Year":
        start = now.replace(month=1, day=1)
        end = start.replace(year=start.year + 1)
    else:
        raise ValueError("Invalid preset.")

    return (
        start.strftime("%Y-%m-%dT00:00:00.000+0000"),
        end.strftime("%Y-%m-%dT00:00:00.000+0000")
    )
