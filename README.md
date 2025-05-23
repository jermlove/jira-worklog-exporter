# 🧾 Jira Worklog Exporter

This tool allows you to export your Jira worklogs into an Excel spreadsheet, complete with:

- A full log of your entries
- A summary of total time by issue
- A summary of total time by day
- A total time footer row

## 🚀 Features

- Supports date ranges like `This Week`, `Last Week`, `This Month`, etc.
- Filter by any user's email address
- Outputs to an organized Excel workbook
- Automatically calculates totals and formats time

---

## 🔐 Step 1: Get Your Jira API Token

1. Visit [https://id.atlassian.com/manage-profile/security/api-tokens](https://id.atlassian.com/manage-profile/security/api-tokens)
2. Click **"Create API token"**
3. Name it something like `Jira Worklog Exporter`
4. Click **Create**, then **Copy to clipboard**
5. Store it in a safe place — you will use this in your `.env` file

---

## ⚙️ Step 2: Configure Environment Variables

Create a `.env` file in the project root with the following content:

```env
JIRA_BASE_URL=https://your-domain.atlassian.net
JIRA_EMAIL=your.email@example.com
JIRA_API_TOKEN=your_api_token_here
```
Replace the values with your actual Jira domain and credentials.

## 📦 Step 3: Install Dependencies
Make sure you have Python 3.8+ installed.

Then install dependencies:
```bash
pip install -r requirements.txt
```
If you don't have a requirements.txt, use:
```bash
pip install requests openpyxl python-dotenv pytz
```

## 🧠 Step 4: Supported Date Ranges
You can use the following presets as the --date_range value:

- This Week
- Last Week
- This Month
- Last Month
- This Year

## 🖥️ Step 5: Run the Script
```bash
python main.py --user your.email@example.com --date_range "Last Week"
```
- --user = the Jira user email whose logs you want (typically yourself)
- --date_range = one of the supported date ranges above

## 📂 Output
The script will generate an Excel file inside the `/exports` directory:
```java
exports/
├── worklogs_your_email_at_domain_com_Apr2024-Week_2.xlsx
```
The workbook contains:
- ✅ Work Logs: Full log of entries
- ✅ Summary by Issue: Aggregated hours per Jira issue
- ✅ Summary by Day: Aggregated hours per day
- ✅ Footer row in Work Logs showing total time in hours and minutes

## 🧼 Example Output (Work Logs Sheet)
| started    | issue   | timeSpent    | comment               | author          |
| ---------- | ------- | ------------ | --------------------- | --------------- |
| 2025-05-13 | XYZ-123 | 2h 30m       | Finished login screen | your.email\@... |
| TOTAL TIME |         | 2 hrs 30 min |                       |                 |

## 📋 Optional: Export Logs for Another User
To get worklogs for a teammate (if you have permission):
```bash
python main.py --user colleague@example.com --date_range "This Month"
```

## ❓ Troubleshooting
- If the script returns no data, ensure:
    - The date range includes worklogs
    - The user's email is correct
    - Your API token is valid    
- Make sure your Jira user has permission to view other users' worklogs (if applicable)