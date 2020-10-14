# Andrew McCollum, 10/13/20
# Hackerrank, Python Find a String

"""The user enters a string and a substring. You have to print the number of times that the substring occurs
in the given string. String traversal will take place from left to right, not from right to left.
Programmer's comment: this challenge requires you to use Hackerrank's provided code"""


def count_substring(string, sub_string):  # required by hackerrank
    Matches = 0  # start value at zero
    for i in range(len(string)):  # Iterate through string
        if string[i:].startswith(sub_string):  # if all characters after i (as a string) begin with sub_string
            Matches += 1
    return Matches


if __name__ == '__main__':  # required by hackerrank
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
