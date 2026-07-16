import os
import datetime
import subprocess
from zoneinfo import ZoneInfo
import nws_api_fetch

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
API_FILE_PATH = os.path.abspath(os.path.join(BASE_DIR, '..', 'api', 'api.py'))
REPO_ROOT = os.path.abspath(os.path.join(BASE_DIR, '..'))


def clean_text(value):
    """Prevent generated Python file from breaking."""
    if value is None:
        return "N/A"

    return str(value).replace('"', '\\"')


def refresh_api(push_to_git=True):
    print("Fetching live data for API refresh...")

    data = nws_api_fetch.fetch_weather_data()

    if not data:
        print("API Build cancelled: Could not reach NWS.")
        return

    # Pacific time timestamp
    timestamp = datetime.datetime.now(
        ZoneInfo("America/Los_Angeles")
    ).strftime("%B %d, %Y at %I:%M %p PT")

    # Forecast data
    high = clean_text(data.get("forecast-high", "N/A"))
    low = clean_text(data.get("forecast-low", "N/A"))
    day_sky = clean_text(data.get("forecast-day-sky", "Clear"))

    api_content = f'''from flask import Flask, jsonify

app = Flask(__name__)

LAST_UPDATED = "{timestamp}"


@app.route('/api/temperature')
def temperature():
    return jsonify({{
        "high": "{high}",
        "low": "{low}",
        "last_updated": LAST_UPDATED
    }})


@app.route('/api/skies')
def skies():
    return jsonify({{
        "skies": "{day_sky}"
    }})


@app.route('/api/last-updated')
def get_last_updated():
    return jsonify({{
        "last_updated": LAST_UPDATED
    }})


# Forecast summary only
@app.route('/api/forecast')
def forecast():
    return jsonify({{
        "high": "{high}",
        "low": "{low}",
        "skies": "{day_sky}",
        "last_updated": LAST_UPDATED
    }})


# Current observations are handled separately
@app.route('/api/observations')
def observations():
    return jsonify({{
        "message": "Current observations are on the observations page.",
        "last_updated": LAST_UPDATED
    }})


# IMPORTANT FOR VERCEL
app = app
'''

    os.makedirs(os.path.dirname(API_FILE_PATH), exist_ok=True)

    with open(API_FILE_PATH, "w", encoding="utf-8") as f:
        f.write(api_content)

    print(f"API file updated at {timestamp}")

    if push_to_git:
        try:
            os.chdir(REPO_ROOT)

            subprocess.run(
                ["git", "add", "api/api.py"],
                check=True
            )

            status = subprocess.run(
                ["git", "status", "--porcelain"],
                capture_output=True,
                text=True
            )

            if status.stdout.strip():
                subprocess.run(
                    ["git", "commit", "-m", "Automated API update"],
                    check=True
                )

                subprocess.run(
                    ["git", "push"],
                    check=True
                )

                print("API changes pushed to GitHub.")
            else:
                print("No changes to commit.")

        except Exception as e:
            print(f"Git push failed: {e}")


if __name__ == "__main__":
    refresh_api(push_to_git=True)