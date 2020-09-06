# Andrew McCollum, 09/06/20
# Hackerrank, Python Write a Function

"""Task:
Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True,
otherwise return False."""


def is_leap(year):

    if (year % 4 == 0) and (year % 100 != 0):
        leap = True
    elif (year % 100 == 0) and (year % 400 ==0):
        leap = True
    else:
        leap = False

    return leap


year = int(input("Please enter the year in question: "))
print(is_leap(year))