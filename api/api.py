from flask import Flask, jsonify

# chatgpt cleaned this up, also i am prolly going to add more endpoints and make it easier to maintain, as well as mabye automate and make the website use this api to get the forecast too, which will make everything a but eassier.

app = Flask(__name__)

@app.route('/api/temperature')
def temperature():

    return jsonify({
        "temperature-high-lake-oswego": 70,
        "temperature-low-lake-oswego": 48
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
        "last-updated-lake-oswego": "June 1st, 2026 at 6:05 PM PT"
    })

@app.route('/api/observations')
def observations():
    return jsonify({
        "observations-lake-oswego": "82 degrees Fahrenheit, Increasing clouds.",
        "last-updated-observations-lake-oswego": "June 1st, 2026 at 6:05PM PT"
    })

@app.route('/api/events')
def events():
    return jsonify({
        "events-lake-oswego": "There are no current special events sorry D:"
    })

# IMPORTANT FOR VERCEL
app = app