# Andrew McCollum, 09/22/20
# Hackerrank, Python Nested Lists

"""Given the names and grades for each student in a class of N students,
store them in a nested list and print the name(s) of any student(s) having the second lowest grade."""


StuN = int(input("please input the number of students: "))  # Read int input for variable
SScore = []  # initiate lists
SBoth = []
SFinal = []

def sort_students(Students):  # function to sort the nested lists
    return sorted(Students, key = lambda x: x[1])


for n in range(StuN):  # for range, input a name and a score
    TempName = input("Please enter the student's name: ")
    TempGrade = float(input("Please enter their grade score: "))
    SBoth.append([[TempName, TempGrade]])  # nest a list of name & grade, per student, into this list
    SScore.append(TempGrade)  # only a score for this list

ScoreMax = sorted(list(set(SScore)))[1]  # set variable to second lowest score


for z in range(len(SScore)):  # for range, if list element = 2nd lowest score, add element copy to another list
    if SScore[z] == ScoreMax:
        SFinal.append(SBoth[z][0][0])

for a in (sorted(list(set(SFinal)))):  # for element in list, print
    print()
