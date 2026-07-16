from flask import Flask, jsonify

app = Flask(__name__)

LAST_UPDATED = "July 15, 2026 at 09:30 PM PT"


@app.route('/api/temperature')
def temperature():
    return jsonify({
        "high": "79 degrees fahrenheit",
        "low": "59 degrees fahrenheit",
        "last_updated": LAST_UPDATED
    })


@app.route('/api/skies')
def skies():
    return jsonify({
        "skies": "Chance Showers And Thunderstorms then Partly Sunny"
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
        "low": "59 degrees fahrenheit",
        "skies": "Chance Showers And Thunderstorms then Partly Sunny",
        "last_updated": LAST_UPDATED
    })


# Current observations are handled separately
@app.route('/api/observations')
def observations():
    return jsonify({
        "message": "Current observations are on the observations page.",
        "last_updated": LAST_UPDATED
    })


# IMPORTANT FOR VERCEL
app = app
