from flask import Flask, jsonify

# chatgpt cleaned this up, also i am prolly going to add more endpoints and make it easier to maintain, as well as mabye automate and make the website use this api to get the forecast too, which will make everything a but eassier.

app = Flask(__name__)

@app.route('/api/temperature')
def temperature():

    return jsonify({
        "temperature-high-lake-oswego": 67,
        "temperature-low-lake-oswego": 45
    })

@app.route('/api/skies')
def skies():

    return jsonify({
        "skies-lake-oswego":
        "Cloudy and rainy starting 8am and then clearing up around 3pm then partly cloudy skies from 8pm until the end of the day."
    })

@app.route('/api/warnings-advisories')
def warnings():

    return jsonify({
        "warnings-advisories-lake-oswego":
        "There are no current warnings or advisories :D"
    })

# IMPORTANT FOR VERCEL
app = app