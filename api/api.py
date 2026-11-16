from flask import Flask, jsonify

app = Flask(__name__)

LAST_UPDATED = "November 16, 2026 at 11:30 AM PT"


@app.route('/api/temperature')
def temperature():
    return jsonify({
        "high": "53 degrees fahrenheit",
        "low": "40 degrees fahrenheit",
        "last_updated": LAST_UPDATED
    })


@app.route('/api/skies')
def skies():
    return jsonify({
        "skies": "Mostly Sunny then Chance Rain Showers"
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
        "high": "53 degrees fahrenheit",
        "low": "40 degrees fahrenheit",
        "skies": "Mostly Sunny then Chance Rain Showers",
        "last_updated": LAST_UPDATED
    })


@app.route('/api/observations')
def observations():
    return jsonify({
        "current": "53 degrees fahrenheit, Mostly Sunny then Chance Rain Showers",
        "last_updated": LAST_UPDATED
    })


# IMPORTANT FOR VERCEL
app = app
