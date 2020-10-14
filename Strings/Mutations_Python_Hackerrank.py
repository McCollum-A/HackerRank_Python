# Andrew McCollum, 10/13/20
# Hackerrank, Python Mutations

"""Read a given string, change the character at a given index and then print the modified string.
Programmer's comment: this challenge requires you to use Hackerrank's provided code"""


def mutate_string(string, position, character):  # included from hackerrank
    CopyS = string[:position] + character + string[position + 1:]  # create duplicate. then swap out the character
    return CopyS

if __name__ == '__main__':  # included from hackerrank
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
