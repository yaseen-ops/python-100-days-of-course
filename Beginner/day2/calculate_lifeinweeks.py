age = int(input("Enter you age : "))

total_years = 90
days_in_a_year = 365
weeks_in_a_year = 52
months_in_a_year = 12

remaining_years = total_years - age
days_left = remaining_years * days_in_a_year
weeks_left = remaining_years * weeks_in_a_year
months_left = remaining_years * months_in_a_year

result = f"You have {days_left} days, {weeks_left} weeks and {months_left} months left"
print(result)