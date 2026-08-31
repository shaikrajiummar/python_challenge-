def get_weather_report(temperature):
    # Complete this function
    if temperature < 22:
        return "Cold"
    elif 22 <= temperature < 35:
        return "Warm"
    else:
        return "Hot"


temperature = int(input())
# Call the get_weather_report function
result = get_weather_report(temperature)
print(result)