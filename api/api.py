from flask import Flask, jsonify

app = Flask(__name__)

LAST_UPDATED = "October 30, 2026 at 09:30 AM PT"


@app.route('/api/temperature')
def temperature():
    return jsonify({
        "high": "54 degrees fahrenheit",
        "low": "38 degrees fahrenheit",
        "last_updated": LAST_UPDATED
    })


@app.route('/api/skies')
def skies():
    return jsonify({
        "skies": "Rain Showers Likely"
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
        "high": "54 degrees fahrenheit",
        "low": "38 degrees fahrenheit",
        "skies": "Rain Showers Likely",
        "last_updated": LAST_UPDATED
    })


@app.route('/api/observations')
def observations():
    return jsonify({
        "current": "54 degrees fahrenheit, Rain Showers Likely",
        "last_updated": LAST_UPDATED
    })


# IMPORTANT FOR VERCEL
app = app
