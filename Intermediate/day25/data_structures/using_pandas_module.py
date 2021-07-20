import pandas

data = pandas.read_csv("weather_data.csv")
# print(data["temp"])
temperatures = []
for row in data["temp"]:
    temperature = int(row)
    temperatures.append(temperature)
print("Printing List generated from For Loop")
print(temperatures)

print("\n## Data conversion to a Dictionary ##")
data_dict = data.to_dict()
print(data_dict)

print("\n## Data conversion to a List ##")
data_list = data["day"].to_list()
print(data_list)

# Find average temperature
print("\n ## Average Temperature Check Program ##")
# data_list = data["temp"].to_list()
# average_temperature = sum(data_list) // len(data_list)
# print(f"Average temperature for this week is {average_temperature}")
# OR  "simply this 'mean' method gives the average of the series automatically
average_temperature = round(data["temp"].mean())
print(f"Average temperature for this week is {average_temperature}")

print("\n## Maximum and Minimum temperature check ##")
maximum_temperature = data.temp.max()  # We can use data.temp = data["temp"]
minimum_temperature = data["temp"].min()
# data["temp"] treating like Dictionary
# data.temp treating like Object
print(f"This week's Maximum Temperature is {maximum_temperature} and Minimum Temperatures is {minimum_temperature}")

# Get a row's data from Data
print("\n## Data from a row ##")
print(data[data.day == "Monday"])
print("\n## Row details of maximum temperature ##")
print(data[data.temp == maximum_temperature])  # get the row details of maximum temperature
print("         ##### OR ######")
print(data[data.temp == data.temp.max()])

print("\n## Get Weather Condition of the data Monday ##")
monday = data[data.day == "Monday"]
print("Monday's Weather Condition is " + monday.condition)
monday_temperature = float((monday.temp * 1.8) + 32)
print(f"Monday's Temperature is {monday_temperature}'F")
