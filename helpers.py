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
        return ['units', units]
    response = weather(lat, lon, units, api_key)
    today = reverse_weather(lat, lon, units, api_key)
    if response == 'no' or today == 'no':
        # reverse geocache/get city name
        y = f'({lat}, {lon})'
        return ['no', y]
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
        print(hope)
        return list

def icon(today):
    # return '01' in today['weather'][0]['icon']
    if '01' in today['weather'][0]['icon']:
        #    <!-- clear sky -->
        link = ["/static/clear.png", 'Clear skies', 'Made by Afif Fuden']
    elif '02' in today['weather'][0]['icon']:
        #    <!-- few clouds -->
        link = ["https://cdn-icons-png.freepik.com/512/10331/10331006.png", 'Few clouds', 'Icon by BZZRINCANTATION']
    elif '03' in today['weather'][0]['icon']:
        # <!-- scattered clouds -->
        link = ["https://cdn-icons-png.freepik.com/512/10076/10076409.png", 'scattered clouds', 'Icon by afif fuden']
    elif '04' in today['weather'][0]['icon']:
        # <!-- broken clouds -->
        link = ["https://cdn-icons-png.freepik.com/256/1116/1116455.png?ga=GA1.1.1142624802.1722824111&semt=ais_hybrid", 'broken clouds', 'Icon by Eucalyp']
    elif '09' in today['weather'][0]['icon']:
        #    <!-- shower rain -->
        link = ["https://cdn-icons-png.freepik.com/256/13035/13035105.png?ga=GA1.1.1142624802.1722824111&semt=ais_hybrid", 'shower rain', 'Icon by VectorPortal']
    elif '10' in today['weather'][0]['icon']:
        #    <!-- rainy -->
        link = ["https://cdn-icons-png.freepik.com/256/3026/3026267.png?ga=GA1.1.1142624802.1722824111&semt=ais_hybrid", 'rainy', 'Icon by Freepik']
    elif '11' in today['weather'][0]['icon']:
        #    <!-- thunderstorm 
        link = ["https://cdn-icons-png.freepik.com/256/2722/2722880.png?semt=ais_hybrid", 'thunderstorm', 'Icon by creative stall premium']
    elif '13' in today['weather'][0]['icon']:
        #    <!-- snowy -
        link = ["https://cdn-icons-png.freepik.com/256/6566/6566269.png?ga=GA1.1.1142624802.1722824111&semt=ais_hybrid", 'snowy', 'Icon by Dreamcreateicons']
    elif '50' in today['weather'][0]['icon']:
        #    <!-- misty -->
        link = ["https://cdn-icons-png.freepik.com/256/13882/13882726.png?ga=GA1.1.1142624802.1722824111&semt=ais_hybrid", 'misty', 'Icon by Grafixpoint']
    else:
        link = ['accident']

    # then get weather 
    hi = float(today['wind']['deg'])
    if hi < 22.5 or hi >= 337.5:
        link.append('N')
    elif hi >= 22.5 and hi < 67.5:
        link.append('NE')
    elif hi >= 67.5 and hi < 112.5:
        link.append('E')
    elif hi >= 112.5 and hi < 157.5:
        link.append('SE')
    elif hi >= 157.5 and hi < 202.5:
        link.append('S')
    elif hi >= 202.5 and hi < 247.5:
        link.append('SW')
    elif hi >= 247.5 and hi < 292.5:
        link.append('W')
    elif hi >= 292.5 and hi < 337.5:
        link.append('NW')
    return link
   
def timing(UTC, offset):
    """
    Converts UTC time and offset to local time zone
    """
    hope = datetime.datetime.utcfromtimestamp(UTC + offset).strftime('%H:%M:%S')

def iterations(data, day):
    """
    iterates for before/after stuff
    """
    ffinally = []
    bool = False
    hi = data['list']
    for i in hi:
        if day in i['dt_txt']:
            bool = True
            continue
        elif('12:00' in i['dt_txt'] and bool == True and day not in i['dt_txt']):
            ffinally.append(i)
    return ffinally 
    
def iterations1(data, day):
    """
    iterates for before/after stuff
    """
    ffinally = []
    bool = True
    hi = data['list']
    for i in hi:
        if day in i['dt_txt']:
            bool = False
            continue
        elif('12:00' in i['dt_txt'] and bool == True and day not in i['dt_txt']):
            ffinally.append(i)
    return ffinally 
    


