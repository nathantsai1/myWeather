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
    location,
    reverse_weather,
    time_zone,
    eez,
    icon,
    timing,
    iterations,
    iterations1
    )
import datetime
from zoneinfo import ZoneInfo

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
    if request.method == "POST":
        # check paramaters
        if not request.form.get("city") or request.form.get("city").strip() == "":
            return render_template('weather.html', empty='empty')
        
        # Construct the complete API URL
        # use openweathermap to geocode the location
        response = location(request.form.get('city'), api_key)
       
        # if there is no location
        if response == "no" or response == "":
            return render_template('weather.html', alert=request.form.get('city'))
        data = response.json()
        # give out all responses
        # get number of responses
        length = sum(1 for i in data if isinstance(i, dict))
        if length > 1:
            # if there are multiple places, ask for which one to use
            return render_template("loop.html", length=length, data=data)
        #return specific city information if there is only one
        # only if it works though
        try:
            data = data[0]
        except IndexError:
            return render_template('weather.html', alert=request.form.get('city'))
        link = f"/weather/{ data['lat'] }/{ data['lon']}"
        return redirect(link)       
    else:
        return render_template('weather.html')


@app.route("/weather/<path:lat>/<path:lon>/<path:units>", methods=["GET"])
def lat_n_lon(lat, lon, units):
    # use for finding latitude/longitude, and weather associated with it
    # Send the request to OpenWeather API
        welcoming = eez(lat, lon, units, api_key)
        # return welcoming[6]
        if welcoming[0] == 'no':
            # reverse geocache/get city name
            return render_template('weather.html', newert=welcoming[1])
        elif welcoming[0] == 'units':
            return render_template('weather.html', units=welcoming[1])
        datatize = icon(welcoming[3])
        return render_template('forecast.html', data=welcoming[0], lon=welcoming[1], lat=welcoming[2], today=welcoming[3], timing=welcoming[4], now=welcoming[5], united=welcoming[6], need=datatize)

@app.route('/weather/<path:lat>/<path:lon>/<path:units>/<path:day>', methods=['GET'])
def last(lat, lon, units, day):   
    # basically the same as above, but pass in the 'day' argument
    welcoming = eez(lat, lon, units, api_key)
    if welcoming[0] == 'no':
        # reverse geocache/get city name
        return render_template('weather.html', newert=welcoming[1])
    elif welcoming[0] == 'units':
        return render_template('weather.html', units=welcoming[1])
    datatize = icon(welcoming[3])
    # get mornings and evenings\
    hola = []
    for i in welcoming[0]['list']:
        hola.append(i['dt_txt'])
        # if welcoming is the day 'day'
        if (day in i['dt_txt']):
            # if is morning
            if ('12:00:00' in i['dt_txt']):
                morning = i
                continue
            # or night
            elif ('18:00:00' in i['dt_txt']):
                evening = i
                print('hi')
                break
    # return jsonify(morning)
    # if is evening
    after = iterations(welcoming[0], day)
    before = iterations1(welcoming[0], day)
    sunrise = timing(welcoming[0]['city']['sunrise'], welcoming[0]['city']['timezone'])
    sunset = timing(welcoming[0]['city']['sunset'], welcoming[0]['city']['timezone'])
    # pass a looooooooot of information so that jinja does not return error statements
    # also is easier to do intellectual part server side
    return render_template('oneday.html', sunrise=sunrise, sunset=sunset, 
                           morning=morning, evening=evening, data=welcoming[0], 
                            lon=welcoming[1], lat=welcoming[2], 
                           today=welcoming[3], timing=welcoming[4], 
                           now=welcoming[5], united=welcoming[6], 
                           need=datatize, special=day, before=before, after=after)

# for 'learning' what the weather symbols mean
@app.route('/learning', methods=["GET"])
def learning():
    return render_template('learning.html')

# credits due to where they are needed
@app.route('/about', methods=["GET"])
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)