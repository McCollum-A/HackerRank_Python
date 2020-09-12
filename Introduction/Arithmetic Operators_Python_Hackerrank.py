# Andrew McCollum, 09/03/20
# Hackerrank, Python Arithmetic Operators

"""Task:
The provided code stub reads two integers from STDIN, A and B. Add code to print three lines where:
-The first line contains the sum of the two numbers
-The second line contains the difference of the two numbers (first - second)
-The third line contains the product of the two numbers"""

Numbers = []  # Dim list for holding the numbers
Numbers.append(int(input("Please enter a number")))  # inserts input into list
Numbers.append(int(input("Please enter a second number")))  # inserts input into list
NumbersSum = sum(Numbers)  # Operation for adding the two numbers
NumbersDiff = ((Numbers[0]) - (Numbers[1]))  # Operation for subtraction
NumbersProd = ((Numbers[0]) * (Numbers[1]))  # Operation for multiplication


print(NumbersSum)  # These three lines print their respective mathematics
print(NumbersDiff)
print(NumbersProd)
