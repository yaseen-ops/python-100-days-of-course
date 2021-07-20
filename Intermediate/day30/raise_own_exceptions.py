
height = float(input("Height: "))
weight = float(input("Weight: "))

# Here i can give any value to height which is beyond natural height of any human
# To track this we can raise our own exceptions
if height > 3:
    raise ValueError("Human height shouldn't be over 3 meters")

bmi = weight / (height ** 2)

print(round(bmi, 2))
