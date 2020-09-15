# Andrew McCollum, 09/14/20
# Hackerrank, Python Find Angle MBC

"""Task:
The task requires graphics, please see; https://www.hackerrank.com/challenges/find-angle/problem"""

import math

AB = int(input("Please input the length of line AB: "))
BC = int(input("Please input the length of line BC: "))

# Set up Pythagorean's theory for AC, A^2 (AB) + B^2 (BC) = C^2 (AC)
AC = math.sqrt((AB ** 2) + (BC ** 2))
MC = (AC / 2)  # Find half of AC

# Use arc cosine to find the wanted angle
Adjacent = (BC / 2)
Theta = (math.degrees(math.acos(Adjacent / MC)))

print((str(int(round(Theta)))) + "°")
# print; string(degrees), the int Theta rounded
