# Andrew McCollum, 09/03/20
# Hackerrank, Python If-Else

"""Task:
Given an integer, n (Number), perform the following conditional actions:
-If N is odd, print Weird
-If N is even and in the inclusive range of 2 to 5, print Not Weird
-If N is even and in the inclusive range of 6 to 20, print Weird
-If N is even and greater than 20, print Not Weird"""


Number = int(input("Please enter a number"))  # Gather the user's number

if (Number % 2) != 0:  # Math to check if it is an odd number
    print("Weird")
elif (Number >= 2) and (Number <= 5):  # Is the number between a range
    print("Not Weird")
elif (Number >= 6) and (Number <= 20):  # Is the number between a range
    print("Weird")
elif Number > 20:  # If the number is greater than
    print("Not Weird")
