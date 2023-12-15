from functions import *
from math import *
from test import *

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


M = dico_into_matrix(matrice('.\cleaned'))
m = translate_matrix(M)

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

def similarity(A,B): #A and B being two vectors
    scalar = scalar_product(A, B)
    normA = norm(A)
    normB = norm(B)
    return scalar/(normA*normB)

question = "Peux-tu me dire comment une nation peut-elle prendre soin du climat ?"

Question_Vector = dico_into_matrix(TF_IDF_question(question))
Doc1_Vector = m[5]
print(Question_Vector)
print(Doc1_Vector)
for i in range(8):
    print(similarity(Question_Vector, m[i]))
    print(similarity(m[i], Question_Vector))