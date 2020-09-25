# Andrew McCollum, 09/25/20
# Hackerrank, Python Split String and Join

"""You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen."""

"""Programmer's comment: This isn't the best way to try teaching about split() and join() as you can easily get
the challenge's desired result using three lines:

OrgStr = input("Please type you phrase: ")
NewStr = OrgStr.replace(" ", "-")
print = (NewStr)"""


def split_and_join(line):
    result = line.replace(" ", "-")
    return(result)


# write your code here

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)