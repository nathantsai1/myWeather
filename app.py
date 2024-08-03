import requests
from flask import Flask, jsonify, request, render_template

from helpers import (
    weather,
    location
    )

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
        # check paramaters
        if not request.form.get("city") or request.form.get("city").strip() == "":
            # give alert that declares that there is no city inputted
            return render_template('weather.html', empty='empty')
        
        # Construct the complete API URL

        # use maps.co to geocode the location
        api = '66aea33917c5a663090428mokbd8a48'
        response = location(request.form.get('city'), api)
        # data = response.json()
        # return jsonify(
        #     data
        # )
        # jsonify response
        data = response.json()

        # if there is no location
        if data == []:
            return render_template('weather.html', alert=request.form.get('city'))
        # give out all responses
        # get number of responses
        length = sum(1 for i in data if isinstance(i, dict))
        if length > 1:
            # if there are multiple places, ask for which one to use
            return render_template("loop.html", length=length, data=data)
        return render_template('useless.html', row=data)
        # ask which one
        

        # Send the request to OpenWeather API
        api_key = 'd0d0e6975b6a6865318ca1e63051a638'
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