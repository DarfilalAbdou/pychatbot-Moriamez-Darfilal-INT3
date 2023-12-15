from functions import *
from math import *

def dico_into_matrix(dico):
    M = []
    for i in dico.keys():
        M.append(dico[i])
    return M

def translate_matrix(M):
    m = []
    n = len(M)
    for j in range(len(M[0])):
        temp = []
        for i in range(n):
            temp.append(M[i][j])
        m.append(temp)
    return m


'''print(matrice('.\cleaned'))
M = dico_into_matrix(matrice('.\cleaned'))
for i in M:
    print(i)
m = translate_matrix(M)
for i in m:
    print(i)'''

def scalar_product(A, B): #A and B being two vectors
    sum = 0
    for i in range(len(A)):
        sum += A[i]*B[i]
    return sum

def norm(A): #A being a vector
    sum = 0
    for i in A:
        sum += i**2
    return sqrt(sum)

print(norm([3,4]))