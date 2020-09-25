# Andrew McCollum, 09/25/20
# Hackerrank, Python Whats Your Name

"""You are given the firstname and lastname of a person on two different lines. Your task is to read them and print the
following: Hello firstname lastname! You just delved into python."""

"""Programmer's comment: This doesn't need to be a function, and could be written as 3 lines, but hackerrank's
testing required it this way"""


def print_full_name(first_name, last_name):
    print("Hello " + first_name + " " + last_name + "!" + " You just delved into python.")

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)
    