# # creating a list by reading the data from "weather_data.csv", then adding all the lines to a new file
# with open("weather_data.csv") as data_file:
#     data_list = data_file.readlines()
#     for line in data_list:
#         # stripped_line = line.strip()
#         with open("data_file.csv", mode="a") as new_data_file:
#             new_data_file.write(line)

import csv
with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)   # now data is an object with each line as a list
    # for row in data:
    #     print(row)
    # """
    # Output:
    # ['day', 'temp', 'condition']
    # ['Monday', '12', 'Sunny']
    # ['Tuesday', '14', 'Rain']
    # ['Wednesday', '15', 'Rain']
    # ['Thursday', '14', 'Cloudy']
    # ['Friday', '21', 'Sunny']
    # ['Saturday', '22', 'Sunny']
    # ['Sunday', '24', 'Sunny']
    # """
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperature = int(row[1])
            temperatures.append(temperature)
    print(temperatures)
