"""
Weather App for ASUSTOR NAS Lockerstor 6604T
A Flask-based web application for displaying weather conditions.
Powered by Open-Meteo API (free, no API key required)

© Copyright 2024-2026 Nsfr750 - All rights reserved.
Licensed under GPLv3
"""

import os
import requests
from datetime import datetime
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# Open-Meteo API - free, no API key required
DEFAULT_CITY = "Rome"
DEFAULT_COUNTRY = "IT"

GEOCODING_API_URL = "https://geocoding-api.open-meteo.com/v1/search"
WEATHER_API_URL = "https://api.open-meteo.com/v1/forecast"


def get_coordinates(city):
    """Get latitude and longitude for a city using Open-Meteo Geocoding API."""
    params = {
        "name": city,
        "count": 1,
        "language": "it",
        "format": "json"
    }
    
    try:
        response = requests.get(GEOCODING_API_URL, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        if not data.get("results"):
            return {"error": f"Città '{city}' non trovata"}
        
        result = data["results"][0]
        return {
            "lat": result["latitude"],
            "lon": result["longitude"],
            "name": result.get("name", city),
            "country": result.get("country_code", "")
        }
    except requests.exceptions.RequestException as e:
        return {"error": f"Errore di connessione: {str(e)}"}


def get_weather_data(lat, lon):
    """Fetch current weather data from Open-Meteo API."""
    params = {
        "latitude": lat,
        "longitude": lon,
        "current": ["temperature_2m", "relative_humidity_2m", "apparent_temperature", 
                    "is_day", "weather_code", "pressure_msl", "wind_speed_10m", 
                    "wind_direction_10m", "cloud_cover"],
        "timezone": "auto"
    }
    
    try:
        response = requests.get(WEATHER_API_URL, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": f"Errore di connessione: {str(e)}"}


def get_forecast_data(lat, lon):
    """Fetch 7-day forecast data from Open-Meteo API."""
    params = {
        "latitude": lat,
        "longitude": lon,
        "daily": ["weather_code", "temperature_2m_max", "temperature_2m_min", 
                  "relative_humidity_2m_mean", "wind_speed_10m_max"],
        "timezone": "auto",
        "forecast_days": 6
    }
    
    try:
        response = requests.get(WEATHER_API_URL, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": f"Errore di connessione: {str(e)}"}


def get_weather_icon_url(weather_code, is_day=1):
    """Get weather icon URL based on WMO weather code."""
    # Map WMO codes to icon names
    icon_map = {
        0: "clear",           # Clear sky
        1: "cloudy-light",    # Mainly clear
        2: "cloudy-light",    # Partly cloudy
        3: "cloudy",          # Overcast
        45: "fog",            # Fog
        48: "fog",            # Depositing rime fog
        51: "rain-light",     # Drizzle light
        53: "rain-light",     # Drizzle moderate
        55: "rain",           # Drizzle dense
        56: "rain-light",     # Freezing drizzle light
        57: "rain",           # Freezing drizzle dense
        61: "rain-light",     # Rain slight
        63: "rain",           # Rain moderate
        65: "rain-heavy",     # Rain heavy
        66: "rain-light",     # Freezing rain light
        67: "rain-heavy",     # Freezing rain heavy
        71: "snow-light",     # Snow fall slight
        73: "snow",           # Snow fall moderate
        75: "snow-heavy",     # Snow fall heavy
        77: "snow-light",     # Snow grains
        80: "rain-light",     # Rain showers slight
        81: "rain",           # Rain showers moderate
        82: "rain-heavy",     # Rain showers violent
        85: "snow-light",     # Snow showers slight
        86: "snow-heavy",     # Snow showers heavy
        95: "thunder",        # Thunderstorm
        96: "thunder",        # Thunderstorm with hail
        99: "thunder"         # Thunderstorm with heavy hail
    }
    
    icon_name = icon_map.get(weather_code, "unknown")
    
    # Use Open-Meteo's built-in icon service
    return f"https://bmcdn.nl/assets/weather-icons/v3.0/fill/svg/{icon_name}.svg"


def get_weather_description(weather_code):
    """Get weather description in Italian based on WMO weather code."""
    descriptions = {
        0: "Cielo sereno",
        1: "Prevalentemente sereno",
        2: "Parzialmente nuvoloso",
        3: "Coperto",
        45: "Nebbia",
        48: "Nebbia con brina",
        51: "Pioviggine leggera",
        53: "Pioviggine moderata",
        55: "Pioviggine intensa",
        56: "Pioviggine gelata leggera",
        57: "Pioviggine gelata intensa",
        61: "Pioggia leggera",
        63: "Pioggia moderata",
        65: "Pioggia intensa",
        66: "Pioggia gelata leggera",
        67: "Pioggia gelata intensa",
        71: "Neve leggera",
        73: "Neve moderata",
        75: "Neve intensa",
        77: "Grani di neve",
        80: "Rovesci leggeri",
        81: "Rovesci moderati",
        82: "Rovesci violenti",
        85: "Nevicate leggere",
        86: "Nevicate intense",
        95: "Temporale",
        96: "Temporale con grandine",
        99: "Temporale con forte grandine"
    }
    return descriptions.get(weather_code, "Condizioni sconosciute")


@app.route("/")
def index():
    """Main page route."""
    return render_template("index.html")


@app.route("/api/weather")
def api_weather():
    """API endpoint for current weather."""
    city = request.args.get("city", DEFAULT_CITY)
    
    # Get coordinates for the city
    coords = get_coordinates(city)
    if "error" in coords:
        return jsonify(coords), 400
    
    # Get weather data using coordinates
    data = get_weather_data(coords["lat"], coords["lon"])
    
    if "error" in data:
        return jsonify(data), 400
    
    current = data.get("current", {})
    weather_code = current.get("weather_code", 0)
    is_day = current.get("is_day", 1)
    
    # Format the response
    weather_info = {
        "city": coords["name"],
        "country": coords["country"],
        "temperature": round(current.get("temperature_2m", 0), 1),
        "feels_like": round(current.get("apparent_temperature", 0), 1),
        "humidity": current.get("relative_humidity_2m", 0),
        "pressure": current.get("pressure_msl", 0),
        "wind_speed": current.get("wind_speed_10m", 0),
        "wind_deg": current.get("wind_direction_10m", 0),
        "description": get_weather_description(weather_code),
        "icon": get_weather_icon_url(weather_code, is_day),
        "clouds": current.get("cloud_cover", 0),
        "timestamp": datetime.now().strftime("%d/%m/%Y %H:%M")
    }
    
    return jsonify(weather_info)


@app.route("/api/forecast")
def api_forecast():
    """API endpoint for weather forecast."""
    city = request.args.get("city", DEFAULT_CITY)
    
    # Get coordinates for the city
    coords = get_coordinates(city)
    if "error" in coords:
        return jsonify(coords), 400
    
    # Get forecast data using coordinates
    data = get_forecast_data(coords["lat"], coords["lon"])
    
    if "error" in data:
        return jsonify(data), 400
    
    daily = data.get("daily", {})
    daily_forecasts = []
    
    # Open-Meteo returns arrays for daily data
    dates = daily.get("time", [])
    weather_codes = daily.get("weather_code", [])
    temp_max = daily.get("temperature_2m_max", [])
    temp_min = daily.get("temperature_2m_min", [])
    humidity = daily.get("relative_humidity_2m_mean", [])
    wind_speed = daily.get("wind_speed_10m_max", [])
    
    # Build forecast list (skip today, get next 5 days)
    for i in range(1, min(6, len(dates))):
        date_obj = datetime.strptime(dates[i], "%Y-%m-%d")
        weather_code = weather_codes[i] if i < len(weather_codes) else 0
        
        daily_forecasts.append({
            "date": date_obj.strftime("%d/%m"),
            "day": date_obj.strftime("%A").capitalize(),
            "temperature": round((temp_max[i] + temp_min[i]) / 2, 1) if i < len(temp_max) else 0,
            "temp_max": round(temp_max[i], 1) if i < len(temp_max) else 0,
            "temp_min": round(temp_min[i], 1) if i < len(temp_min) else 0,
            "description": get_weather_description(weather_code),
            "icon": get_weather_icon_url(weather_code, 1),
            "humidity": humidity[i] if i < len(humidity) else 0,
            "wind_speed": wind_speed[i] if i < len(wind_speed) else 0
        })
    
    return jsonify({
        "city": coords["name"],
        "country": coords["country"],
        "forecasts": daily_forecasts
    })


@app.route("/api/config")
def api_config():
    """Get default configuration."""
    return jsonify({
        "default_city": DEFAULT_CITY,
        "default_country": DEFAULT_COUNTRY
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=False)
