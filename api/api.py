from flask import Flask, jsonify

app = Flask(__name__)
last_updated = "July 06, 2026 at 09:30 PM PT"

@app.route('/api/temperature')
def temperature():
    return jsonify({"high": "84 degrees fahrenheit", "low": "58 degrees fahrenheit", "last_updated": last_updated})

@app.route('/api/skies')
def skies():
    return jsonify({"skies": "Mostly Sunny"})

@app.route('/api/last-updated')
def last_updated():
    return jsonify({"last_updated": last_updated})

@app.route('/api/observations')
def observations():
    return jsonify({"current": "84 degrees fahrenheit degrees, Mostly Sunny", "last_updated": last_updated})

# IMPORTANT FOR VERCEL
app = app
