import requests
from dotenv import load_dotenv
import os
from pprint import pprint

# Load environment variables from the .env file (if present)
load_dotenv()

def get_current_weather():
    ## Access environment variables as if they came from the actual environment
    API_KEY = os.getenv("API_KEY")

    print('\n*** Get current weather conditions ***\n')

    city = input("\nPlease enter a city name:\n")

    request_url = f'https://api.openweathermap.org/data/2.5/weather?appid={API_KEY}&q={city}&units=imperial'

    print(request_url)
    weather_data = requests.get(request_url).json()

    #Accessing json data
    print(f'\nCurrent weather for {weather_data["name"]}')
    print(f'\nThe temperature is {weather_data["main"]["temp"]}')
    print(f'\nFeels like {weather_data["main"]["feels_like"]} and {weather_data["weather"][0]["description"]}.')

    pprint(weather_data)

    
if __name__ == "__main__":
    get_current_weather()