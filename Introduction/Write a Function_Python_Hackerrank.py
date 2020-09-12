# Andrew McCollum, 09/06/20
# Hackerrank, Python Write a Function

"""Task:
Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True,
otherwise return False."""


def is_leap(year):  # function name (parameters)

    if (year % 4 == 0) and (year % 100 != 0):  # This math follows the division guild-lines for equating a leap year
        leap = True
    elif (year % 100 == 0) and (year % 400 ==0):
        leap = True
    else:
        leap = False

    return leap


year = int(input("Please enter the year in question: "))  # Gather user input as int
print(is_leap(year))  # Print the return of function is_leap
