from flask import Flask, jsonify

app = Flask(__name__)

LAST_UPDATED = "August 02, 2026 at 10:00 PM PT"


@app.route('/api/temperature')
def temperature():
    return jsonify({
        "high": "88 degrees fahrenheit",
        "low": "54 degrees fahrenheit",
        "last_updated": LAST_UPDATED
    })


@app.route('/api/skies')
def skies():
    return jsonify({
        "skies": "Smoke"
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
        "high": "88 degrees fahrenheit",
        "low": "54 degrees fahrenheit",
        "skies": "Smoke",
        "last_updated": LAST_UPDATED
    })


@app.route('/api/observations')
def observations():
    return jsonify({
        "current": "88 degrees fahrenheit, Smoke",
        "last_updated": LAST_UPDATED
    })


# IMPORTANT FOR VERCEL
app = app
