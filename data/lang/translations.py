"""
Translations for Weather App
Contains all language strings for IT and EN

© Copyright 2024-2026 Nsfr750 - All rights reserved.
Licensed under GPLv3
"""

TRANSLATIONS = {
    'it': {
        # App title and header
        'app_title': 'Meteo ASUSTOR',
        'app_subtitle': 'Lockerstor - Weather Station',
        
        # Navigation
        'nav_home': 'Home',
        'nav_stats': 'Statistiche',
        
        # Search
        'search_placeholder': 'Inserisci città (es. Roma, Milano, Napoli)',
        'search_button': 'Cerca',
        'search_aria_label': 'Cerca città',
        
        # Language selector
        'language': 'Lingua',
        'language_it': 'Italiano',
        'language_en': 'English',
        
        # Weather info
        'current_weather': 'Condizioni Attuali',
        'forecast_5days': 'Previsioni 5 Giorni',
        'temperature': 'Temperatura',
        'feels_like': 'Percepita',
        'humidity': 'Umidità',
        'pressure': 'Pressione',
        'wind': 'Vento',
        'wind_speed': 'Velocità del vento',
        'cloudiness': 'Nuvolosità',
        'description': 'Condizioni',
        
        # Weather conditions
        'weather_clear': 'Cielo sereno',
        'weather_clear_mostly': 'Prevalentemente sereno',
        'weather_cloudy_partly': 'Parzialmente nuvoloso',
        'weather_cloudy': 'Coperto',
        'weather_fog': 'Nebbia',
        'weather_fog_rime': 'Nebbia con brina',
        'weather_drizzle_light': 'Pioviggine leggera',
        'weather_drizzle_moderate': 'Pioviggine moderata',
        'weather_drizzle_heavy': 'Pioviggine intensa',
        'weather_rain_light': 'Pioggia leggera',
        'weather_rain_moderate': 'Pioggia moderata',
        'weather_rain_heavy': 'Pioggia intensa',
        'weather_snow_light': 'Neve leggera',
        'weather_snow_moderate': 'Neve moderata',
        'weather_snow_heavy': 'Neve intensa',
        'weather_thunder': 'Temporale',
        'weather_unknown': 'Condizioni sconosciute',
        
        # Stats page
        'stats_title': 'Statistiche Meteo',
        'stats_subtitle': 'Dati storici e grafici',
        'stats_summary': 'Riepilogo',
        'stats_avg_temp': 'Temperatura Media',
        'stats_max_temp': 'Temperatura Max',
        'stats_min_temp': 'Temperatura Min',
        'stats_days_count': 'Giorni Archiviati',
        'stats_temp_trend': 'Andamento Temperature',
        'stats_humidity': 'Umidità Media',
        'stats_pressure': 'Pressione Atmosferica',
        'stats_wind': 'Velocità del Vento',
        'stats_hourly': 'Andamento Orario (Ultime 24 ore)',
        'stats_period': 'Periodo',
        'stats_7days': 'Ultimi 7 giorni',
        'stats_30days': 'Ultimi 30 giorni',
        'stats_90days': 'Ultimi 3 mesi',
        'stats_365days': 'Ultimo anno',
        
        # Time periods
        'days': 'giorni',
        'hours': 'ore',
        'today': 'Oggi',
        'tomorrow': 'Domani',
        
        # Loading and errors
        'loading': 'Caricamento dati meteo...',
        'error_loading': 'Errore durante il caricamento dei dati',
        'error_city_not_found': 'Città non trovata',
        'error_connection': 'Errore di connessione',
        'no_data': 'Nessun dato disponibile',
        'no_data_hint': 'Cerca il meteo dalla pagina principale per iniziare a raccogliere dati.',
        
        # Units
        'unit_celsius': '°C',
        'unit_percent': '%',
        'unit_hpa': 'hPa',
        'unit_ms': 'm/s',
        
        # Footer
        'powered_by': 'Powered by Open-Meteo API',
        'designed_for': 'Designed for ASUSTOR NAS',
        
        # API info
        'api_info': 'Dati forniti da Open-Meteo',
    },
    
    'en': {
        # App title and header
        'app_title': 'ASUSTOR Weather',
        'app_subtitle': 'Lockerstor - Weather Station',
        
        # Navigation
        'nav_home': 'Home',
        'nav_stats': 'Statistics',
        
        # Search
        'search_placeholder': 'Enter city (e.g., Rome, London, New York)',
        'search_button': 'Search',
        'search_aria_label': 'Search city',
        
        # Language selector
        'language': 'Language',
        'language_it': 'Italiano',
        'language_en': 'English',
        
        # Weather info
        'current_weather': 'Current Conditions',
        'forecast_5days': '5-Day Forecast',
        'temperature': 'Temperature',
        'feels_like': 'Feels Like',
        'humidity': 'Humidity',
        'pressure': 'Pressure',
        'wind': 'Wind',
        'wind_speed': 'Wind Speed',
        'cloudiness': 'Cloud Cover',
        'description': 'Conditions',
        
        # Weather conditions
        'weather_clear': 'Clear sky',
        'weather_clear_mostly': 'Mainly clear',
        'weather_cloudy_partly': 'Partly cloudy',
        'weather_cloudy': 'Overcast',
        'weather_fog': 'Fog',
        'weather_fog_rime': 'Fog with rime',
        'weather_drizzle_light': 'Light drizzle',
        'weather_drizzle_moderate': 'Moderate drizzle',
        'weather_drizzle_heavy': 'Heavy drizzle',
        'weather_rain_light': 'Light rain',
        'weather_rain_moderate': 'Moderate rain',
        'weather_rain_heavy': 'Heavy rain',
        'weather_snow_light': 'Light snow',
        'weather_snow_moderate': 'Moderate snow',
        'weather_snow_heavy': 'Heavy snow',
        'weather_thunder': 'Thunderstorm',
        'weather_unknown': 'Unknown conditions',
        
        # Stats page
        'stats_title': 'Weather Statistics',
        'stats_subtitle': 'Historical data and charts',
        'stats_summary': 'Summary',
        'stats_avg_temp': 'Average Temperature',
        'stats_max_temp': 'Max Temperature',
        'stats_min_temp': 'Min Temperature',
        'stats_days_count': 'Days Archived',
        'stats_temp_trend': 'Temperature Trend',
        'stats_humidity': 'Average Humidity',
        'stats_pressure': 'Atmospheric Pressure',
        'stats_wind': 'Wind Speed',
        'stats_hourly': 'Hourly Trend (Last 24 hours)',
        'stats_period': 'Period',
        'stats_7days': 'Last 7 days',
        'stats_30days': 'Last 30 days',
        'stats_90days': 'Last 3 months',
        'stats_365days': 'Last year',
        
        # Time periods
        'days': 'days',
        'hours': 'hours',
        'today': 'Today',
        'tomorrow': 'Tomorrow',
        
        # Loading and errors
        'loading': 'Loading weather data...',
        'error_loading': 'Error loading data',
        'error_city_not_found': 'City not found',
        'error_connection': 'Connection error',
        'no_data': 'No data available',
        'no_data_hint': 'Search for weather from the main page to start collecting data.',
        
        # Units
        'unit_celsius': '°C',
        'unit_percent': '%',
        'unit_hpa': 'hPa',
        'unit_ms': 'm/s',
        
        # Footer
        'powered_by': 'Powered by Open-Meteo API',
        'designed_for': 'Designed for ASUSTOR NAS',
        
        # API info
        'api_info': 'Data provided by Open-Meteo',
    }
}

# Weather code to translation key mapping
WEATHER_CODE_MAP = {
    0: 'weather_clear',
    1: 'weather_clear_mostly',
    2: 'weather_cloudy_partly',
    3: 'weather_cloudy',
    45: 'weather_fog',
    48: 'weather_fog_rime',
    51: 'weather_drizzle_light',
    53: 'weather_drizzle_moderate',
    55: 'weather_drizzle_heavy',
    56: 'weather_drizzle_light',  # Freezing drizzle
    57: 'weather_drizzle_heavy',  # Freezing drizzle
    61: 'weather_rain_light',
    63: 'weather_rain_moderate',
    65: 'weather_rain_heavy',
    66: 'weather_rain_light',  # Freezing rain
    67: 'weather_rain_heavy',  # Freezing rain
    71: 'weather_snow_light',
    73: 'weather_snow_moderate',
    75: 'weather_snow_heavy',
    77: 'weather_snow_light',  # Snow grains
    80: 'weather_rain_light',  # Rain showers
    81: 'weather_rain_moderate',  # Rain showers
    82: 'weather_rain_heavy',  # Rain showers
    85: 'weather_snow_light',  # Snow showers
    86: 'weather_snow_heavy',  # Snow showers
    95: 'weather_thunder',
    96: 'weather_thunder',  # Thunderstorm with hail
    99: 'weather_thunder',  # Thunderstorm with heavy hail
}


def get_weather_translation_key(weather_code: int) -> str:
    """Get translation key for weather code."""
    return WEATHER_CODE_MAP.get(weather_code, 'weather_unknown')
