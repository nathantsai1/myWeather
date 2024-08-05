import requests
from flask import Flask, request, render_template, jsonify
import datetime
from zoneinfo import ZoneInfo

def time_zone(lat, lon, api_key):
    # construct complete API URL
    complete_url = f" http://api.timezonedb.com/v2.1/get-time-zone?key={api_key}&format=json&by=position&lat={lat}&lng={lon}"
    response = requests.get(complete_url)
    return response

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

# because this needs to go on two different sites
def eez(lat, lon, units, api_key):
    # make sure units is actually a units
    if (units !="standard" and units != "metric" and units != "imperial"):
        return 'units'
    response = weather(lat, lon, units, api_key)
    today = reverse_weather(lat, lon, units, api_key)
    if response == 'no' or today == 'no':
        # reverse geocache/get city name
        y = f'({lat}, {lon})'
        return 'no'
    # Check if the request was successful
    else:
        api = 'Y6MYXZF20VQF'
        timed = time_zone(lat, lon, api)
        # Parse JSON data
        dataday = today.json()
        # dataday is today's 
        data = response.json()
        # data is the week
        zoned = timed.json()
        # return data
        # and zoned is the time zone
        # get time:
        hope = datetime.datetime.utcfromtimestamp(dataday['dt'] + dataday['timezone']).strftime('%Y-%m-%d %H:%M:%S')
        list = [data, lon, lat, dataday, zoned, hope, units]
        return list
