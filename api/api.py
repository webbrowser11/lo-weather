from flask import Flask, jsonify

# chatgpt cleaned this up, also i am prolly going to add more endpoints and make it easier to maintain, as well as mabye automate and make the website use this api to get the forecast too, which will make everything a but eassier.

last_updated = "June 5th, 2026 at 4:00PM PT"
temp_last_updated = "June 5th, 2026 at 4:00PM PT"
observations_last_updated = "June 5th, 2026 at 4:00PM PT"

app = Flask(__name__)

@app.route('/api/temperature')
def temperature():

    return jsonify({
        "temperature-high-lake-oswego": 65,
        "temperature-low-lake-oswego": 47,
        "temperature-last-updated-lake-oswego": temp_last_updated
    })

@app.route('/api/skies')
def skies():

    return jsonify({
        "skies-lake-oswego":
        "Partly cloudy all day until late this afternoon when cloud cover will being to decrease. Clear or mostly clear with chilly weather all night."
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
        "observations-lake-oswego": "68 degrees Fahrenheit, sunny.",
        "last-updated-observations-lake-oswego": observations_last_updated
    })

@app.route('/api/events')
def events():
    return jsonify({
        "events-lake-oswego": "Tonight the auroras are supposed to be very good! Check them out!"
    })

# IMPORTANT FOR VERCEL
app = app