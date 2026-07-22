from flask import Flask, jsonify

app = Flask(__name__)

LAST_UPDATED = "July 21, 2026 at 08:00 PM PT"


@app.route('/api/temperature')
def temperature():
    return jsonify({
        "high": "101 degrees fahrenheit",
        "low": "70 degrees fahrenheit",
        "last_updated": LAST_UPDATED
    })


@app.route('/api/skies')
def skies():
    return jsonify({
        "skies": "Patchy Smoke then Chance Showers And Thunderstorms"
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
        "high": "101 degrees fahrenheit",
        "low": "70 degrees fahrenheit",
        "skies": "Patchy Smoke then Chance Showers And Thunderstorms",
        "last_updated": LAST_UPDATED
    })


@app.route('/api/observations')
def observations():
    return jsonify({
        "current": "101 degrees fahrenheit, Patchy Smoke then Chance Showers And Thunderstorms",
        "last_updated": LAST_UPDATED
    })


# IMPORTANT FOR VERCEL
app = app
