import requests

API_KEY = "Enter API KEY"  # Get from https://openweathermap.org/
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    try:
        params = {
            "q": city,
            "appid": API_KEY,
            "units": "metric"
        }

        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if response.status_code == 200:
            print(f"\nWeather in {city}:")
            print(f"Temperature: {data['main']['temp']}°C")
            print(f"Humidity: {data['main']['humidity']}%")
            print(f"Condition: {data['weather'][0]['description']}")
        else:
            print("City not found!")

    except Exception as e:
        print("Error:", e)

city = input("Enter city name: ").strip()
get_weather(city)
