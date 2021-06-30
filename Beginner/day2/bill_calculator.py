print("Welcome to the bill calculator")

bill_amount = float(input("What was the total bill? $"))
tip_percentage = float(input("What percentage tip you would like to give? "))
number_people = int(input("How many people to split the bill? "))

tip_amount = tip_percentage / 100 * bill_amount
total_bill_amount = bill_amount + tip_amount
bill_per_person = total_bill_amount / number_people
# final_amount = round(bill_per_person, 2)
# This will add zeros to the decimal value if there isn't any where round function doesn't do
final_amount = "{:.2f}".format(total_bill_amount)
print(f"Each person should pay : ${final_amount}")
