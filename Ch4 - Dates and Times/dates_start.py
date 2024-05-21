#
# Example file for working with date information
# LinkedIn Learning Python course by Joe Marini
#
from datetime import date
from datetime import time
from datetime import datetime


def main():
    ## DATE OBJECTS
    # TODO: Get today's date from the simple today() method from the date class
    today = date.today()
    print("The date today is:", today)

    # TODO: print out the date's individual components
    print("The components of the date are:", today.day, today.month, today.year)

    # TODO: retrieve today's weekday (0=Monday, 6=Sunday)
    print("Today's weekday No. ", today.weekday())
    days = ["Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun"]
    print("Which is a", days[today.weekday()])

    ## DATETIME OBJECTS
    # TODO: Get today's date from the datetime class
    today = datetime.now()
    print("The current date and time is:", today)

    # TODO: Get the current time
    t = datetime.time(datetime.now())
    print("The current time is:", t)

    # TODO: Get the current date only
    d = datetime.date(datetime.now())
    print("The current time is:", d)


if __name__ == "__main__":
    main()
