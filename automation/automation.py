import os
import datetime
import subprocess
import requests
import nws_api_fetch  # Lives in the same 'automation' folder

# Locate the 'automation' folder where this script runs
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Go up one level to the root, then into the 'site' folder
TODAY_HTML_PATH = os.path.abspath(os.path.join(BASE_DIR, '..', 'site', 'todays-weather.html'))
HISTORY_HTML_PATH = os.path.abspath(os.path.join(BASE_DIR, '..', 'site', 'weather-history.html'))
REPO_ROOT = os.path.abspath(os.path.join(BASE_DIR, '..'))

def fetch_all_current_data():
    """Pulls forecast data from your fetcher and grabs live alerts."""
    try:
        data = nws_api_fetch.fetch_weather_data()
        
        headers = {"User-Agent": "lo-weather/1.0 (terpstragraham@gmail.com)"}
        alert_res = requests.get('https://api.weather.gov/alerts/active/zone/ORZ006', headers=headers)
        alert_data = alert_res.json()
        features = alert_data.get('features', [])
        
        if features:
            data['alerts'] = " | ".join([f['properties']['headline'] for f in features])
        else:
            data['alerts'] = "No active watches, warnings, or advisories at this time."
            
        return data
    except Exception as e:
        print(f"Error compiling live metrics: {e}")
        return None

def get_ordinal_date_string():
    # FIXED: Now uses exactly today's date!
    today = datetime.date.today()
    day = today.day
    if 11 <= day <= 13:
        suffix = 'th'
    else:
        suffix = {1: 'st', 2: 'nd', 3: 'rd'}.get(day % 10, 'th')
    return today.strftime(f"%B {day}{suffix}")

def push_updates_to_github():
    """Switches to the repository root and pushes the updated HTML pages to GitHub."""
    try:
        os.chdir(REPO_ROOT)
        subprocess.run(["git", "add", TODAY_HTML_PATH, HISTORY_HTML_PATH], check=True)
        
        status = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True)
        if status.stdout.strip():
            commit_msg = f"Automated history update: Logged weather for {get_ordinal_date_string()}"
            subprocess.run(["git", "commit", "-m", commit_msg], check=True)
            subprocess.run(["git", "push"], check=True)
            print("Successfully pushed daily updates to GitHub! Vercel is now redeploying.")
        else:
            print("No data changes detected. Skipping Git push.")
    except subprocess.CalledProcessError as e:
        print(f"Git automation error: {e}")

def build_static_html_files(push_to_git=True):
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

    today_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Today's Weather</title>
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

    history_entry = f"""  <p><strong>Today, {date_label}'s weather in lake oswego.</strong></p>
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

    # 1. Write the static file to site/todays-weather.html
    with open(TODAY_HTML_PATH, 'w', encoding='utf-8') as f:
        f.write(today_content)
    print(f"Updated: {TODAY_HTML_PATH}")

    # 2. Append to site/weather-history.html
    marker = "<!-- HISTORY TRACKING MARKER -->"
    base_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Weather History</title>
</head>
<body>
  <h1>Lake Oswego Weather History</h1>
  <div style="position: fixed; top: 10px; right: 10px; color: blue; text-decoration: none;">
    <a href="javascript:history.back()" style="color: blue; text-decoration: none;"><- Back</a>
  </div>
  {marker}
</body>
</html>"""

    history_content = ""
    if os.path.exists(HISTORY_HTML_PATH):
        with open(HISTORY_HTML_PATH, 'r', encoding='utf-8') as f:
            history_content = f.read()
    
    if "<h1>Lake Oswego Weather History</h1>" not in history_content:
        print("History file is missing or corrupted. Rebuilding base template...")
        history_content = base_template

    if marker in history_content:
        new_history = history_content.replace(marker, f"{marker}\n{history_entry}")
        with open(HISTORY_HTML_PATH, 'w', encoding='utf-8') as f:
            f.write(new_history)
        print(f"Appended history tracking entry for {date_label}!")
    else:
        new_history = history_content.replace("</body>", f"{marker}\n{history_entry}\n</body>")
        with open(HISTORY_HTML_PATH, 'w', encoding='utf-8') as f:
            f.write(new_history)
        print(f"Fixed marker and appended history tracking entry for {date_label}!")

    # 3. Handle Git Push
    if push_to_git:
        push_updates_to_github()
    else:
        print("\n✅ TEST MODE: Files built successfully on local disk. Git push was skipped.")

if __name__ == '__main__':
    build_static_html_files(push_to_git=True)