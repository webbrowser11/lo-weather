from flask import Flask, jsonify

app = Flask(__name__)

LAST_UPDATED = "November 23, 2026 at 09:00 AM PT"


@app.route('/api/temperature')
def temperature():
    return jsonify({
        "high": "48 degrees fahrenheit",
        "low": "43 degrees fahrenheit",
        "last_updated": LAST_UPDATED
    })


@app.route('/api/skies')
def skies():
    return jsonify({
        "skies": "Cloudy then Chance Light Rain"
    })


@app.route('/api/last-updated')
def get_last_updated():
    return jsonify({
        "last_updated": LAST_UPDATED
    })


# Forecast summary only
@app.route('/api/forecast')
def forecast():
    return jsonify({
        "high": "48 degrees fahrenheit",
        "low": "43 degrees fahrenheit",
        "skies": "Cloudy then Chance Light Rain",
        "last_updated": LAST_UPDATED
    })


@app.route('/api/observations')
def observations():
    return jsonify({
        "current": "48 degrees fahrenheit, Cloudy then Chance Light Rain",
        "last_updated": LAST_UPDATED
    })


# IMPORTANT FOR VERCEL
app = app
