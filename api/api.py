from flask import Flask, jsonify

app = Flask(__name__)

LAST_UPDATED = "July 31, 2026 at 09:00 PM PT"


@app.route('/api/temperature')
def temperature():
    return jsonify({
        "high": "76 degrees fahrenheit",
        "low": "60 degrees fahrenheit",
        "last_updated": LAST_UPDATED
    })


@app.route('/api/skies')
def skies():
    return jsonify({
        "skies": "Mostly Cloudy then Chance Light Rain"
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
        "high": "76 degrees fahrenheit",
        "low": "60 degrees fahrenheit",
        "skies": "Mostly Cloudy then Chance Light Rain",
        "last_updated": LAST_UPDATED
    })


@app.route('/api/observations')
def observations():
    return jsonify({
        "current": "76 degrees fahrenheit, Mostly Cloudy then Chance Light Rain",
        "last_updated": LAST_UPDATED
    })


# IMPORTANT FOR VERCEL
app = app
