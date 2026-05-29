from flask import Flask, jsonify

# chatgpt cleaned this up, also i am prolly going to add more endpoints and make it easier to maintain, as well as mabye automate and make the website use this api to get the forecast too, which will make everything a but eassier.

app = Flask(__name__)
app.config["JSONIFY_PRETTYPRINT_REGULAR"] = True

@app.route('/api/temperature')
def temperature():

    return jsonify({
        "temperature-high-lake-oswego": 80,
        "temperature-low-lake-oswego": 54
    })

@app.route('/api/skies')
def skies():

    return jsonify({
        "skies-lake-oswego":
        "cloudy until 4pm, then mostly cloudy with a chance of rain before 1am."
    })

@app.route('/api/warnings-advisories')
def warnings():

    return jsonify({
        "warnings-advisories-lake-oswego":
        "There are no current warnings or advisories :D"
    })

# IMPORTANT FOR VERCEL
app = app
