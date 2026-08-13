from flask import Flask, jsonify

app = Flask(__name__)

LAST_UPDATED = "August 13, 2026 at 10:45 AM PT"


@app.route('/api/temperature')
def temperature():
    return jsonify({
        "high": "85 degrees fahrenheit",
        "low": "60 degrees fahrenheit",
        "last_updated": LAST_UPDATED
    })


@app.route('/api/skies')
def skies():
    return jsonify({
        "skies": "Sunny then Areas Of Smoke"
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
        "high": "85 degrees fahrenheit",
        "low": "60 degrees fahrenheit",
        "skies": "Sunny then Areas Of Smoke",
        "last_updated": LAST_UPDATED
    })


@app.route('/api/observations')
def observations():
    return jsonify({
        "current": "85 degrees fahrenheit, Sunny then Areas Of Smoke",
        "last_updated": LAST_UPDATED
    })


# IMPORTANT FOR VERCEL
app = app
