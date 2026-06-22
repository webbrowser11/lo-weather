from flask import Flask, jsonify

# chatgpt cleaned this up, also i am prolly going to add more endpoints and make it easier to maintain, as well as mabye automate and make the website use this api to get the forecast too, which will make everything a but eassier.

last_updated = "June 22nd, 2026 at 4:30 PM PDT"
temp_last_updated = "June 22nd, 2026 at 4:30 PM PDT"
observations_last_updated = "June 22nd, 2026 at 4:30 PM PDT"

app = Flask(__name__)

@app.route('/api/temperature')
def temperature():

    return jsonify({
        "temperature-high-lake-oswego": 92,
        "temperature-low-lake-oswego": 61,
        "temperature-last-updated-lake-oswego": temp_last_updated
    })

@app.route('/api/skies')
def skies():

    return jsonify({
        "skies-lake-oswego":
        "Sunny."
    })

@app.route('/api/alerts')
def alerts():

    return jsonify({
        "alerts-lake-oswego":
        "AN EXTREME HEAT ADVISORY IS IN EFFECT FROM JUNE 22, 11:00 AM PDT UNTIL JUNE 23, 11:00 PM PDT\nAN EXTREME DROUGHT WATCH CONTINUES FOR THE ENTIRE STATE OF OREGON."
    })

@app.route('/api/last-updated')
def last_updated():
    return jsonify({
        "last-updated-lake-oswego": last_updated
    })

@app.route('/api/observations')
def observations():
    return jsonify({
        "observations-lake-oswego": "90 degrees Fahrenheit, Sunny.",
        "last-updated-observations-lake-oswego": observations_last_updated
    })

@app.route('/api/events')
def events():
    return jsonify({
        "events-lake-oswego": "No special events D:"
    })

# IMPORTANT FOR VERCEL
app = app
