def format_name(f_name, l_name):
    # In case user haven't provided any input, check with if condition
    # If user hasn't provided input for f_name or l_name, the function will be exited by "return"
    if f_name == "" or l_name == "":
        return "You haven't provided enough information"
    first_name = f_name.title()
    last_name = l_name.title()
    return f"{first_name} {last_name}"


name = format_name(f_name=input("Enter your first name : "), l_name=input("Enter your last name : "))

print(name)