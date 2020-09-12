# Andrew McCollum, 09/09/20
# Hackerrank, Python Runner-Up Score

"""Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score.
You are given N scores. Store them in a list and find the score of the runner-up."""


ScoresNo = int(input("Please enter the number of recorded scores: "))
# The above variable isn't actually needed, but was required to pass Hackerrank's automated testing
ScoresList = list(map(int, input("Please input the scores, separated by a space: ").split()))
# The above splits the input into a list of ints
ScoresList.sort(reverse=True)  # Sort descending

print(max([x for x in ScoresList if x != max(ScoresList)]))
# Since the numbers are now ordered descending, this returns the non-max number from left to right, aka second highest
