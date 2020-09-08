# Andrew McCollum, 09/07/20
# Hackerrank, Python Calendar Module

"""Task:
You are given a date. Your task is to find what the day is on that date."""

import calendar


def to_int(Day):#
    if Day[0] == '0':
        return int(Day[1])
    return int(Day)


Month, Day, Year = input("Please enter the MM DD YYYY in question: ").split()
TheCal = calendar.weekday(int(Year), to_int(Month), to_int(Day))
print(calendar.day_name[TheCal].upper())
