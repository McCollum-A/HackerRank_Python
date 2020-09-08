# Andrew McCollum, 09/07/20
# Hackerrank, Python Print Function

"""Task:
The provided code stub will read in a dictionary containing key/value pairs of name:[marks]
for a list of students. Print the average of the marks array for the student name provided,
showing 2 places after the decimal."""


StudentNum = int(input("Please enter the number of students: "))
StartNum = 1
StudentScores = {}

while StartNum <= StudentNum:
    Name, *line = input("Enter name and scores, Name XX YY ZZ: ").split()
    Scores = list(map(float, line))
    StudentScores[Name] = Scores
    StartNum = StartNum + 1


QueryName = input("Which student's average would you like to see? ")
# print(StudentScores[QueryName])
Avg = ((sum(StudentScores[QueryName])) / 3)
print("%.2f" % Avg)
