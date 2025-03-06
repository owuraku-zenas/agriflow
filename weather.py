import pyowm


def get_weather():
    API_KEY = "d5a14bc32497c6fb5b9605506a10ab2d"

    owm = pyowm.OWM(API_KEY)  # Initialize with your API key

    mgr = owm.weather_manager()
    observation = mgr.weather_at_place("Accra")

    w = observation.weather  # Corrected way to access the weather data

    print(w.detailed_status)         # 'clouds'
    print(w.wind())                  # {'speed': 4.6, 'deg': 330}
    print(w.humidity)                # 87
    print(w.temperature('celsius'))  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
    print(w.rain)                    # {}
    print(w.heat_index)              # None
    print(w.clouds)

    return {
        "detailed_status": w.detailed_status,
        "wind": w.wind(),
        "humidity": w.humidity,
        "temperature": w.temperature('celsius'),
        "rain": w.rain,
        "heat_index": w.heat_index,
        "clouds": w.clouds
    }
