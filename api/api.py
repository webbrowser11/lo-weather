from flask import Flask, jsonify

app = Flask(__name__)

LAST_UPDATED = "November 05, 2026 at 08:45 PM PT"


@app.route('/api/temperature')
def temperature():
    return jsonify({
        "high": "61 degrees fahrenheit",
        "low": "44 degrees fahrenheit",
        "last_updated": LAST_UPDATED
    })


@app.route('/api/skies')
def skies():
    return jsonify({
        "skies": "Light Rain Likely"
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
        "high": "61 degrees fahrenheit",
        "low": "44 degrees fahrenheit",
        "skies": "Light Rain Likely",
        "last_updated": LAST_UPDATED
    })


@app.route('/api/observations')
def observations():
    return jsonify({
        "current": "61 degrees fahrenheit, Light Rain Likely",
        "last_updated": LAST_UPDATED
    })


# IMPORTANT FOR VERCEL
app = app
