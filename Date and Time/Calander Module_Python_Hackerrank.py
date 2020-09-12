# Andrew McCollum, 09/07/20
# Hackerrank, Python Calendar Module

"""Task:
You are given a date. Your task is to find what the day is on that date."""

import calendar  # imports the needed calendar module for the tasks


def to_int(Day):  # Function named "to_int", parameters (Day)
    if Day[0] == '0':  # being that if Day[0] is equal to 0
        return int(Day[1])
    return int(Day)


Month, Day, Year = input("Please enter the MM DD YYYY in question: ").split()  # Split the input into the three lists
TheCal = calendar.weekday(int(Year), to_int(Month), to_int(Day))  # use the lists(in int) to create a numerical day
print(calendar.day_name[TheCal].upper())  # print the day's name using the numerical day value
