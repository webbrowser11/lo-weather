from flask import Flask, jsonify

app = Flask(__name__)

LAST_UPDATED = "November 03, 2026 at 08:15 PM PT"


@app.route('/api/temperature')
def temperature():
    return jsonify({
        "high": "59 degrees fahrenheit",
        "low": "41 degrees fahrenheit",
        "last_updated": LAST_UPDATED
    })


@app.route('/api/skies')
def skies():
    return jsonify({
        "skies": "Patchy Fog then Chance Light Rain"
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
        "low": "41 degrees fahrenheit",
        "skies": "Patchy Fog then Chance Light Rain",
        "last_updated": LAST_UPDATED
    })


@app.route('/api/observations')
def observations():
    return jsonify({
        "current": "59 degrees fahrenheit, Patchy Fog then Chance Light Rain",
        "last_updated": LAST_UPDATED
    })


# IMPORTANT FOR VERCEL
app = app
