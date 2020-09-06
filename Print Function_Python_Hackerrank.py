# Andrew McCollum, 09/06/20
# Hackerrank, Python Print Function

"""Task:
Without using any string methods, try to print the following:
123...n
Note that "..." represents the consecutive values in between."""

ListNums = []
n = int(input("Please enter a number: "))
StartNum = 1


while StartNum <= n:
    ListNums.append(StartNum)
    StartNum = StartNum + 1

print(*ListNums, sep='')