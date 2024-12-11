// countySelection.js

document.addEventListener("DOMContentLoaded", function() {
    const apiKey = 'e60f50b1572fc3e577fb812bb7b49154'; // Your OpenWeatherMap API key

    document.getElementById("countySelectionForm").addEventListener("submit", function(event) {
        event.preventDefault(); // Prevent default form submission

        // Get the input value
        var county = document.getElementById('countyInput').value;

        if (county) {
            fetchWeather(county);
        } else {
            alert("Please enter a county name.");
        }
    });

    // Function to fetch weather data
    function fetchWeather(county) {
        var url = `https://api.openweathermap.org/data/2.5/weather?q=${county}&appid=${apiKey}&units=metric`;

        fetch(url)
            .then(response => {
                if (!response.ok) {
                    throw new Error("Weather data not available");
                }
                return response.json();
            })
            .then(data => {
                displayWeather(data);
            })
            .catch(error => {
                console.error("Error fetching weather data: ", error);
                alert("Failed to fetch weather data. Please check the county name.");
            });
    }

    // Function to display weather data
    function displayWeather(data) {
        document.getElementById('weatherInfo').style.display = 'block';
        var description = data.weather[0].description;
        var temperature = data.main.temp + "°C";
        var humidity = "Humidity: " + data.main.humidity + "%";

        document.getElementById('weatherDescription').innerText = "Current weather: " + description;
        document.getElementById('temperature').innerText = "Temperature: " + temperature;
        document.getElementById('humidity').innerText = humidity;
    }
});