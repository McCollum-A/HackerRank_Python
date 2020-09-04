# Andrew McCollum, 09/03/20
# Hackerrank, Python Division

"""Task:
The provided code stub reads two integers from STDIN, A and B.
Add logic to print two lines. The first line should contain the result of integer division, A // B.
The second line should contain the result of float division, A / B.
No rounding or formatting is necessary"""

NumsDiv = []
NumsDiv.append(int(input("Please enter a number")))
NumsDiv.append(int(input("Please enter a second number")))
NumsDiv_R = ((NumsDiv[0]) // (NumsDiv[1]))
NumsDiv_Is = ((NumsDiv[0]) / (NumsDiv[1]))

print(NumsDiv_R)
print(NumsDiv_Is)