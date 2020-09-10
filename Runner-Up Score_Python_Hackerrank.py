# Andrew McCollum, 09/09/20
# Hackerrank, Python Runner-Up Score

"""Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score.
You are given N scores. Store them in a list and find the score of the runner-up."""


ScoresOrder = []
ScoresNo = int(input("Please enter the number of recorded scores: "))
ScoresList = list(map(int, input("Please input the scores, separated by a space: ").split()))

ScoresList.sort(reverse=True)

print(max([x for x in ScoresList if x != max(ScoresList)]))
