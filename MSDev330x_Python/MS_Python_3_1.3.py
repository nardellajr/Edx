from datetime import timedelta, datetime, date


def datestuff():

    delta1 = timedelta(days=2, seconds=0, minutes=15, hours=1, weeks=4)
    print(delta1, "is stored in delta1")
    # 30 days, 1:15:00 is stored in delta1

    d = delta1.days
    s = delta1.seconds
    ms = delta1.microseconds
    print(f"Days = {d} | Seconds = {s} | Microseconds = ms")
    # Days = 30 | Seconds = 4500 | Microseconds = ms

    # Notice seconds, returns the total seconds (hours + minutes).
    #
    #  We could use total_seconds(), which return all of the time in seconds.
    # Could use this to calculate the difference between 2 dates.
    all_seconds = delta1.total_seconds()
    print(f"Total number of seconds = {all_seconds}")

    date1 = datetime(year=2015, month=1, day=19)
    date2 = datetime.today()

    delta2 = date2 - date1

    # 1097 days, 18:43:08.218576 is stored in delta2
    print(f"{delta2} is stored in delta2")
    print("Total number of seconds = ", delta2.total_seconds())
    # Total number of seconds =  94848188.218576


    onehundred_days = timedelta(days=100)
    current_date = datetime(day=15, month=4, year=2019)

    new_date = current_date + onehundred_days

    # 100 days after 2019-04-15 00:00:00 is Jul/24/2019
    print(f"100 days after {current_date} is {new_date.strftime('%b/%d/%Y')}")

    twohundred_days = onehundred_days * 2
    threehundred_days = onehundred_days * 3

    current_date = datetime.today()

    new_date1 = current_date + twohundred_days
    new_date2 = current_date + threehundred_days

    print(f"After 200 days: {new_date1.strftime('%b/%d/%Y')}")
    print(f"After 300 days: {new_date2.strftime('%b/%d/%Y')}")

    # After 200 days: Aug/08/2018
    # After 300 days: Nov/16/2018

    birthday1 = date(year=1993, month=3, day=5)
    birthday2 = date(year=2003, month=3, day=20)

    if birthday1 > birthday2:
        print("Person 2 is older")
    elif birthday1 < birthday2:
        print("Person 1 is older")
    else:
        print("Person 1 and Person 2 are of the same age")

    print(birthday1 == birthday2)

    now = datetime(month=1, day=20, year=2018)
    solstice = datetime(month=12, day=21, year=1)
    solstice = solstice.replace(year=now.year)

    count = solstice - now

    print(f"Count is type {type(count)}")
    # Count is type <class 'datetime.timedelta'>
    print(f"There are only {count.days} days till December solstice!")

    print(date(year=2018, month=11, day=7))
    h = date(year=2018, month=7, day=1)
    print(h)


if __name__ == '__main__':
    datestuff()
