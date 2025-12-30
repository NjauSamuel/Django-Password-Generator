from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.conf import settings
import requests
import json

# Create your views here.
def weather(request):
    api_key = settings.OPENWEATHER_API_KEY
    
    # Get city name from request (defaults to Thika if not provided)
    city_name = request.GET.get('city', 'Thika')
    
    # Step 1: Get latitude and longitude from city name using Geocoding API
    geocoding_url = "http://api.openweathermap.org/geo/1.0/direct"
    geocoding_params = {
        'q': city_name,
        'limit': 1,
        'appid': api_key
    }
    
    geocoding_response = requests.get(geocoding_url, params=geocoding_params)
    geocoding_data = geocoding_response.json()
    
    # Check if geocoding was successful
    if not geocoding_data or len(geocoding_data) == 0:
        return JsonResponse({'error': 'City not found'}, status=404)
    
    # Extract lat and lon from geocoding response
    lat = geocoding_data[0]['lat']
    lon = geocoding_data[0]['lon']
    
    # Step 2: Get current weather data using coordinates
    weather_url = "https://api.openweathermap.org/data/2.5/weather"
    weather_params = {
        'lat': lat,
        'lon': lon,
        'appid': api_key,
        'units': 'metric',  # always return metric (Celsius) values
    }
    
    # Make the weather API call
    weather_response = requests.get(weather_url, params=weather_params)
    raw_data = weather_response.json()
    
    # Reduce the response to the key fields similar to the tutorial
    reduced_data = {
        "city": raw_data["name"],
        "country_code": raw_data["sys"]["country"],
        "coordinate": str(raw_data["coord"]["lon"]) + ' ' + str(raw_data["coord"]["lat"]),
        "temp": round(raw_data["main"]["temp"], 2),  # already in °C due to units=metric
        "humidity": str(raw_data["main"]["humidity"]),
        "description": raw_data["weather"][0]["description"],
    }
    
    return JsonResponse(reduced_data)
