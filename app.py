import requests
from flask import Flask, jsonify, request, render_template

app = Flask(__name__)
# API key and base URL for OpenWeather API
# api_key = 'd0d0e6975b6a6865318ca1e63051a638'
api_key = 'd0d0e6975b6a6865318ca1e63051a638'
base_url = 'http://api.openweathermap.org/data/2.5/weather'

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')
@app.route('/weather', methods=['GET'])
def get_weather():
    # Get the city name from query parameters, default to 'London' if not provided
    city_name = request.args.get('city', 'London')

    # Construct the complete API URL
    complete_url = f"{base_url}?q={city_name}&appid={api_key}"

    # Send the request to OpenWeather API
    response = requests.get(complete_url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse JSON data
        data = response.json()
        # gives results like:
        #{'coord': {'lon': -0.1257, 'lat': 51.5085}, 
        # 'weather': [{'id': 804, 'main': 'Clouds', 
        # 'description': 'overcast clouds', 'icon': '04n'}], 
        # 'base': 'stations', 
        # 'main': {'temp': 293.86, 'feels_like': 293.84, 'temp_min': 291.91, 'temp_max': 294.87, 'pressure': 1011, 'humidity': 71, 'sea_level': 1011, 'grnd_level': 1007}, 
        # 'visibility': 10000, 'wind': {'speed': 0.45, 'deg': 272, 'gust': 0.89}, 
        # 'clouds': {'all': 100}, 
        # 'dt': 1722633190, 
        # 'sys': {'type': 2, 'id': 2075535, 'country': 'GB', 'sunrise': 1722572772, 'sunset': 1722628031}, 
        # 'timezone': 3600, 'id': 2643743, 'name': 'London', 'cod': 200}

        # to extract from main:
        # use: main = data['main']
        # for a thing like temperature: temperature = main['temp']

        # for a thing like weather:
        # weather = data['weather'][0]
        # description = weather['discription']

        # for kelvin to ferenheihgt: Fahrenheit = ((Kelvin - 273.15) * 1.8) + 32

        # Extract specific data, e.g., temperature, description, etc.

        main = data['main']
        weather = data['weather'][0]
        
        temperature = main['temp']
        weather_description = weather['description']
        return render_template('useless.html', row=data)
        # Return the results as JSON
        return jsonify({
            'city': city_name,
            'temperature': f"{temperature}K",
            'weather_description': weather_description
        })
    else:
        # Return an error message with the status code
        return jsonify({
            'error': f"Failed to get weather data for {city_name}.",
            'status_code': response.status_code
        }), response.status_code

if __name__ == '__main__':
    app.run(debug=True)