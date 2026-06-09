from flask import Flask, jsonify

# chatgpt cleaned this up, also i am prolly going to add more endpoints and make it easier to maintain, as well as mabye automate and make the website use this api to get the forecast too, which will make everything a but eassier.

last_updated = "June 8th, 2026 at 6:00 PM PT"
temp_last_updated = "June 8th, 2026 at 6:00 PM PT"
observations_last_updated = "June 6th, 2026 at 2:45PM PT"

app = Flask(__name__)

@app.route('/api/temperature')
def temperature():

    return jsonify({
        "temperature-high-lake-oswego": 62,
        "temperature-low-lake-oswego": 52,
        "temperature-last-updated-lake-oswego": temp_last_updated
    })

@app.route('/api/skies')
def skies():

    return jsonify({
        "skies-lake-oswego":
        "Cloudy. Showers expected."
    })

@app.route('/api/alerts')
def alerts():

    return jsonify({
        "alerts-lake-oswego":
        "Abnormally dry conditions have been reported by the National Weather Service."
    })

@app.route('/api/last-updated')
def last_updated():
    return jsonify({
        "last-updated-lake-oswego": last_updated
    })

@app.route('/api/observations')
def observations():
    return jsonify({
        "observations-lake-oswego": "61 degrees Fahrenheit, Cloudy.",
        "last-updated-observations-lake-oswego": observations_last_updated
    })

@app.route('/api/events')
def events():
    return jsonify({
        "events-lake-oswego": "No special events D:"
    })

# IMPORTANT FOR VERCEL
app = app