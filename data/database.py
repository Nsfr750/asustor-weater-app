"""
Database module for Weather App
SQLite database for storing daily weather statistics

© Copyright 2024-2026 Nsfr750 - All rights reserved.
Licensed under GPLv3
"""

import sqlite3
import os
from datetime import datetime, timedelta
from typing import Optional, List, Dict, Any


class WeatherDatabase:
    """SQLite database manager for weather data."""
    
    def __init__(self, db_path: Optional[str] = None):
        """Initialize database connection."""
        if db_path is None:
            # Default location in app directory
            app_dir = os.path.dirname(os.path.abspath(__file__))
            db_path = os.path.join(app_dir, "weather_data.db")
        
        self.db_path = db_path
        self.init_database()
    
    def get_connection(self) -> sqlite3.Connection:
        """Get database connection with row factory."""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn
    
    def init_database(self):
        """Initialize database tables."""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        # Daily weather statistics table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS daily_weather (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                city TEXT NOT NULL,
                country TEXT,
                date DATE NOT NULL,
                temperature_max REAL,
                temperature_min REAL,
                temperature_avg REAL,
                humidity_avg REAL,
                pressure_avg REAL,
                wind_speed_max REAL,
                wind_speed_avg REAL,
                weather_code INTEGER,
                weather_description TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                UNIQUE(city, date)
            )
        """)
        
        # Hourly snapshots for detailed graphs
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS hourly_weather (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                city TEXT NOT NULL,
                timestamp TIMESTAMP NOT NULL,
                temperature REAL,
                humidity REAL,
                pressure REAL,
                wind_speed REAL,
                weather_code INTEGER,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        # Index for faster queries
        cursor.execute("""
            CREATE INDEX IF NOT EXISTS idx_daily_city_date 
            ON daily_weather(city, date)
        """)
        
        cursor.execute("""
            CREATE INDEX IF NOT EXISTS idx_hourly_city_timestamp 
            ON hourly_weather(city, timestamp)
        """)
        
        conn.commit()
        conn.close()
    
    def save_daily_weather(self, data: Dict[str, Any]) -> bool:
        """Save daily weather summary."""
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            
            cursor.execute("""
                INSERT OR REPLACE INTO daily_weather (
                    city, country, date, temperature_max, temperature_min,
                    temperature_avg, humidity_avg, pressure_avg, wind_speed_max,
                    wind_speed_avg, weather_code, weather_description
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                data.get("city"),
                data.get("country"),
                data.get("date"),
                data.get("temperature_max"),
                data.get("temperature_min"),
                data.get("temperature_avg"),
                data.get("humidity_avg"),
                data.get("pressure_avg"),
                data.get("wind_speed_max"),
                data.get("wind_speed_avg"),
                data.get("weather_code"),
                data.get("weather_description")
            ))
            
            conn.commit()
            conn.close()
            return True
            
        except Exception as e:
            print(f"Error saving daily weather: {e}")
            return False
    
    def save_hourly_weather(self, data: Dict[str, Any]) -> bool:
        """Save hourly weather snapshot."""
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            
            cursor.execute("""
                INSERT INTO hourly_weather (
                    city, timestamp, temperature, humidity, pressure,
                    wind_speed, weather_code
                ) VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (
                data.get("city"),
                data.get("timestamp"),
                data.get("temperature"),
                data.get("humidity"),
                data.get("pressure"),
                data.get("wind_speed"),
                data.get("weather_code")
            ))
            
            conn.commit()
            conn.close()
            return True
            
        except Exception as e:
            print(f"Error saving hourly weather: {e}")
            return False
    
    def get_daily_stats(self, city: str, days: int = 30) -> List[Dict[str, Any]]:
        """Get daily statistics for a city."""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        date_from = (datetime.now() - timedelta(days=days)).strftime("%Y-%m-%d")
        
        cursor.execute("""
            SELECT * FROM daily_weather 
            WHERE city = ? AND date >= ?
            ORDER BY date ASC
        """, (city, date_from))
        
        rows = cursor.fetchall()
        conn.close()
        
        return [dict(row) for row in rows]
    
    def get_hourly_stats(self, city: str, hours: int = 24) -> List[Dict[str, Any]]:
        """Get hourly statistics for a city."""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        time_from = datetime.now() - timedelta(hours=hours)
        
        cursor.execute("""
            SELECT * FROM hourly_weather 
            WHERE city = ? AND timestamp >= ?
            ORDER BY timestamp ASC
        """, (city, time_from))
        
        rows = cursor.fetchall()
        conn.close()
        
        return [dict(row) for row in rows]
    
    def get_temperature_stats(self, city: str, days: int = 30) -> Dict[str, Any]:
        """Get temperature statistics summary."""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        date_from = (datetime.now() - timedelta(days=days)).strftime("%Y-%m-%d")
        
        cursor.execute("""
            SELECT 
                AVG(temperature_avg) as avg_temp,
                MAX(temperature_max) as max_temp,
                MIN(temperature_min) as min_temp,
                COUNT(*) as days_count
            FROM daily_weather 
            WHERE city = ? AND date >= ?
        """, (city, date_from))
        
        row = cursor.fetchone()
        conn.close()
        
        if row:
            return {
                "average": round(row["avg_temp"], 1) if row["avg_temp"] else None,
                "maximum": row["max_temp"],
                "minimum": row["min_temp"],
                "days_count": row["days_count"]
            }
        return {}
    
    def get_cities_with_data(self) -> List[str]:
        """Get list of cities with stored data."""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT DISTINCT city FROM daily_weather ORDER BY city ASC
        """)
        
        rows = cursor.fetchall()
        conn.close()
        
        return [row["city"] for row in rows]
    
    def cleanup_old_data(self, days: int = 365):
        """Remove data older than specified days."""
        conn = self.get_connection()
        cursor = conn.cursor()
        
        date_limit = (datetime.now() - timedelta(days=days)).strftime("%Y-%m-%d")
        time_limit = datetime.now() - timedelta(days=days)
        
        cursor.execute("""
            DELETE FROM daily_weather WHERE date < ?
        """, (date_limit,))
        
        cursor.execute("""
            DELETE FROM hourly_weather WHERE timestamp < ?
        """, (time_limit,))
        
        conn.commit()
        conn.close()


# Singleton instance
db = WeatherDatabase()
