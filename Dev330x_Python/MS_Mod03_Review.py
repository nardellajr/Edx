import os
import datetime
import sys


def errortypes():
    try:
        # SyntaxError
        # print(exec("if w in q:"))
        # SyntaxError unexpected EOF while parsing (<string>, line 1)

        # ValueError
        # print(float("mike"))
        # Created ValueError could not convert string to float: 'mike'

        # TypeError
        stuff = ""
        stuff.count(1)
        # Created TypeError must be str, not int

    except SyntaxError as exception_object:
        print("SyntaxError", exception_object)
    except TypeError as exception_object:
        print("Created TypeError", exception_object)
    except ValueError as exception_object:
        print("Created ValueError", exception_object)


def handlingexceptions():
    lst = [8, 85.4, [55, 4], 'word', (59,), {2: 43.5}]

    try:
        x = input("Enter a number: ")
        x = float(x)

        for i in range(7):
            print("{} / {:.2f} = {:.2f}".format(lst[i], x, lst[i] / x))

    except TypeError as exception_object:
        print("Error with:", x, exception_object)
    except ValueError as exception_object:
        print(x, "is not a float", exception_object)
    except ZeroDivisionError as exception_object:
        print("Cannot divide by zero", exception_object)

    print("Done!")


def fileexceptionhandling():
    print(os.getcwd())

    # ask user for a file name
    fname = input("Enter file name: ")
    f = None
    try:
        # the file should be located in `parent_dir`
        fname = os.path.join(os.getcwd(), "parent_dir", fname)

        # opening text_file.txt for reading
        f = open(fname, 'r')
        print(f.readline())
        f.close()

    except Exception as exception_object:
        print("Unexpected exception", exception_object)
    finally:
        if f != None and not f.close():
            f.close()


def findnum(x):
    valid_nums = (1, 2, 8, 16, 32, 64)

    while x not in valid_nums:

        try:
            x = int(input("Please enter a number: "))
            print(x)
        except ValueError as exception_object:
            print("Oops! That was no valid number. Try again...")

    print("You guessed the number!")


def add_rainy(weather):

    for key, info in weather.items():
        rainy = False
        if float(info[2]) > 0.0:
            rainy = True

        info.append(rainy)
        weather[key] = info


def consolidate(weather):
    """
    Consolidate the daily weather information by year.

    Use the weather dictionary to generate a new consolidated dictionary (yearly_weather).
    The new dictionary uses years as keys, and the associated values are lists containing (in order):
        1) The average of the highest recorded temperatures in the year (AVG_TMAX)
        2) The average of the lowest recorded temperatures in the year (AVG_TMIN)
        3) The total recorded precipitation in the year (TOTAL_PRCP)
        4) The total number of rainy days in the year (TOTAL_RAINY_DAYS)
        5) The number of recorded days (TOTAL_DAYS).
           This element is necessary to account for days where the station breaks (missing recordings),
           or if the year hasn't finished yet.

    args:
        weather: dictionary, keys are date objects and values are lists [TMAX, TMIN, PRCP, RAINY_DAY]

    returns:
        yearly_weather: consolidated dictionary, keys are years (int), values are lists
                        [AVG_TMAX, AVG_TMIN, TOTAL_PRCP, TOTAL_RAINY_DAYS, TOTAL_DAYS]
    """
    yearly = {}
    totalrecordcount = 0
    processingyear = 0
    yearrecordcount = 0
    for key, value in sorted(weather.items()):
        totalrecordcount += 1
        d = key
        if d.year != processingyear:
            if processingyear != 0:
                # cal averages
                yearly[processingyear] = [total_tmax / yearrecordcount, total_tmin / yearrecordcount,
                                  total_precp / yearrecordcount,
                                  total_rainy, yearrecordcount]
            processingyear = d.year
            # reset total & count variables
            yearrecordcount = 0
            total_tmax = 0
            total_tmin = 0
            total_precp = 0
            total_rainy = 0

        yearrecordcount += 1
        total_tmax += value[0]
        total_tmin += value[1]
        total_precp += value[2]
        if value[3]:
            total_rainy += 1

        if totalrecordcount == len(weather):
            # cal averages
            yearly[processingyear] = [total_tmax / yearrecordcount, total_tmin / yearrecordcount,
                              total_precp / yearrecordcount,
                              total_rainy, yearrecordcount]

    return yearly


def Hottestyear(weather):

    # Returns key for max value for 1st item in value list, in this case it is temp
    maxtemp = max(weather1.keys(), key=lambda k: weather1[k])
    print(maxtemp.year)

    print(type(max(weather.values())[0]))

    # return the item 0 in the value list
    max_val = max(weather1.values())[0]
    print(type(max_val))

    keys = (k for k, v in weather1.items() if v[0] >= max_val)
    print(keys)

    # 2nd item in value list is the min temp. This isn't returning the correct value
    # It is looking at the first item in the value list
    min_val = min(weather1.values())
    print(min_val)


def coldest(weather):
    mintemp_year = ()
    coldest = sys.maxsize
    for k, v in weather.items():
        if v[1] < coldest:
            coldest = v[1]
            mintemp_year = v[1], k.year

    print(mintemp_year[1])


def rainiest_day(weather):
    rainiest_info = ()
    raindays = 0
    for k, v in weather.items():
        if v[2] > raindays:
            raindays = v[2]
            rainiest_info = v[2], k.year

    print(rainiest_info[1])


if __name__ == '__main__':
    weather1 = {datetime.date(1948, 1, 1): [51, 42, 0.47], datetime.date(1951, 1, 2): [45, 36, 0.59],
               datetime.date(1948, 1, 3): [45, 35, 0.42], datetime.date(1951, 1, 4): [45, 34, 0.31],
               datetime.date(1948, 1, 5): [45, 32, 0.17], datetime.date(1951, 1, 6): [48, 39, 0.44],
               datetime.date(1948, 1, 7): [50, 40, 0.41], datetime.date(1951, 1, 8): [48, 35, 0.04],
               datetime.date(1948, 1, 9): [50, 31, 0.12], datetime.date(1951, 1, 10): [43, 34, 0.74],
               datetime.date(1949, 1, 11): [42, 32, 0.01], datetime.date(1952, 1, 12): [41, 26, 0.0],
               datetime.date(1949, 1, 13): [45, 29, 0.0], datetime.date(1952, 1, 14): [38, 26, 0.0],
               datetime.date(1949, 1, 15): [34, 31, 0.0], datetime.date(1952, 1, 16): [34, 28, 0.0],
               datetime.date(1949, 1, 17): [35, 29, 0.0], datetime.date(1952, 1, 18): [33, 28, 0.0],
               datetime.date(1949, 1, 19): [34, 27, 0.0], datetime.date(1952, 1, 20): [36, 29, 0.0],
               datetime.date(1950, 1, 21): [48, 32, 0.0], datetime.date(1953, 1, 22): [47, 44, 0.21],
               datetime.date(1950, 1, 23): [47, 43, 0.0], datetime.date(1953, 1, 24): [45, 34, 0.1],
               datetime.date(1950, 1, 25): [46, 30, 0.0], datetime.date(1953, 1, 26): [45, 32, 0.0],
               datetime.date(1950, 1, 27): [53, 33, 0.0], datetime.date(1953, 1, 28): [53, 30, 0.0],
               datetime.date(1950, 1, 29): [42, 34, 0.22]}

    weather = {datetime.date(1948, 1, 1): [51, 42, 0.47, True], datetime.date(1951, 1, 2): [45, 36, 0.59, True],
               datetime.date(1948, 1, 3): [45, 35, 0.42, True], datetime.date(1951, 1, 4): [45, 34, 0.31, True],
               datetime.date(1948, 1, 5): [45, 32, 0.17, True], datetime.date(1951, 1, 6): [48, 39, 0.44, True],
               datetime.date(1948, 1, 7): [50, 40, 0.41, True], datetime.date(1951, 1, 8): [48, 35, 0.04, True],
               datetime.date(1948, 1, 9): [50, 31, 0.12, True], datetime.date(1951, 1, 10): [43, 34, 0.74, True],
               datetime.date(1949, 1, 11): [42, 32, 0.01, True], datetime.date(1952, 1, 12): [41, 26, 0.0, True],
               datetime.date(1949, 1, 13): [45, 29, 0.0, True], datetime.date(1952, 1, 14): [38, 26, 0.0, True],
               datetime.date(1949, 1, 15): [34, 31, 0.0, True], datetime.date(1952, 1, 16): [34, 28, 0.0, True],
               datetime.date(1949, 1, 17): [35, 29, 0.0, True], datetime.date(1952, 1, 18): [33, 28, 0.0, True],
               datetime.date(1949, 1, 19): [34, 27, 0.0, True], datetime.date(1952, 1, 20): [36, 29, 0.0, True],
               datetime.date(1950, 1, 21): [48, 32, 0.0, True], datetime.date(1953, 1, 22): [47, 44, 0.21, True],
               datetime.date(1950, 1, 23): [47, 43, 0.0, True], datetime.date(1953, 1, 24): [45, 34, 0.1, True],
               datetime.date(1950, 1, 25): [46, 30, 0.0, True], datetime.date(1953, 1, 26): [45, 32, 0.0, True],
               datetime.date(1950, 1, 27): [53, 33, 0.0, True], datetime.date(1953, 1, 28): [53, 25, 0.0, True],
               datetime.date(1950, 1, 29): [42, 34, 0.22, True]}


    # rainiest_day(weather1)
    # coldest(weather1)

    Hottestyear(weather)

    # add_rainy(weather1)
    # print(weather1)


    # yearly_weather = consolidate(weather)
    # print(yearly_weather)

    # Year | Avg High Temp | Avg Low Temp | Percip |  # Rainy days | # Recorded days
    # o - -----------------------------------------------------------------------------o
    # == year_info(2016, yearly_weather) == (contained in the dictionary)
    # 2016 |     62.55     |    47.61     |  0.12  |      1.0      |        366

    # tmax, tmin, tprcp, trainydays, tdays = yearly_weather[1953]
    #print("{:^10d}|{:^20.2f}|{:^15.2f}|{:^8.2f}|{:^15.1f}|{:^20d}".format(1953, tmax, tmin, tprcp, trainydays, tdays))

    # findnum(4)
    # handlingexceptions()
    # errortypes()
