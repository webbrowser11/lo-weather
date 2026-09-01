from flask import Flask, jsonify

app = Flask(__name__)

LAST_UPDATED = "September 01, 2026 at 03:30 PM PT"


@app.route('/api/temperature')
def temperature():
    return jsonify({
        "high": "74 degrees fahrenheit",
        "low": "59 degrees fahrenheit",
        "last_updated": LAST_UPDATED
    })


@app.route('/api/skies')
def skies():
    return jsonify({
        "skies": "Slight Chance Drizzle"
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
        "high": "74 degrees fahrenheit",
        "low": "59 degrees fahrenheit",
        "skies": "Slight Chance Drizzle",
        "last_updated": LAST_UPDATED
    })


@app.route('/api/observations')
def observations():
    return jsonify({
        "current": "74 degrees fahrenheit, Slight Chance Drizzle",
        "last_updated": LAST_UPDATED
    })


# IMPORTANT FOR VERCEL
app = app
