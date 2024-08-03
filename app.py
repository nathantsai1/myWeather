import requests
from flask import Flask, jsonify, request, render_template

from helpers import (weather)
# my first time using an api
app = Flask(__name__)
# API key and base URL for OpenWeather API
# api_key = 'd0d0e6975b6a6865318ca1e63051a638'
# thx to chatGPT for helping me with learning how to retrieve information from APIs
base_url = 'http://api.openweathermap.org/data/2.5/weather'

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')


@app.route('/weather', methods=['POST', 'GET'])
def get_weather():
    # Get the city name from query parameters, default to 'London' if not provided
    if request.method == "POST":
        api_key = 'd0d0e6975b6a6865318ca1e63051a638'
        # Construct the complete API URL
        # complete_url = f"{base_url}?q={city_name}&appid={api_key}"

        # Send the request to OpenWeather API
        response = weather(request.form.get('city'), api_key)
        if response == 'no':
            return render_template('weather.html', alert=request.form.get('city'))
        # Check if the request was successful
        if response.status_code == 200:
            # Parse JSON data
            data = response.json()
            

            main = data['main']
            # weather = data['weather'][0]
            
            return render_template('weather.html', row=data)
    else:
        return render_template('weather.html')

if __name__ == '__main__':
    app.run(debug=True)