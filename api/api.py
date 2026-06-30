from flask import Flask, jsonify

app = Flask(__name__)
last_updated = "June 30, 2026 at 04:15 PM PT"

@app.route('/api/temperature')
def temperature():
    return jsonify({"high": "69 degrees fahrenheit", "low": "51 degrees fahrenheit", "last_updated": last_updated})

@app.route('/api/skies')
def skies():
    return jsonify({"skies": "Partly Sunny"})

@app.route('/api/last-updated')
def last_updated():
    return jsonify({"last_updated": last_updated})

@app.route('/api/observations')
def observations():
    return jsonify({"current": "69 degrees fahrenheit degrees, Partly Sunny", "last_updated": last_updated})

# IMPORTANT FOR VERCEL
app = app
