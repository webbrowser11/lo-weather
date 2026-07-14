from flask import Flask, jsonify

app = Flask(__name__)

LAST_UPDATED = "July 14, 2026 at 02:00 PM PT"

@app.route('/api/temperature')
def temperature():
    return jsonify({
        "high": "91 degrees fahrenheit",
        "low": "60 degrees fahrenheit",
        "last_updated": LAST_UPDATED
    })

@app.route('/api/skies')
def skies():
    return jsonify({
        "skies": "Sunny"
    })

@app.route('/api/last-updated')
def get_last_updated():
    return jsonify({
        "last_updated": LAST_UPDATED
    })

@app.route('/api/observations')
def observations():
    return jsonify({
        "current": "91 degrees fahrenheit, Sunny",
        "last_updated": LAST_UPDATED
    })

# IMPORTANT FOR VERCEL
app = app
