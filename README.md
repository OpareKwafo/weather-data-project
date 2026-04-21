# 🌤️ OpenWeather CLI Tool (Python)

A simple Python command-line application that fetches real-time weather data using the OpenWeather API.  
This project is built for learning how to work with REST APIs, JSON data, and secure API key handling in Python.

---

## 🚀 Features

- Get current weather for any city in the world
- Supports multi-word city names (e.g. "San Francisco")
- Displays:
  - Temperature (°C)
  - Feels-like temperature
  - Weather description
  - Humidity
  - Wind speed
- Clean and structured output
- Uses secure environment variables for API keys

---

## 🛠️ Tech Stack

- Python 3
- requests library
- OpenWeather API
- python-dotenv (for environment variables)

---

## Installation

### 1. Clone the repository

### 2. Install Dependencies

### 3. Create a .env file

## ▶️ Usage

## 🔐 Security Notice

- API keys are stored in .env
- .env is excluded via .gitignore
- Never commit secrets to GitHub

## API Reference

https://api.openweathermap.org/data/2.5/weather
https://openweathermap.org/api

## 📁 Project Structure

weather-cli/
│
├── weather.py
├── .env
├── .gitignore
└── README.md

## 📚 What I Learned

- REST APIs in Python
- JSON parsing
- CLI argument handling (sys.argv)
- Environment variables
- Secure coding practices

🚀 Future Improvements

- 5-day forecast support
- Better error handling
- argparse CLI interface
- Unit conversion (°C / °F)
- Save weather history

🧑‍💻 Author

Built as a Python practice project for API integration and CLI development.






