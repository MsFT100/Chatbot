
import requests

def get_bot_weather(city):
    api_key = "247e5b7538be25746d4566ba53a94f45"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    response = requests.get(url)
    data = response.json()

    if data["cod"] == "404":
        return "City not found. Please check your spelling."
    else:
        weather = data["weather"][0]["description"]
        return weather
def get_weather(city):
    api_key = "247e5b7538be25746d4566ba53a94f45"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    response = requests.get(url)
    data = response.json()

    if data["cod"] == "404":
        return "City not found. Please check your spelling."
    else:
        weather = data["weather"][0]["description"]
        return f"The weather in {city} is currently {weather}."

if __name__ == "__main__":
    city = input("Enter a city name: ")
    result = get_weather(city)
    print(result)
