# Andrew McCollum, 09/06/20
# Hackerrank, Python Print Function

"""Task:
Without using any string methods, try to print the following:
123...n
Note that "..." represents the consecutive values in between."""

ListNums = []  # Dim list for numbers
n = int(input("Please enter a number: "))  # Sets n as limit
StartNum = 1  # Starting counter


while StartNum <= n:  # Each step the value is added to the list of numbers
    ListNums.append(StartNum)
    StartNum = StartNum + 1

print(*ListNums, sep='')  # Print with no separations
