# Andrew McCollum, 09/07/20
# Hackerrank, Python Print Function

"""Task:
The provided code stub will read in a dictionary containing key/value pairs of name:[marks]
for a list of students. Print the average of the marks array for the student name provided,
showing 2 places after the decimal."""


StudentNum = int(input("Please enter the number of students: "))  # Number of students
StartNum = 1  # While-loop counter
StudentScores = {}  # Dim set for the scores

while StartNum <= StudentNum:  # Begin loop
    Name, *line = input("Enter name and scores, Name XX YY ZZ: ").split()  # Splits the input
    Scores = list(map(float, line))  # Maps the scores input to the name
    StudentScores[Name] = Scores  # sets the list for names, scores
    StartNum = StartNum + 1


QueryName = input("Which student's average would you like to see? ")  # Sets the name to query
Avg = ((sum(StudentScores[QueryName])) / 3)  # Sets sum of NAME's score
print("%.2f" % Avg)  # limit the float to two decimal places when printed
