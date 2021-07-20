class Bike:

    def bike_from_india(self):
        print("Bikes from India")

    def bike_from_pakistan(self):
        print("Bikes from India")


# class BikeFromUK(Bike):  # Inheriting Class Bike, so that Class BikefromUK can access Class Bike
class BikeFromUK:

    def bike_from_london(self):
        print("Bikes form London")

    def bike_from_birmingham(self):
        print("Bikes from Birmingham")


# class BikeFromEurope(BikeFromUK): # Can access Class BikeFromUK & Class Bike if Class BikeFromUK
# Inherits Class Bike else only inherits Class BikeFromUk
class BikeFromEurope(Bike, BikeFromUK):  # Can Separately inherits both the Classes

    def bike_from_spain(self):
        print("Bikes from spain")

    def bike_from_italy(self):
        print("Bikes from italy")


bike1 = Bike()
bike2 = BikeFromUK()
bike3 = BikeFromEurope()
bike3.bike_from_india()
