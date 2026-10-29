from flask import Flask, jsonify

app = Flask(__name__)

LAST_UPDATED = "October 29, 2026 at 08:45 AM PT"


@app.route('/api/temperature')
def temperature():
    return jsonify({
        "high": "55 degrees fahrenheit",
        "low": "40 degrees fahrenheit",
        "last_updated": LAST_UPDATED
    })


@app.route('/api/skies')
def skies():
    return jsonify({
        "skies": "Chance Rain Showers"
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
        "high": "55 degrees fahrenheit",
        "low": "40 degrees fahrenheit",
        "skies": "Chance Rain Showers",
        "last_updated": LAST_UPDATED
    })


@app.route('/api/observations')
def observations():
    return jsonify({
        "current": "55 degrees fahrenheit, Chance Rain Showers",
        "last_updated": LAST_UPDATED
    })


# IMPORTANT FOR VERCEL
app = app
