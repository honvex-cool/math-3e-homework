#!/usr/bin/python3

import random

RAIN_PROBABILITY = 0.1
FORECAST_ACCURACY = 2 / 3
UMBRELLA_PROBABILITY = (1, 1.0 / 3.0)

def decision(probability):
    return random.random() < probability

def is_raining():
    return decision(RAIN_PROBABILITY)

def forecast(actual):
    return actual if decision(FORECAST_ACCURACY) else not actual

def simulate_mismatches(n):
    rainy_days = 0
    sunny_days = 0
    lacking_umbrella_days = 0
    unnecessary_umbrella_days = 0
    for i in range(n):
        rain = is_raining()
        expected_rain = forecast(rain)
        umbrella = decision(UMBRELLA_PROBABILITY[int(not expected_rain)])
        if rain:
            rainy_days += 1
            if not umbrella:
                lacking_umbrella_days += 1
        else:
            sunny_days += 1
            if umbrella:
                unnecessary_umbrella_days += 1
    return lacking_umbrella_days / rainy_days, unnecessary_umbrella_days / sunny_days

days = int(input("How many days to simulate: "))

lacking, unnecessary = simulate_mismatches(days)

print(f"Lacking umbrella probability {lacking}")
print(f"Unnecessary umbrella probability {unnecessary}")

