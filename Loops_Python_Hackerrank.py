# Andrew McCollum, 09/04/20
# Hackerrank, Python Loops

"""Task:
The provided code stub reads and integer, N, from STDIN. For all non-negative integers I < N, print (I^2)."""

N = int(input("Please enter a number greater than 0: "))
i = 0

while (i < N) and (N >= 1) and (N <= 20):
    print((i * i))
    i = i + 1
