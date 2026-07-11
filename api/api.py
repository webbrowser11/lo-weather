from flask import Flask, jsonify

app = Flask(__name__)

LAST_UPDATED = "July 10, 2026 at 09:30 PM PT"

@app.route('/api/temperature')
def temperature():
    return jsonify({
        "high": "80 degrees fahrenheit",
        "low": "57 degrees fahrenheit",
        "last_updated": LAST_UPDATED
    })

@app.route('/api/skies')
def skies():
    return jsonify({
        "skies": "Partly Sunny"
    })

@app.route('/api/last-updated')
def get_last_updated():
    return jsonify({
        "last_updated": LAST_UPDATED
    })

@app.route('/api/observations')
def observations():
    return jsonify({
        "current": "80 degrees fahrenheit, Partly Sunny",
        "last_updated": LAST_UPDATED
    })

# IMPORTANT FOR VERCEL
app = app
