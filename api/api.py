from flask import Flask, jsonify

app = Flask(__name__)
last_updated = "July 02, 2026 at 08:45 AM PT"

@app.route('/api/temperature')
def temperature():
    return jsonify({"high": "75 degrees fahrenheit", "low": "56 degrees fahrenheit", "last_updated": last_updated})

@app.route('/api/skies')
def skies():
    return jsonify({"skies": "Partly Sunny"})

@app.route('/api/last-updated')
def last_updated():
    return jsonify({"last_updated": last_updated})

@app.route('/api/observations')
def observations():
    return jsonify({"current": "75 degrees fahrenheit degrees, Partly Sunny", "last_updated": last_updated})

# IMPORTANT FOR VERCEL
app = app
