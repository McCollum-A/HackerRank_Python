# Andrew McCollum, 09/12/20
# Hackerrank, Python Tuples

"""Task:
Given an integer, N, and N space-separated integers as input, create a tuple, T , of those N integers.
Then compute and print the result of Hash(T)."""


N = int(input("Please enter the number of integers: "))  # This is unused, but required by Hackerrank's automated test
T = tuple(map(int, (input("Please enter the integers, separated by a space: ")).split()))  # The tuple to be hash'd

print(hash(T))
