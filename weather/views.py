from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.conf import settings
import requests
import json

# Create your views here.
def weather(request):
    api_key = settings.OPENWEATHER_API_KEY
    
    # Get city name from request (required)
    city_name = request.GET.get('city', '')
    
    # Get units parameter, default to 'metric' (Celsius)
    units = request.GET.get('units', 'metric')
    
    # If no city provided, show empty form
    if not city_name:
        context = {
            'city': '',
            'error': None,
            'units': units,
        }
        return render(request, 'weather/weather.html', context)
    
    # Step 1: Get latitude and longitude from city name using Geocoding API
    geocoding_url = "http://api.openweathermap.org/geo/1.0/direct"
    geocoding_params = {
        'q': city_name,
        'limit': 1,
        'appid': api_key
    }
    
    try:
        geocoding_response = requests.get(geocoding_url, params=geocoding_params)
        geocoding_data = geocoding_response.json()
        
        # Check if geocoding was successful
        if not geocoding_data or len(geocoding_data) == 0:
            context = {
                'city': city_name,
                'error': 'City not found. Please check the city name and try again.',
                'units': units,
            }
            return render(request, 'weather/weather.html', context)
        
        # Extract lat and lon from geocoding response
        lat = geocoding_data[0]['lat']
        lon = geocoding_data[0]['lon']
        
        # Step 2: Get current weather data using coordinates
        weather_url = "https://api.openweathermap.org/data/2.5/weather"
        
        # Map units parameter to OpenWeather API format
        units_map = {
            'metric': 'metric',  # Celsius
            'imperial': 'imperial',  # Fahrenheit
            'kelvin': 'standard'  # Kelvin
        }
        api_units = units_map.get(units, 'metric')
        
        weather_params = {
            'lat': lat,
            'lon': lon,
            'appid': api_key,
            'units': api_units,
        }
        
        # Make the weather API call
        weather_response = requests.get(weather_url, params=weather_params)
        weather_response.raise_for_status()
        raw_data = weather_response.json()
        
        # Determine temperature unit symbol
        unit_symbol = '°C' if units == 'metric' else '°F' if units == 'imperial' else 'K'
        
        # Prepare weather data for template
        weather_data = {
            "city": raw_data["name"],
            "country_code": raw_data["sys"]["country"],
            "coordinate": f"{raw_data['coord']['lon']:.2f}, {raw_data['coord']['lat']:.2f}",
            "temp": round(raw_data["main"]["temp"], 1),
            "temp_unit": unit_symbol,
            "feels_like": round(raw_data["main"]["feels_like"], 1),
            "humidity": raw_data["main"]["humidity"],
            "pressure": raw_data["main"]["pressure"],
            "description": raw_data["weather"][0]["description"].title(),
            "icon": raw_data["weather"][0]["icon"],
            "wind_speed": raw_data.get("wind", {}).get("speed", 0),
            "visibility": raw_data.get("visibility", 0) / 1000 if raw_data.get("visibility") else None,  # Convert to km
        }
        
        context = {
            'weather': weather_data,
            'city': city_name,
            'units': units,
            'error': None,
        }
        
        return render(request, 'weather/weather.html', context)
        
    except requests.exceptions.RequestException as e:
        context = {
            'city': city_name,
            'error': 'Unable to fetch weather data. Please try again later.',
            'units': units,
        }
        return render(request, 'weather/weather.html', context)
    except Exception as e:
        context = {
            'city': city_name,
            'error': 'An error occurred while fetching weather data.',
            'units': units,
        }
        return render(request, 'weather/weather.html', context)
