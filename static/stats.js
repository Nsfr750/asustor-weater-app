/**
 * Statistics JavaScript for Weather App
 * Handles charts and data visualization using Chart.js
 * 
 * © Copyright 2024-2026 Nsfr750 - All rights reserved.
 * Licensed under GPLv3
 */

// Chart instances
let tempChart, humidityChart, pressureChart, windChart, hourlyChart;

// Load default city on page load
document.addEventListener('DOMContentLoaded', function() {
    loadConfig().then(() => {
        loadStats();
    });
    
    // Event listeners
    document.getElementById('searchBtn').addEventListener('click', loadStats);
    document.getElementById('cityInput').addEventListener('keypress', function(e) {
        if (e.key === 'Enter') loadStats();
    });
});

// Load configuration
async function loadConfig() {
    try {
        const response = await fetch('/api/config');
        const config = await response.json();
        document.getElementById('cityInput').value = config.default_city;
    } catch (error) {
        console.error('Error loading config:', error);
    }
}

// Show/hide loading
function showLoading(show) {
    document.getElementById('loading').classList.toggle('hidden', !show);
    document.getElementById('statsContainer').classList.toggle('hidden', show);
}

// Show error message
function showError(message) {
    const errorEl = document.getElementById('error');
    errorEl.textContent = message;
    errorEl.classList.remove('hidden');
    showLoading(false);
}

// Clear error
function clearError() {
    document.getElementById('error').classList.add('hidden');
}

// Load all statistics
async function loadStats() {
    clearError();
    showLoading(true);
    
    const city = document.getElementById('cityInput').value.trim() || 'Roma';
    const days = document.getElementById('daysSelect').value;
    
    try {
        // Load summary, daily and hourly data in parallel
        const [summaryRes, dailyRes, hourlyRes] = await Promise.all([
            fetch(`/api/stats/summary?city=${encodeURIComponent(city)}&days=${days}`),
            fetch(`/api/stats/daily?city=${encodeURIComponent(city)}&days=${days}`),
            fetch(`/api/stats/hourly?city=${encodeURIComponent(city)}&hours=24`)
        ]);
        
        const summary = await summaryRes.json();
        const daily = await dailyRes.json();
        const hourly = await hourlyRes.json();
        
        // Check if we have data
        if (!daily.data || daily.data.length === 0) {
            showNoData();
            return;
        }
        
        showData();
        
        // Update summary cards
        updateSummary(summary.summary);
        
        // Update charts
        updateTempChart(daily.data);
        updateHumidityChart(daily.data);
        updatePressureChart(daily.data);
        updateWindChart(daily.data);
        updateHourlyChart(hourly.data);
        
        showLoading(false);
        
    } catch (error) {
        console.error('Error loading stats:', error);
        showError('Errore durante il caricamento delle statistiche.');
    }
}

// Show no data message
function showNoData() {
    document.getElementById('noData').classList.remove('hidden');
    document.getElementById('statsContainer').classList.add('hidden');
    showLoading(false);
}

// Show data container
function showData() {
    document.getElementById('noData').classList.add('hidden');
    document.getElementById('statsContainer').classList.remove('hidden');
}

// Update summary cards
function updateSummary(summary) {
    document.getElementById('avgTemp').textContent = summary.average || '-';
    document.getElementById('maxTemp').textContent = summary.maximum || '-';
    document.getElementById('minTemp').textContent = summary.minimum || '-';
    document.getElementById('daysCount').textContent = summary.days_count || '-';
}

// Common chart options
const commonOptions = {
    responsive: true,
    maintainAspectRatio: true,
    plugins: {
        legend: {
            display: true
        }
    },
    scales: {
        x: {
            ticks: {
                maxRotation: 45,
                minRotation: 45
            }
        }
    }
};

// Update temperature chart
function updateTempChart(data) {
    const ctx = document.getElementById('tempChart').getContext('2d');
    
    const labels = data.map(d => {
        const date = new Date(d.date);
        return date.toLocaleDateString('it-IT', { day: '2-digit', month: 'short' });
    });
    
    const maxTemps = data.map(d => d.temperature_max);
    const minTemps = data.map(d => d.temperature_min);
    const avgTemps = data.map(d => d.temperature_avg);
    
    if (tempChart) tempChart.destroy();
    
    tempChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: labels,
            datasets: [
                {
                    label: 'Max',
                    data: maxTemps,
                    borderColor: '#ff6b6b',
                    backgroundColor: 'rgba(255, 107, 107, 0.1)',
                    tension: 0.4
                },
                {
                    label: 'Media',
                    data: avgTemps,
                    borderColor: '#4ecdc4',
                    backgroundColor: 'rgba(78, 205, 196, 0.1)',
                    tension: 0.4
                },
                {
                    label: 'Min',
                    data: minTemps,
                    borderColor: '#45b7d1',
                    backgroundColor: 'rgba(69, 183, 209, 0.1)',
                    tension: 0.4
                }
            ]
        },
        options: {
            ...commonOptions,
            plugins: {
                ...commonOptions.plugins,
                title: {
                    display: false
                }
            },
            scales: {
                ...commonOptions.scales,
                y: {
                    title: {
                        display: true,
                        text: 'Temperatura (°C)'
                    }
                }
            }
        }
    });
}

// Update humidity chart
function updateHumidityChart(data) {
    const ctx = document.getElementById('humidityChart').getContext('2d');
    
    const labels = data.map(d => {
        const date = new Date(d.date);
        return date.toLocaleDateString('it-IT', { day: '2-digit', month: 'short' });
    });
    
    const humidity = data.map(d => d.humidity_avg);
    
    if (humidityChart) humidityChart.destroy();
    
    humidityChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [{
                label: 'Umidità Media (%)',
                data: humidity,
                backgroundColor: 'rgba(54, 162, 235, 0.6)',
                borderColor: 'rgba(54, 162, 235, 1)',
                borderWidth: 1
            }]
        },
        options: {
            ...commonOptions,
            scales: {
                ...commonOptions.scales,
                y: {
                    min: 0,
                    max: 100,
                    title: {
                        display: true,
                        text: 'Umidità (%)'
                    }
                }
            }
        }
    });
}

// Update pressure chart
function updatePressureChart(data) {
    const ctx = document.getElementById('pressureChart').getContext('2d');
    
    const labels = data.map(d => {
        const date = new Date(d.date);
        return date.toLocaleDateString('it-IT', { day: '2-digit', month: 'short' });
    });
    
    const pressure = data.map(d => d.pressure_avg);
    
    if (pressureChart) pressureChart.destroy();
    
    pressureChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: labels,
            datasets: [{
                label: 'Pressione Media (hPa)',
                data: pressure,
                borderColor: '#9b59b6',
                backgroundColor: 'rgba(155, 89, 182, 0.1)',
                tension: 0.4,
                fill: true
            }]
        },
        options: {
            ...commonOptions,
            scales: {
                ...commonOptions.scales,
                y: {
                    title: {
                        display: true,
                        text: 'Pressione (hPa)'
                    }
                }
            }
        }
    });
}

// Update wind chart
function updateWindChart(data) {
    const ctx = document.getElementById('windChart').getContext('2d');
    
    const labels = data.map(d => {
        const date = new Date(d.date);
        return date.toLocaleDateString('it-IT', { day: '2-digit', month: 'short' });
    });
    
    const windMax = data.map(d => d.wind_speed_max);
    const windAvg = data.map(d => d.wind_speed_avg);
    
    if (windChart) windChart.destroy();
    
    windChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: labels,
            datasets: [
                {
                    label: 'Vento Max (m/s)',
                    data: windMax,
                    borderColor: '#e74c3c',
                    backgroundColor: 'rgba(231, 76, 60, 0.1)',
                    tension: 0.4
                },
                {
                    label: 'Vento Medio (m/s)',
                    data: windAvg,
                    borderColor: '#3498db',
                    backgroundColor: 'rgba(52, 152, 219, 0.1)',
                    tension: 0.4
                }
            ]
        },
        options: {
            ...commonOptions,
            scales: {
                ...commonOptions.scales,
                y: {
                    title: {
                        display: true,
                        text: 'Velocità (m/s)'
                    }
                }
            }
        }
    });
}

// Update hourly chart
function updateHourlyChart(data) {
    const ctx = document.getElementById('hourlyChart').getContext('2d');
    
    // Sort by timestamp
    data.sort((a, b) => new Date(a.timestamp) - new Date(b.timestamp));
    
    const labels = data.map(d => {
        const date = new Date(d.timestamp);
        return date.toLocaleTimeString('it-IT', { hour: '2-digit', minute: '2-digit' });
    });
    
    const temperatures = data.map(d => d.temperature);
    const humidity = data.map(d => d.humidity);
    
    if (hourlyChart) hourlyChart.destroy();
    
    hourlyChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: labels,
            datasets: [
                {
                    label: 'Temperatura (°C)',
                    data: temperatures,
                    borderColor: '#ff6b6b',
                    backgroundColor: 'rgba(255, 107, 107, 0.1)',
                    yAxisID: 'y',
                    tension: 0.4
                },
                {
                    label: 'Umidità (%)',
                    data: humidity,
                    borderColor: '#3498db',
                    backgroundColor: 'rgba(52, 152, 219, 0.1)',
                    yAxisID: 'y1',
                    tension: 0.4
                }
            ]
        },
        options: {
            responsive: true,
            maintainAspectRatio: true,
            interaction: {
                mode: 'index',
                intersect: false
            },
            scales: {
                x: {
                    ticks: {
                        maxRotation: 45,
                        minRotation: 45
                    }
                },
                y: {
                    type: 'linear',
                    display: true,
                    position: 'left',
                    title: {
                        display: true,
                        text: 'Temperatura (°C)'
                    }
                },
                y1: {
                    type: 'linear',
                    display: true,
                    position: 'right',
                    min: 0,
                    max: 100,
                    title: {
                        display: true,
                        text: 'Umidità (%)'
                    },
                    grid: {
                        drawOnChartArea: false
                    }
                }
            }
        }
    });
}
