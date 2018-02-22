from random import randint
# from random import choice
from datetime import time
from datetime import date
from datetime import datetime


def odd_random():
    odd = randint(1, 6)
    while odd % 2 != 1:   # 5 % 2 = 1
        odd = randint(1, 6)

    return odd


def checktime():
    # 24 hour time
    # Time is 8:55:20.000500 PM
    t = time(20, 55, 20, 500)
    print(t)
    # Better to show the labels, more readable
    t = time(minute=10, hour=9, microsecond=900000, second=30)
    print(t)

    # attributes not set, will default to 0

    t = time(hour=1, minute=5)
    print(t)

    t = time(hour=9, minute=10, second=43, microsecond=100)

    h = t.hour
    m = t.minute
    s = t.second
    ms = t.microsecond

    print(f"The time is: {h} hours, {m} minutes, {s} seconds, {ms} microseconds")

    t = t.replace(hour=10, minute=39)

    print(f"New time {t}")


def checkdate():
    date1 = date(2013, 5, 7)
    print(date1)

    date2 = date(day=23, month=4, year=1999)
    print(date2)

    specialDate = date(year=2017, month=12, day=23)

    y = specialDate.year
    m = specialDate.month
    d = specialDate.day

    print(f"The special Date is: / month {m}: / day: {d}, / year: {y}")

    specialDate = specialDate.replace(year=2016, day=29)

    print(f"New date: {specialDate}")

    # Get local time from computer
    d = date.today()
    print(d)

    dt = datetime(2022, 7, 1, 16, 30)
    print(dt)
    dt = datetime(day=1, month=12, hour=6, minute=23, second=1, year=2018, microsecond=20)
    print(dt)

    print("Year is: ", dt.year)
    print("Minute is: ", dt.minute)

    dt = dt.replace(year=2035, second=30)
    print(dt)

    dt = datetime.today()
    print(dt)
    t = dt.time()
    print("Time is: ", t)
    d = dt.date()
    print("Date is: ", d)

    t = time(hour=6, minute=45, second=0)
    d = date.today()

    dt = datetime.combine(date=d, time=t)
    print("Combined Date and Time: ", dt)

    t = time(hour=10, minute=15)

    formatted_string = t.strftime("%I:%M %p") # %I - 12 hours clock, %M minutes, %p AM/PM
    print(formatted_string)

    d = date(year=1999, month=11, day=3)
    formatted_string = d.strftime("%B, %d, %Y")
    print("First format: ", formatted_string)
    # First format:  November, 03, 1999
    formatted_string = d.strftime("%b, %d, %y")
    print(formatted_string)
    # Nov, 03, 99

    dt = datetime(year=1999, month=11, day=3, hour=10, minute=15)
    formatted_string = dt.strftime("%B, %d, %Y @ %I:%M %p")
    print(formatted_string)
    # November, 03, 1999 @ 10:15 AM

    # TypeError: year is required
    #mydt = datetime(month=10, day=24)
    #print(mydt)


if __name__ == '__main__':
    print(odd_random())
    checktime()
    checkdate()

