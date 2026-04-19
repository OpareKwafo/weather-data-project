🌤️ OpenWeather CLI Tool

A simple Python command-line application that fetches real-time weather data using the OpenWeather API. This project demonstrates how to work with REST APIs, handle JSON data, and build CLI tools in Python.

🚀 Features
Get current weather for any city
Supports multi-word city names (e.g., "San Francisco")
Displays:
Temperature (°C)
Feels-like temperature
Weather description
Humidity
Wind speed
Saves clean, structured weather data to a file (optional)
Secure API key handling using environment variables
🛠️ Tech Stack
Python 3
Requests library
OpenWeather API
python-dotenv (for environment variables)
📦 Installation
1. Clone the repository
git clone https://github.com/yourusername/openweather-cli.git
cd openweather-cli
2. Install dependencies
pip install requests python-dotenv
3. Create a .env file

In the project root, create a .env file:

OPENWEATHER_API_KEY=your_api_key_here
▶️ Usage

Run the script from the terminal:

python weather.py "City Name" COUNTRY_CODE
Example:
python weather.py "San Francisco" US
📊 Example Output
City: San Francisco
Temperature: 16.7°C
Feels Like: 15.2°C
Condition: broken clouds
Humidity: 72%
Wind Speed: 5.1 m/s
🔐 API Key Security

This project uses environment variables to protect sensitive data.

API keys are stored in a .env file
.env is excluded from version control using .gitignore

⚠️ Never hardcode API keys in your source code.

📁 Project Structure
openweather-cli/
│
├── weather.py
├── .env
├── .gitignore
└── README.md
🌐 API Reference

This project uses the OpenWeather Current Weather API:

https://api.openweathermap.org/data/2.5/weather

More info: https://openweathermap.org/api

📚 What I Learned
Working with REST APIs in Python
Parsing JSON responses
Handling command-line arguments (sys.argv)
Securing API keys using environment variables
Structuring small Python CLI tools
🚀 Future Improvements
Add 5-day weather forecast support
Improve error handling (invalid city, API failures)
Add unit conversion (Celsius ↔ Fahrenheit toggle)
Build a nicer CLI interface using argparse
Export weather history to CSV
🧑‍💻 Author

Built as a Python practice project for learning API integration and CLI tool development.