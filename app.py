import requests
from flask import (
    Flask, 
    request, 
    render_template, 
    abort,
    redirect,
    jsonify
    )
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

api_key = 'd0d0e6975b6a6865318ca1e63051a638'
@app.route('/weather', methods=['POST', 'GET'])
def get_weather():
    # Get the city name from query parameters, default to 'London' if not provided
    if request.method == "POST":
        # check paramaters
        if not request.form.get("city") or request.form.get("city").strip() == "":
            # give alert that declares that there is no city inputted
            return render_template('weather.html', empty='empty')
        
        # Construct the complete API URL

        # use openweathermap to geocode the location
        response = location(request.form.get('city'), api_key)
       
        # if there is no location
        if response == "no":
            return render_template('weather.html', alert=request.form.get('city'))
        data = response.json()
        # give out all responses
        # get number of responses
        length = sum(1 for i in data if isinstance(i, dict))
        if length > 1:
            # if there are multiple places, ask for which one to use
            return render_template("loop.html", length=length, data=data)
        #return specific city information if there is only one
        data = data[0]
        link = f"/weather/{ data['lat'] }/{ data['lon']}"
        return redirect(link)       
    else:
        return render_template('weather.html')

@app.route("/weather/<path:lat>/<path:lon>", methods=["POST", "GET"])
def lat_n_lon(lat, lon):
    # use for finding latitude/longitude, and weather associated with it
    # Send the request to OpenWeather API
    if request.method == "GET":
        response = weather(lat, lon, api_key)
        if response == 'no':
            # reverse geocache/get city name
            y = f'({lat}, {lon})'
            return render_template('weather.html', newert=y)
        # Check if the request was successful
        else:
            # Parse JSON data
            data = response.json()
            # weather = data['weather'][0]
            return jsonify(data)
            return render_template('forecast.html', data=data)
    else:
        abort(404)

if __name__ == '__main__':
    app.run(debug=True)