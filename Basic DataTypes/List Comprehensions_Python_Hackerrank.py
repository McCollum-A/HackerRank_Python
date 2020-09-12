# Andrew McCollum, 09/09/20
# Hackerrank, Python List Comprehension

"""Task: You are given three integers X, Y and Z representing the dimensions of a cuboid along with an integer N.
Print a list of all possible coordinates given by (i,j,k) on a 3D grid where the sum of i+j+k is not equal to N.
Here. Please use list comprehensions rather than multiple loops, as a learning exercise"""

IntX = int(input("Please enter X value: "))  # These four lines gather user input
IntY = int(input("Please enter Y value: "))
IntZ = int(input("Please enter Z value: "))
IntN = int(input("Please enter N value: "))
ListX = []  # These three lines Dim a new list
ListY = []
ListZ = []
Counter = 0  # loop counter

while Counter <= IntX:  # For each step, add Counters' value into the list. This is repeated per list
    ListX.append(Counter)
    Counter = Counter + 1

Counter = 0  # Reset Counter to zero

while Counter <= IntY:
    ListY.append(Counter)
    Counter = Counter + 1

Counter = 0

while Counter <= IntZ:
    ListZ.append(Counter)
    Counter = Counter + 1


Perms = [[i, j, k] for i in ListX for j in ListY for k in ListZ if (i + j + k != IntN)]
# The above line creates nested lists for each iteration, but only if the nested sum is not equal to IntN
print(str(Perms))
