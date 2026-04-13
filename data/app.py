"""
Weather App for ASUSTOR NAS Lockerstor 6604T
A Flask-based web application for displaying weather conditions.
Powered by Open-Meteo API (free, no API key required)

Project Structure:
- CONTROL/: ASUSTOR control files (scripts, config.json, icon.png)
- data/: Application files (this file, templates/, static/, database.py)
- After APK install on NAS: /usr/local/AppCentral/weather-app/

© Copyright 2024-2026 Nsfr750 - All rights reserved.
Licensed under GPLv3
"""

import os
import requests
from datetime import datetime, date
from flask import Flask, render_template, jsonify, request, session
from database import db
from lang.language_manager import get_language_manager, get_weather_description, translate

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'weather-app-secret-key')

# Initialize language manager
lang_manager = get_language_manager('it')

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


def get_current_language():
    """Get current language from session or default."""
    return session.get('language', 'it')


def set_current_language(lang):
    """Set current language in session."""
    if lang in ['it', 'en']:
        session['language'] = lang
        lang_manager.set_language(lang)
        return True
    return False


def get_localized_description(weather_code):
    """Get weather description in current language based on WMO weather code."""
    return get_weather_description(weather_code, get_current_language())


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
    
    # Save hourly snapshot to database
    hourly_data = {
        "city": coords["name"],
        "timestamp": datetime.now(),
        "temperature": current.get("temperature_2m"),
        "humidity": current.get("relative_humidity_2m"),
        "pressure": current.get("pressure_msl"),
        "wind_speed": current.get("wind_speed_10m"),
        "weather_code": weather_code
    }
    db.save_hourly_weather(hourly_data)
    
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
        "default_country": DEFAULT_COUNTRY,
        "current_language": get_current_language(),
        "supported_languages": lang_manager.get_supported_languages()
    })


@app.route("/api/language", methods=['GET', 'POST'])
def api_language():
    """Get or set current language."""
    if request.method == 'POST':
        data = request.get_json()
        lang = data.get('language', 'it')
        if set_current_language(lang):
            return jsonify({
                "success": True,
                "language": lang,
                "message": translate('language_set', lang)
            })
        return jsonify({
            "success": False,
            "error": "Invalid language"
        }), 400
    
    # GET request
    return jsonify({
        "language": get_current_language(),
        "supported": lang_manager.get_supported_languages()
    })


@app.route("/api/translations")
def api_translations():
    """Get all translations for current or specified language."""
    lang = request.args.get('lang', get_current_language())
    translations = lang_manager.get_all_translations(lang)
    return jsonify({
        "language": lang,
        "translations": translations
    })


@app.route("/api/stats/daily")
def api_daily_stats():
    """API endpoint for daily statistics."""
    city = request.args.get("city", DEFAULT_CITY)
    days = request.args.get("days", 30, type=int)
    
    stats = db.get_daily_stats(city, days)
    return jsonify({
        "city": city,
        "days": days,
        "data": stats
    })


@app.route("/api/stats/hourly")
def api_hourly_stats():
    """API endpoint for hourly statistics."""
    city = request.args.get("city", DEFAULT_CITY)
    hours = request.args.get("hours", 24, type=int)
    
    stats = db.get_hourly_stats(city, hours)
    return jsonify({
        "city": city,
        "hours": hours,
        "data": stats
    })


@app.route("/api/stats/summary")
def api_stats_summary():
    """API endpoint for temperature summary statistics."""
    city = request.args.get("city", DEFAULT_CITY)
    days = request.args.get("days", 30, type=int)
    
    summary = db.get_temperature_stats(city, days)
    return jsonify({
        "city": city,
        "days": days,
        "summary": summary
    })


@app.route("/api/stats/cities")
def api_cities():
    """API endpoint for list of cities with data."""
    cities = db.get_cities_with_data()
    return jsonify({"cities": cities})


@app.route("/stats")
def stats_page():
    """Statistics page route."""
    return render_template("stats.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=False)
