from flask import Flask, jsonify

app = Flask(__name__)

LAST_UPDATED = "October 24, 2026 at 07:45 AM PT"


@app.route('/api/temperature')
def temperature():
    return jsonify({
        "high": "63 degrees fahrenheit",
        "low": "41 degrees fahrenheit",
        "last_updated": LAST_UPDATED
    })


@app.route('/api/skies')
def skies():
    return jsonify({
        "skies": "Patchy Fog then Partly Sunny"
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
        "high": "63 degrees fahrenheit",
        "low": "41 degrees fahrenheit",
        "skies": "Patchy Fog then Partly Sunny",
        "last_updated": LAST_UPDATED
    })


@app.route('/api/observations')
def observations():
    return jsonify({
        "current": "63 degrees fahrenheit, Patchy Fog then Partly Sunny",
        "last_updated": LAST_UPDATED
    })


# IMPORTANT FOR VERCEL
app = app
