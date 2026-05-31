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
        "Partly cloudy all day until late this afternoon, with decreasing cloud cover. Clear with chilly weather all night."
    })

@app.route('/api/alerts')
def alerts():

    return jsonify({
        "alerts-lake-oswego":
        "There are no current alerts :D"
    })

@app.route('/api/last-updated')
def last_updated():
    return jsonify({
        "last-updated-lake-oswego": "May 30th, 2026 at 6:44 PM PT"
    })

@app.route('/api/observations')
def observations():
    return jsonify({
        "observations-lake-oswego": "Currently my observations are that it is 68 degrees but feels like 65.\n And is partly cloudy, with decreasing cloud cover.\n"
        "The high is higher than I originally predicted, and the low has also gone up with it."
    })

# IMPORTANT FOR VERCEL
app = app