# Visit https://openweathermap.org/api
import json
import requests
from dotenv import load_dotenv
import sys
import os

load_dotenv()

APPID = os.getenv('OPENWEATHER_API_KEY')

# Compute location from command line arguments

if len(sys.argv) < 2:
    print("Usage: getOpenWeather.py city_name, 2-letter_country_code")
    sys.exit()
# location = ' '.join(sys.argv[1:])
city = ' '.join(sys.argv[1:-1])
country = sys.argv[-1]     
location = f"{city},{country}"

# Download the JSON data from openweatherMap API
url = "https://api.openweathermap.org/data/2.5/weather"

params = {
    "q": location,
    "appid": APPID,
    "units": "metric"
}

response = requests.get(url, params=params)
response.raise_for_status()
weather_data = response.json() # a python dictionary


# Convert back to JSON object for pretty printing
# print(json.dumps(weather_data, indent=3))

# Extracting useful data

city = weather_data["name"]
temp = weather_data["main"]["temp"]
feels_like = weather_data["main"]["feels_like"]
description = weather_data["weather"][0]["description"]
humidity = weather_data["main"]["humidity"]
wind_speed = weather_data["wind"]["speed"]

# Creating a personal data structure
clean_data = {
    "city": city,
    "temperature": temp,
    "feels_like": feels_like,
    "description": description,
    "humidity": humidity,
    "wind_speed": wind_speed
}

# Saving results as JSON for future use
with open("weather.json", "w") as file:
    json.dump(clean_data, file, indent=2)