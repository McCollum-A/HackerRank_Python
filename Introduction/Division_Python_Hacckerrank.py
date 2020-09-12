# Andrew McCollum, 09/03/20
# Hackerrank, Python Division

"""Task:
The provided code stub reads two integers from STDIN, A and B.
Add logic to print two lines. The first line should contain the result of integer division, A // B.
The second line should contain the result of float division, A / B.
No rounding or formatting is necessary"""

NumsDiv = []  # Dim list to hold the entered numbers
NumsDiv.append(int(input("Please enter a number: ")))  # insert the input into list as number
NumsDiv.append(int(input("Please enter a second number: ")))  # same as above
NumsDiv_R = ((NumsDiv[0]) // (NumsDiv[1]))  # Operation for division non-decimal
NumsDiv_Is = ((NumsDiv[0]) / (NumsDiv[1]))  # Standard division

print(NumsDiv_R)  # These two lines print their respective results9
print(NumsDiv_Is)
