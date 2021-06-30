def greet():
    print("Hello Coder")
    print("How do you doing , Coder?")


greet()

# Function with Input
def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you doing, {name}?")


greet_with_name("Cyber Coder")


# Function with multiple inputs
def greet_with_name_location(name, location):
    print(f"Hello {name}")
    print(f"How is weather in {location}?")

greet_with_name_location("Coder", "Chennai")

# changing input data order
def greet_with_name_location(name, location):
    print(f"Hello {name}")
    print(f"How is weather in {location}?")

greet_with_name_location("Chennai", "Coder")

# We can assign the parameter value directly in the function call
def greet_with_name_location(name, location):
    print(f"Hello {name}")
    print(f"How is weather in {location}?")

greet_with_name_location(location="Chennai", name="Coder")