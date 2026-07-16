from flask import Flask, jsonify

app = Flask(__name__)

LAST_UPDATED = "July 16, 2026 at 02:00 PM PT"


@app.route('/api/temperature')
def temperature():
    return jsonify({
        "high": "77 degrees fahrenheit",
        "low": "55 degrees fahrenheit",
        "last_updated": LAST_UPDATED
    })


@app.route('/api/skies')
def skies():
    return jsonify({
        "skies": "Partly Sunny"
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
        "high": "77 degrees fahrenheit",
        "low": "55 degrees fahrenheit",
        "skies": "Partly Sunny",
        "last_updated": LAST_UPDATED
    })


@app.route('/api/observations')
def observations():
    return jsonify({
        "current": "77 degrees fahrenheit, Partly Sunny",
        "last_updated": LAST_UPDATED
    })


# IMPORTANT FOR VERCEL
app = app
