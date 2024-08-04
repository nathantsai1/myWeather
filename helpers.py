import requests
from flask import Flask, request, render_template, jsonify

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

def weather(lat, lon, units, api_key):
    # Construct the complete API URL
    complete_url = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&units={units}&appid={api_key}"
    response = requests.get(complete_url)
    if response.status_code == 200:
        # success!
        # give back the information needed
        return response
    else:
        return 'no'

def reverse_weather(lat, lon, units, api_key):
    # give weather not forecast as above
    # Construct the complete API URL
    complete_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units={units}&appid={api_key}"

    response = requests.get(complete_url)
    if response.status_code == 200:
        # success!
        # give back the information needed
        return response
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

