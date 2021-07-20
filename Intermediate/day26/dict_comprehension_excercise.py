sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

sentence_list = sentence.split()
result = {word: len(word) for word in sentence_list}
print(result)

print("\n ## Converting Weather from Celsius to Fahrenheit")
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
weather_f = {day: (weather * 9/5) + 32 for (day, weather) in weather_c.items()}
print(weather_f)