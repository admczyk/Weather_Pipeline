import requests
import json

def fetch_past_weather_data(latitude, longitude, past_days) -> dict:
    url = (
        "https://api.open-meteo.com/v1/forecast"
        f"?latitude={latitude}"
        f"&longitude={longitude}"
        "&daily="
            "weather_code,"
            "temperature_2m_max,temperature_2m_min,"
            "apparent_temperature_max,apparent_temperature_min,"
            "daylight_duration,"
            "sunset,sunrise,"
            "uv_index_max,"
            "rain_sum,snowfall_sum,"
            "wind_speed_10m_max,"
            "sunshine_duration"
        f"&past_days={past_days}"
        "&forecast_days=0"
        )
    response = requests.get(url)

    #TUTAJ TRZEBA DODAĆ ERROR HANDLING
    try:
        weather_data = response.json()
        return weather_data
    except:
        print("Boo hoo")
        pass

def fetch_weather_forecast_data(latitude, longitude, forecast_days) -> dict:
    url = (
        "https://api.open-meteo.com/v1/forecast"
        f"?latitude={latitude}"
        f"&longitude={longitude}"
        "&daily="
            "weather_code,"
            "temperature_2m_max,temperature_2m_min,"
            "apparent_temperature_max,apparent_temperature_min,"
            "daylight_duration,"
            "sunset,sunrise,"
            "uv_index_max,"
            "rain_sum,snowfall_sum,"
            "wind_speed_10m_max,"
            "sunshine_duration"
        f"&forecast_days={forecast_days}"
        )
    response = requests.get(url)

    #TUTAJ TRZEBA DODAĆ ERROR HANDLING
    try:
        weather_data = response.json()
        return weather_data
    except:
        print("Boo hoo")
        pass

def main():
    #ZAPISUJE DANE DO PLIKU JSON
    with open("./src/past_weather_data.json", "w") as file:
        json.dump(fetch_past_weather_data(52.52, 13.41, 92), file, indent=4)

    with open("./src/weather_forecast_data.json", "w") as file:
        json.dump(fetch_weather_forecast_data(52.52, 13.41, 92), file, indent=4)

if __name__ == "__main__":
    main()