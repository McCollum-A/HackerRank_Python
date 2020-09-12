# Andrew McCollum, 09/04/20
# Hackerrank, Python Loops

"""Task:
The provided code stub reads and integer, N, from STDIN. For all non-negative integers I < N, print (I^2)."""

Number = int(input("Please enter a number greater than 0: "))  # Gather user input
i = 0

while (i < Number) and (Number >= 1) and (Number <= 20):
    print((i * i))
    i = i + 1
# The above code prints, per line, i squared, for as long as it is within bounds
