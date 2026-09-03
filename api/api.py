from flask import Flask, jsonify

app = Flask(__name__)

LAST_UPDATED = "September 03, 2026 at 03:15 PM PT"


@app.route('/api/temperature')
def temperature():
    return jsonify({
        "high": "64 degrees fahrenheit",
        "low": "54 degrees fahrenheit",
        "last_updated": LAST_UPDATED
    })


@app.route('/api/skies')
def skies():
    return jsonify({
        "skies": "Showers And Thunderstorms Likely"
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
        "high": "64 degrees fahrenheit",
        "low": "54 degrees fahrenheit",
        "skies": "Showers And Thunderstorms Likely",
        "last_updated": LAST_UPDATED
    })


@app.route('/api/observations')
def observations():
    return jsonify({
        "current": "64 degrees fahrenheit, Showers And Thunderstorms Likely",
        "last_updated": LAST_UPDATED
    })


# IMPORTANT FOR VERCEL
app = app
