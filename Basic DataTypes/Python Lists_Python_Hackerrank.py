# Andrew McCollum, 09/12/20
# Hackerrank, Python Lists

"""Task:
Initialize your list and read in the value of  followed by  lines of commands where each command will be of the N types
listed above. Iterate through each command in order and perform the corresponding operation on your list."""


TheList = []  # Initiate list
OpNum = input("Enter the number of following operations: ")  # Number of operations to perform

for i in range(int(OpNum)):  # Loop through the number of operations
    Op = input().split()  # Split the input into a command and a value

    if Op[0] == "append":
        TheList.append(int(Op[1]))
    elif Op[0] == "insert":
        TheList.insert((int(Op[1])), int(Op[2]))
    elif Op[0] == "print":
        print(TheList)
    elif Op[0] == "remove":
        TheList.remove(int(Op[1]))
    elif Op[0] == "sort":
        TheList.sort()
    elif Op[0] == "pop":
        TheList.pop()
    elif Op[0] == "reverse":
        TheList.reverse()


