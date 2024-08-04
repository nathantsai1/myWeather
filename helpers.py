import requests
from flask import Flask, request, render_template

# from another cs50 pset
def apology(message, code=400):
    """Render message as an apology to user."""
    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [
            ("-", "--"),
            (" ", "-"),
            ("_", "__"),
            ("?", "~q"),
            ("%", "~p"),
            ("#", "~h"),
            ("/", "~s"),
            ('"', "''"),
        ]:
            s = s.replace(old, new)
        return s
    return render_template("apology.html", top=code, bottom=escape(message)), code

def weather(lat, lon, api_key):
    # Construct the complete API URL
    complete_url = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_key}"
    response = requests.get(complete_url)
    if response.status_code == 200:
        # success!
        # give back the information needed
        return response
        # also lemme give you important information
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
    else:
        return 'no'
    
def location(city_name, api_key):
    # give coordinates of location based off of city_name
    complete_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=10&appid={api_key}"
    response = requests.get(complete_url)
    if response.status_code == 200:
        # if there are locations, give all of them
        return response
    else:
        # else, do not give failed response
        return 'no'
    
def reverse_geo(lat, lon, api_key):
    """
    reverse geocache city
    """
    complete_url = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_key}"
    response = requests.get(complete_url)
    if response.status_code == 200:
        return response # like above
    else:
        return 'no'
