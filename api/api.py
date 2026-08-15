from flask import Flask, jsonify

app = Flask(__name__)

LAST_UPDATED = "August 15, 2026 at 09:45 AM PT"


@app.route('/api/temperature')
def temperature():
    return jsonify({
        "high": "82 degrees fahrenheit",
        "low": "59 degrees fahrenheit",
        "last_updated": LAST_UPDATED
    })


@app.route('/api/skies')
def skies():
    return jsonify({
        "skies": "Slight Chance Showers And Thunderstorms"
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
        "high": "82 degrees fahrenheit",
        "low": "59 degrees fahrenheit",
        "skies": "Slight Chance Showers And Thunderstorms",
        "last_updated": LAST_UPDATED
    })


@app.route('/api/observations')
def observations():
    return jsonify({
        "current": "82 degrees fahrenheit, Slight Chance Showers And Thunderstorms",
        "last_updated": LAST_UPDATED
    })


# IMPORTANT FOR VERCEL
app = app
