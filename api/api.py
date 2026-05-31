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
        "last-updated-lake-oswego": "May 31st, 2026 at 2:35 PM PT"
    })

@app.route('/api/observations')
def observations():
    return jsonify({
        "observations-lake-oswego": "My current observations for lake oswego is that it is currently about 70 degrees fahrenheit, and it feels like 73.\nThe skies are currently clear, and it's a nice day to go outside!\nI really do have to mention the heat though.\n It is very hot, so stay hyrated. Also, remember the sun is very strong!\n Don't forget to wear at least SPF 50 sunscreen if you are goin outside for long periods of time.",
        "last-updated-observations-lake-oswego": "May 31st, 2026 at 2:35 PM PT"
    })

@app.route('/api/events')
def events():
    return jsonify({
        "events-lake-oswego": "There are no current special events sorry D:"
    })

# IMPORTANT FOR VERCEL
app = app