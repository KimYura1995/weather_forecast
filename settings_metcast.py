# -*- coding: utf-8 -*-
import os

API_KEY_METCAST = "07744e9e-b409-450e-a3cd-6afa092d1586"
API_KEY_GEO = "b5d78a68-cd6c-4a73-9b40-6396c4c776e9"

PARAMS_GEO = {
    "apikey": API_KEY_GEO,
    "geocode": None,
    "format": "json",
    "lang": "ru_RU"
}

PARAMS_METCAST = {
    "lat": None,
    "lon": None,
    "limit": "7",
    "hours": "false",
    "format": "json",
    "lang": "ru_RU"
}

HEADER_METCAST = {
    "X-Yandex-API-Key": API_KEY_METCAST
}

CONDITION_SET = {
    ("clear",): "Солнечно",
    ("partly-cloudy", "cloudy", "overcast",): "Облачно",
    ("drizzle", "light-rain", "rain",
     "moderate-rain", "heavy-rain",
     "continuous-heavy-rain", "showers",
     "thunderstorm", "thunderstorm-with-rain",
     "thunderstorm-with-hail"): "Дождь",
    ("wet-snow", "light-snow", "snow",
     "snow-showers", "hail"): "Снег"
}

# В формате BGR
COLOR_SET = {
    "Солнечно": {
        "color1": (0, 255, 255),
        "color2": (255, 255, 255)
    },
    "Дождь": {
        "color1": (255, 0, 0),
        "color2": (255, 255, 255)
    },
    "Снег": {
        "color1": (255, 205, 0),
        "color2": (255, 255, 255)
    },
    "Облачно": {
        "color1": (100, 100, 100),
        "color2": (255, 255, 255)
    },
}

IMAGE_SET = {
    "Солнечно": os.path.join("weather_source_img", "sun.png"),
    "Дождь": os.path.join("weather_source_img", "rain.png"),
    "Снег": os.path.join("weather_source_img", "snow.png"),
    "Облачно": os.path.join("weather_source_img", "cloud.png")
}
