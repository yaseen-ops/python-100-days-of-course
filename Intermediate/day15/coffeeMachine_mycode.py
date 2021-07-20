from data import MENU, resources


def is_resource_sufficient(coffee):
    """Check if resources availability is sufficient to make a coffee"""
    water_left = resources["water"]
    required_water = MENU[coffee]["ingredients"]["water"]
    coffee_left = resources["coffee"]
    required_coffee = MENU[coffee]["ingredients"]["coffee"]
    if coffee != "espresso":
        milk_left = resources["milk"]
        required_milk = MENU[coffee]["ingredients"]["milk"]
        if required_milk > milk_left:
            print("sorry there is not enough milk")
            return False
    if required_water > water_left:
        print("sorry there is not enough water")
        return False
    elif required_coffee > coffee_left:
        print("sorry there is not enough coffee")
        return False
    else:
        return True


def payment_process(coffee, quarters, dimes, nickles, pennies):
    """Payment, balance and profit generate"""
    coffee_price = MENU[coffee]["cost"]
    amount_paid = round((quarters / 4) + (dimes / 10) + (nickles / 20) + (pennies / 100), 2)
    # OR
    # amount_paid = round((quarters * 0.25) + (dimes * 0.1) + (nickles * 0.05) + (pennies * 0.01), 2)
    user_balance = round(amount_paid - coffee_price, 2)
    if amount_paid < coffee_price:
        print("Sorry that's not enough money, Given Money refunded")
        return False
    else:
        global profit
        profit += coffee_price
        print(f"Here is your ☕️{coffee} Enjoy")
        print(f"Here is your ${user_balance} in change")
        return True


def deduct_resource(coffee):
    """update the resource whenever a coffee made"""
    resources["water"] = resources["water"] - MENU[coffee]["ingredients"]["water"]
    resources["coffee"] = resources["coffee"] - MENU[coffee]["ingredients"]["coffee"]
    if coffee != "espresso":
        resources["milk"] = resources["milk"] - MENU[coffee]["ingredients"]["milk"]


def refill_machine():
    """refill the resources"""
    resources["water"] = 800
    resources["coffee"] = 150
    resources["milk"] = 500


def make_coffee():
    """Coffee Machine which makes the coffee"""
    switch_off_machine = False
    while not switch_off_machine:

        user_choice = input("What would you like? (espresso/latte/cappuccino) : ")

        if user_choice.lower() == "off":
            switch_off_machine = True
            continue
        elif user_choice.lower() == "report":
            print(f'Water : {resources["water"]}ml')
            print(f'Milk : {resources["milk"]}ml')
            print(f'Coffee : {resources["coffee"]}g')
            print(f"Money : ${profit}")
            continue
        elif user_choice.lower() == "refill":
            refill_machine()
            continue
        else:
            print("Please insert coins")
            quarters = int(input("how many quarters?: "))
            dimes = int(input("how many dimes?: "))
            nickles = int(input("how many nickles?: "))
            pennies = int(input("how many pennies?: "))

            if is_resource_sufficient(user_choice):
                if payment_process(user_choice, quarters, dimes, nickles, pennies):
                    deduct_resource(user_choice)


profit = 0
make_coffee()
