import json

new_data_1 = {
    "Amazon":
        {
            "Mail": "Dummy@gmail.com",
            "Password": "34esd+_)"
        }
}
new_data_2 = {
    "Ebay":
        {
            "Mail": "Dummy@gmail.com",
            "Password": "34esd+_)"
        }
}

# Write a new data
with open("data.json", mode="w") as data_file:
    json.dump(new_data_1, data_file, indent=4)  # Add indent to have a clearly human readable indented formant

# Load the existing data
with open("data.json", "r") as data_file:
    data = json.load(data_file)

# Update the another data
with open("data.json", "w") as data_file:
    data.update(new_data_2)
    json.dump(data, data_file, indent=4)
