# Andrew McCollum
# 09/12/2020
"""This is a solution for the Hackerrank Python challenge 'No Idea!'. However I was unable to submit it as my IDE,
PyCharm, ran it just fine, yet causing compiling errors with Hackerrank's cloud compiler
UPDATE 09/14/2020:
This solution was now accepted. Code-wise nothing changed, all I can suppose is that an error was made previously
when pasting from PyCharm"""


Happy = 0
N_M = list(map(int, (input("Please enter the integers, separated by a space: ")).split()))
N_Num = N_M[0]
M_Num = N_M[1]
N_Query = "please enter " + str(N_Num) + " integers, separated by spaces: "
M_Query = "please enter " + str(M_Num) + " integers, separated by spaces: "
ListN = list(map(int, (input(N_Query)).split()))
# ListM = list(map(int, (input(M_Query)).split()))
# ListAll = ListN + ListM

A = set(map(int, (input(M_Query)).split()))
B = set(map(int, (input(M_Query)).split()))

for i in range(len(ListN)):
    if ListN[i] in A:
        Happy = Happy +1

for j in range(len(ListN)):
    if ListN[j] in B:
        Happy = Happy - 1


print(Happy)
