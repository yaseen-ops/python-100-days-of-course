# Simple Dictionary
capitals = {
    "India": "Delhi",
    "Bangladesh": "Dhaka",
}

# Nesting list in a dictionary
travel_log = {
    "India": ["Chennai", "Mumbai", "Kerala"],
    "US": ["Texas", "Florida", "California"]
}

print(travel_log["India"][2])


# Nesting Dictionary in a dictionary
travel_log = {
    "India": {
        "cities_visited": ["Chennai", "Mumbai", "Kerala"],
        "total_visits": 13,
    },
    "Pakistan": ["Lahore", "Peshawar"],
    "US": {
        "cities_visited": ["Texas", "Florida", "California"],
        "total_visits": 9,
    },
}
print(travel_log["India"]["cities_visited"][1])
print(travel_log["India"]["total_visits"])
print(travel_log["Pakistan"])
print(travel_log["US"]["cities_visited"][0])


# Nesting Dictionaries in a List
travel_log = [
    {
        "country": "India",
        "cities_visited": ["Chennai", "Mumbai", "Kerala"],
        "total_visits": 13,
    },
    {
        "country": "US",
        "cities_visited": ["Texas", "Florida", "California"],
        "total_visits": 9,
    },
]
print(travel_log[1]["country"])
