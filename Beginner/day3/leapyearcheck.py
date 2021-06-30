year = int(input("Which year you want to check? \n"))

if year % 4 == 0:
    if year % 100 != 0:
        print(f"Year {year} is a Leap Year")
    elif year % 400 == 0:
        print(f"Year {year} is a Leap Year")
    else:
        print(f"Year {year} is not a Leap Year")
else:
    print(f"Year {year} is not a Leap Year")
