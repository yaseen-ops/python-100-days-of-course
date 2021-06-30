weight = int(input("Enter your Height in kg : "))
height = float(input("Enter your Weight in m : "))

bmi = int(weight / height ** 2)
# OR
# bmi = int(weight / (height * height))
print("Your BMI is : " + str(bmi))
