import requests

def get_weather_data(place, apiKey):
    apiUrl = f"http://api.openweathermap.org/data/2.5/weather?q={place}&appid={apiKey}&units=metric"
    try:
        response = requests.get(apiUrl)

        if response.status_code == 200: 
            weather = response.json()['weather'][0]['main']
            temperature = response.json()['main']['temp']
            description = response.json()['weather'][0]['description']
            humidity = response.json()['main']['humidity']
            wind = response.json()['wind']['speed']

            print(f"Weather in {place}:")
            print(f"Condition: {weather}")
            print(f"Temperature: {temperature}°C")
            print(f"Description: {description}")
            print(f"Humidity: {humidity}%")
            print(f"Wind Speed: {wind} m/s")

        else: 
            print("Error: Unable to fetch weather data. Please check the city name and API key.")
            exit()

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        exit()


if __name__ == "__main__":

    print("WEATHER REPORT!")
    print("This app provides current weather information for any city using the OpenWeatherMap API.")
    place = input ("Insert city name: ")
    apiKey = input ("Insert your API key (https://openweathermap.org/api): ")

    get_weather_data(place, apiKey)