south_india = ["Tamil Nadu", "Kerala", "Telungana"]

print(south_india)
print(south_india[0])

south_india[2] = "Andhra Pradesh"   # Updates the index number equivalent value
print(south_india)

south_india.append("Karnataka")  # Appends an item at the end
print(south_india)

print("Removed the State : " + south_india.pop())  # Removes the last item in the list

south_india.extend(["Kerala", "Karnatka"])   # Extend the list with this list of values
print(south_india)
print("Total count : " + str(south_india.count("Kerala")))  # Count the number of occurrences of State Kerala in the list


