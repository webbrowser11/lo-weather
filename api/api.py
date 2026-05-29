# api for the weather website
import json
from flask import Flask, jsonify, request

app = Flask(__name__)

# these are to be updated everyday, at some point i wish to automate this process.

@app.route('/api/temperature', methods=['GET'])
def get_temperature():
    todays_temperature_data = {
        'temperature-high-lake-oswego': 80,
        'temperature-low-lake-oswego': 54
    }
    return jsonify(todays_temperature_data)

@app.route('/api/skies', methods=['POST'])
def get_skies():
    todays_skies_data = {
        'skies-lake-oswego': 'cloudy until 4pm, then mostly cloudy with a chance of rain before 1am.'
    }
    return jsonify(todays_skies_data)

@app.route('/api/warnings-advisories', methods=['GET'])
def get_warnings_advisories():
    todays_warnings_advisories_data = {
        'warnings-advisories-lake-oswego': 'There are no current warnings or advisories :D'
    }
    return jsonify(todays_warnings_advisories_data)