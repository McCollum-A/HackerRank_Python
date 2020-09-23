# Andrew McCollum, 09/22/20
# Hackerrank, Python sWAP cASE

"""You are given a string and your task is to swap cases. In other words,
convert all lowercase letters to uppercase letters and vice versa."""

def Swapping(StringS):  # create function to swap cases
    Swapped = [ch.lower() if ch.isupper() else ch.upper() for ch in StringS]
    # Above creates a list using list comprehension, character lower if it is actually upper,
    # else make it upper, done for each character in the string
    Swapped = ''.join(Swapped)  # join into str
    return Swapped


StringS = input("Please type your string: ")  # read input as variable
Done = Swapping(StringS)  # new variable is StringS run through the function
print(Done)
