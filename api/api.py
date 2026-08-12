from flask import Flask, jsonify

app = Flask(__name__)

LAST_UPDATED = "August 11, 2026 at 07:30 PM PT"


@app.route('/api/temperature')
def temperature():
    return jsonify({
        "high": "79 degrees fahrenheit",
        "low": "60 degrees fahrenheit",
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
        "high": "79 degrees fahrenheit",
        "low": "60 degrees fahrenheit",
        "skies": "Partly Sunny",
        "last_updated": LAST_UPDATED
    })


@app.route('/api/observations')
def observations():
    return jsonify({
        "current": "79 degrees fahrenheit, Partly Sunny",
        "last_updated": LAST_UPDATED
    })


# IMPORTANT FOR VERCEL
app = app
