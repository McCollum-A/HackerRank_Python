# Andrew McCollum
# 09/14/2020
"""You are given N words. Some words may repeat. For each word, output its number of occurrences.
The output order should correspond with the input order of appearance of the word.
See the sample input/output for clarification."""


import collections  # Import for the OrderedDict


Appear = []  # Initialize list
WordCount = int(input("How many words are you going to enter? "))  # Quantity of words to be entered
WordDict = collections.OrderedDict()  # Initialize the OrderedDict


for x in range(WordCount):  # Ask for a word the input'd number of times
    Word = (input("Please enter a word: "))
    if Word in WordDict:
        WordDict[Word] += 1  # Add word to dictionary, if the word (key) is already there, add +1 to the value
    else:
        WordDict[Word] = 1  # Add word to dictionary, if the word (key) isn't already there, set the value as 1

print(len(WordDict))

for key, value in WordDict.items():  # For each word(key) in the dictionary, add said key's value to the list
    Appear.append(value)

print(" ".join(map(str, Appear)))  # Print the Appear list with no brackets and spaces instead of commas

