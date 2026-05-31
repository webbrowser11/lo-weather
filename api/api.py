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
        "last-updated-lake-oswego": "May 30th, 2026 at 7:00 PM PT"
    })

@app.route('/api/observations')
def observations():
    return jsonify({
        "observations-lake-oswego": "Currently my observations are that it is 65 degrees but feels like 66.\n And is mostly clear.\n"
        "The high is was 70 degrees, and the low is probably accurate for today.\n Currently, the sun is begging to set, and tonight should be a good sunset!\n"
        "There are some clouds in the sky, but they are not very dark. No rain should occur. This will add to the sunset.\n"
    })

# IMPORTANT FOR VERCEL
app = app