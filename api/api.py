from flask import Flask, jsonify

app = Flask(__name__)

LAST_UPDATED = "October 27, 2026 at 12:00 AM PT"


@app.route('/api/temperature')
def temperature():
    return jsonify({
        "high": "59 degrees fahrenheit",
        "low": "47 degrees fahrenheit",
        "last_updated": LAST_UPDATED
    })


@app.route('/api/skies')
def skies():
    return jsonify({
        "skies": "Light Rain"
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
        "high": "59 degrees fahrenheit",
        "low": "47 degrees fahrenheit",
        "skies": "Light Rain",
        "last_updated": LAST_UPDATED
    })


@app.route('/api/observations')
def observations():
    return jsonify({
        "current": "59 degrees fahrenheit, Light Rain",
        "last_updated": LAST_UPDATED
    })


# IMPORTANT FOR VERCEL
app = app
