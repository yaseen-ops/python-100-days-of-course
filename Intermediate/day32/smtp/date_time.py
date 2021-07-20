import datetime as dt

now = dt.datetime.now()
print(now.day)
print(now.year)
print(now.weekday())

date_of_birth = dt.datetime(year=2018, month=9, day=19)
print(date_of_birth)