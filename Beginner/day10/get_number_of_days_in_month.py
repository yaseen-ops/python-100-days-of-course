
def is_leap(check_year):
    if year % 4 == 0:
        if year % 100 != 0:
            return True
        elif year % 400 == 0:
            return True
        else:
            return False
    else:
        return False


def days_in_month(check_year, check_month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if check_month > 12 or check_month < 1:
        return "Invalid Month Entered!"
    # My idea of code
    if is_leap(check_year):
        month_days[1] += 1
    # OR # COURSE CODE
    # Below one is somewhat better, because it only checks when user enter 'month 2'
    # But above one always checks for leap year and +1 number of days in Feb month
    # if check_month == 2 and is_leap(check_year):
    #     return 29
    number_of_days = month_days[check_month - 1]
    return number_of_days


year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
