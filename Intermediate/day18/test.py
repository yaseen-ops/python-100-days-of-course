
def add_time(start, duration, *args):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    pa = 0
    piss2 = []
    number_of_days = len(days)

    for piss in args:
        piss2.append(piss)

    for day in days:
        if piss2[0] == day:
            day_to_check = pa + 2
            if day_to_check > number_of_days - 1:
                day_to_check = day_to_check - number_of_days
            print(days[day_to_check])
        pa += 1


add_time("2:59 AM", "24:00", "Saturday")