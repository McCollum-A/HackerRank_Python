# Andrew McCollum, 09/03/20
# Hackerrank, Python Arithmetic Operators

"""Task:
The provided code stub reads two integers from STDIN, A and B. Add code to print three lines where:
-The first line contains the sum of the two numbers
-The second line contains the difference of the two numbers (first - second)
-The third line contains the product of the two numbers"""

Numbers = []
Numbers.append(int(input("Please enter a number")))
Numbers.append(int(input("Please enter a second number")))
NumbersSum = sum(Numbers)
NumbersDiff = ((Numbers[0]) - (Numbers[1]))
NumbersProd = ((Numbers[0]) * (Numbers[1]))


print(NumbersSum)
print(NumbersDiff)
print(NumbersProd)
