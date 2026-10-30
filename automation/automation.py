
import os
import re
import datetime
import subprocess
import requests
import nws_api_fetch

# Locate directories
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TODAY_HTML_PATH = os.path.abspath(
    os.path.join(BASE_DIR, '..', 'site', 'todays-weather.html')
)
HISTORY_HTML_PATH = os.path.abspath(
    os.path.join(BASE_DIR, '..', 'site', 'weather-history.html')
)
REPO_ROOT = os.path.abspath(os.path.join(BASE_DIR, '..'))


def fetch_all_current_data():
    """Pull forecast data and active weather alerts."""
    try:
        data = nws_api_fetch.fetch_weather_data()

        headers = {
            "User-Agent": "lo-weather/1.0 (terpstragraham@gmail.com)"
        }

        alert_res = requests.get(
            'https://api.weather.gov/alerts/active/zone/ORZ006',
            headers=headers,
            timeout=15
        )
        alert_res.raise_for_status()

        alert_data = alert_res.json()
        features = alert_data.get('features', [])

        if features:
            data['alerts'] = " | ".join(
                f['properties']['headline'] for f in features
            )
        else:
            data['alerts'] = (
                "No active watches, warnings, or advisories at this time."
            )

        return data

    except Exception as e:
        print(f"Error compiling live metrics: {e}")
        return None


def get_ordinal_date_string():
    """Return today's date with its ordinal suffix."""
    today = datetime.date.today()
    day = today.day

    if 11 <= day <= 13:
        suffix = 'th'
    else:
        suffix = {1: 'st', 2: 'nd', 3: 'rd'}.get(day % 10, 'th')

    return today.strftime(f"%B {day}{suffix}")


def push_updates_to_github():
    """Sync-safe Git automation push."""
    try:
        os.chdir(REPO_ROOT)

        subprocess.run(
            ["git", "add", TODAY_HTML_PATH, HISTORY_HTML_PATH],
            check=True
        )

        status = subprocess.run(
            ["git", "status", "--porcelain"],
            capture_output=True,
            text=True,
            check=True
        )

        if not status.stdout.strip():
            print("No data changes detected. Skipping Git push.")
            return

        commit_msg = (
            f"Automated history update: Logged weather for "
            f"{get_ordinal_date_string()}"
        )

        subprocess.run(
            ["git", "commit", "-m", commit_msg],
            check=True
        )

        subprocess.run(
            ["git", "pull", "--rebase"],
            check=True
        )

        subprocess.run(["git", "push"], check=True)

        print(
            "Successfully pushed daily updates to GitHub! "
            "Vercel is now redeploying."
        )

    except subprocess.CalledProcessError as e:
        print(f"Git automation error: {e}")


def build_static_html_files(push_to_git=True):
    """Build today's weather page and update weather history."""

    print("Gathering NWS metrics for page build...")

    data = fetch_all_current_data()

    if not data:
        print("Build cancelled: NWS server data could not be reached.")
        return

    date_label = get_ordinal_date_string()

    high_temp = data.get('forecast-high', 'N/A')
    low_temp = data.get('forecast-low', 'N/A')
    day_sky = data.get('forecast-day-sky', 'Clear')
    night_sky = data.get('forecast-night-sky', 'Clear')
    alerts_text = data.get('alerts', 'No active alerts.')

    os.makedirs(os.path.dirname(TODAY_HTML_PATH), exist_ok=True)

    # Today's weather page
    today_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Today's Weather</title>
  <link rel="stylesheet" href="../style.css">
</head>
<body>
  <h1>Today's Weather</h1>
  <div style="position: fixed; top: 10px; right: 10px; color: blue; text-decoration: none;">
    <a href="javascript:history.back()" style="color: blue; text-decoration: none;"><- Back</a>
  </div>
  <p>Today, the weather in lake oswego.</p>
  <p>
  Temperatures<br>
  <br>
  High: {high_temp}<br>
  Low: {low_temp}<br>
  <br>
  Today's information<br>
  <br>
  Skies: {day_sky}.<br>
  Alerts: {alerts_text}<br>
  <br>
  Tonight's information<br>
  <br>
  Skies: {night_sky}.<br>
  Alerts: {alerts_text}<br>
  <br>
  </p>
</body>
</html>
"""

    # Weather history entry
    history_entry = f"""<p><strong>Today, {date_label}'s weather in lake oswego.</strong></p>
<p>
  Temperatures<br>
  <br>
  High: {high_temp}<br>
  Low: {low_temp}<br>
  <br>
  Today's information<br>
  <br>
  Skies: {day_sky}.<br>
  Alerts: {alerts_text}<br>
  <br>
  Tonight's information<br>
  <br>
  Skies: {night_sky}.<br>
  Alerts: {alerts_text}<br>
  <br>
  <br>
</p>
"""

    # Write today's weather page
    with open(TODAY_HTML_PATH, 'w', encoding='utf-8') as f:
        f.write(today_content)

    print(f"Updated: {TODAY_HTML_PATH}")

    # History configuration
    marker = "<!-- HISTORY TRACKING MARKER -->"

    base_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Weather History</title>
  <link rel="stylesheet" href="../style.css">
</head>
<body>
  <h1>Lake Oswego Weather History</h1>
  <div style="position: fixed; top: 10px; right: 10px; color: blue; text-decoration: none;">
    <a href="javascript:history.back()" style="color: blue; text-decoration: none;"><- Back</a>
  </div>
  {marker}
</body>
</html>"""

    # Read existing history
    history_content = ""

    if os.path.exists(HISTORY_HTML_PATH):
        with open(HISTORY_HTML_PATH, 'r', encoding='utf-8') as f:
            history_content = f.read()

    if "<h1>Lake Oswego Weather History</h1>" not in history_content:
        print("History file is missing or corrupted. Rebuilding base template...")
        history_content = base_template

    # Ensure marker exists
    if marker not in history_content:
        history_content = history_content.replace(
            "</body>",
            f"{marker}\n</body>"
        )

    # Separate header from history entries
    header, separator, entries = history_content.partition(marker)

    if not separator:
        print("ERROR: History marker could not be located.")
        return

    # Identify today's existing entry
    date_identifier = f"Today, {date_label}'s weather in lake oswego."

    if date_identifier in entries:
        print(f"Existing entry for {date_label} found. Overwriting...")

        # Replace today's entry without touching previous days
        pattern = (
            r'<p><strong>Today, '
            + re.escape(date_label)
            + r"'s weather in lake oswego\.</strong></p>"
            + r'\s*<p>.*?</p>'
        )

        entries, replacements = re.subn(
            pattern,
            lambda _: history_entry.strip(),
            entries,
            count=1,
            flags=re.DOTALL
        )

        if replacements == 0:
            print("ERROR: Could not replace existing history entry.")
            return

        print(f"Successfully overwrote {date_label}'s weather entry!")

    else:
        print(f"No entry for {date_label} found. Creating new entry...")

        # Add newest entry at the beginning of history
        entries = "\n" + history_entry + "\n" + entries

        print(f"Added new history entry for {date_label}!")

    # Reassemble history
    new_history = header + marker + entries

    with open(HISTORY_HTML_PATH, 'w', encoding='utf-8') as f:
        f.write(new_history)

    print(f"Updated: {HISTORY_HTML_PATH}")

    # Git automation
    if push_to_git:
        push_updates_to_github()
    else:
        print(
            "\nTEST MODE: Files built successfully on local disk. "
            "Git push was skipped."
        )


if __name__ == '__main__':
    build_static_html_files(push_to_git=True)
