/*
 * Weather App for ASUSTOR NAS Lockerstor 6604T
 * © Copyright 2024-2026 Nsfr750 - All rights reserved.
 * Licensed under GPLv3
 * Powered by Open-Meteo API
 */

document.addEventListener('DOMContentLoaded', function() {
    const cityInput = document.getElementById('cityInput');
    const searchBtn = document.getElementById('searchBtn');
    const loading = document.getElementById('loading');
    const error = document.getElementById('error');
    const weatherContainer = document.getElementById('weatherContainer');
    const forecastContainer = document.getElementById('forecastContainer');

    // Load saved city from localStorage
    const savedCity = localStorage.getItem('weatherCity');
    if (savedCity) {
        cityInput.value = savedCity;
    }

    // Event listeners
    searchBtn.addEventListener('click', searchWeather);
    cityInput.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') searchWeather();
    });

    // Auto-load weather if we have a saved city
    if (cityInput.value) {
        searchWeather();
    }

    async function searchWeather() {
        const city = cityInput.value.trim();

        if (!city) {
            showError('Inserisci il nome di una città');
            return;
        }

        // Save to localStorage
        localStorage.setItem('weatherCity', city);

        hideError();
        showLoading();

        try {
            // Fetch current weather
            const weatherResponse = await fetch(`/api/weather?city=${encodeURIComponent(city)}`);
            const weatherData = await weatherResponse.json();

            if (!weatherResponse.ok) {
                throw new Error(weatherData.error || 'Errore nel recupero dei dati meteo');
            }

            // Fetch forecast
            const forecastResponse = await fetch(`/api/forecast?city=${encodeURIComponent(city)}`);
            const forecastData = await forecastResponse.json();

            if (!forecastResponse.ok) {
                throw new Error(forecastData.error || 'Errore nel recupero delle previsioni');
            }

            displayWeather(weatherData);
            displayForecast(forecastData);
            showWeather();

        } catch (err) {
            showError(err.message);
            hideLoading();
        }
    }

    function displayWeather(data) {
        document.getElementById('cityName').textContent = data.city;
        document.getElementById('countryCode').textContent = data.country;
        document.getElementById('timestamp').textContent = `Aggiornato: ${data.timestamp}`;

        document.getElementById('weatherIcon').src = data.icon;
        document.getElementById('weatherIcon').alt = data.description;
        document.getElementById('temperature').textContent = data.temperature;
        document.getElementById('description').textContent = data.description;

        document.getElementById('feelsLike').textContent = data.feels_like;
        document.getElementById('humidity').textContent = data.humidity;
        document.getElementById('pressure').textContent = data.pressure;
        document.getElementById('windSpeed').textContent = data.wind_speed;
        document.getElementById('clouds').textContent = data.clouds;
    }

    function displayForecast(data) {
        forecastContainer.innerHTML = '';

        const days = ['Domenica', 'Lunedì', 'Martedì', 'Mercoledì', 'Giovedì', 'Venerdì', 'Sabato'];

        data.forecasts.forEach(day => {
            const dayDiv = document.createElement('div');
            dayDiv.className = 'forecast-day';

            // Convert English day name to Italian
            const date = new Date(day.date.split('/').reverse().join('-'));
            const dayName = days[date.getDay()] || day.day;

            // Use SVG icons from Open-Meteo
            const iconUrl = day.icon || '';

            dayDiv.innerHTML = `
                <div class="day-name">${dayName}</div>
                <div class="day-date">${day.date}</div>
                <img src="${iconUrl}" alt="${day.description}" onerror="this.style.display='none'">
                <div class="temp-range">
                    <span class="temp-max">↑${day.temp_max}°</span>
                    <span class="temp-min">↓${day.temp_min}°</span>
                </div>
                <div class="temp-avg">${day.temperature}°C</div>
                <div class="desc">${day.description}</div>
                <div class="details">
                    💧 ${day.humidity}% | 💨 ${day.wind_speed} m/s
                </div>
            `;

            forecastContainer.appendChild(dayDiv);
        });
    }

    function showLoading() {
        loading.classList.remove('hidden');
        weatherContainer.classList.add('hidden');
    }

    function hideLoading() {
        loading.classList.add('hidden');
    }

    function showWeather() {
        hideLoading();
        weatherContainer.classList.remove('hidden');
    }

    function showError(message) {
        error.textContent = message;
        error.classList.remove('hidden');
        weatherContainer.classList.add('hidden');
    }

    function hideError() {
        error.classList.add('hidden');
    }
});
