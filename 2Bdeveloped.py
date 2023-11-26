from TF_IDF_matrix import *


def least_important(dico):
    list_of_words = []
    for i in dico.keys():
        if sum(dico[i])== 0:
            list_of_words.append(i)
    return list_of_words

print('the leasst important words are:')
print(least_important(matrice('./cleaned')))

def highest_score(dico):
    maxi = 0
    for i in dico.keys():
        if max(dico[i]) > maxi:
            maxi = max(dico[i])

    list_of_words = []
    for j in dico.keys():
        if max(dico[j]) == maxi:
            list_of_words.append(j)

    return list_of_words

print("\nthe socre with the highest TF_IDF score is:")
print(highest_score(matrice('./cleaned')))

def most_repeated_word(file1,file2):
    occu1 = TF(file1)
    occu2 = TF(file2)

    for i in occu2.keys():
        if i in occu1.keys():
            occu1[i] += occu2[i]
        else:
            occu1[i] = occu2[i]

    maxi = 0
    word = ''
    for k in occu1.keys():
        if occu1[i] > maxi:
            maxi = occu1[i]
            word = i

    return word

print('\nthe most repeated word by Chirac is:')
print(most_repeated_word('Nomination_Chirac1.txt','Nomination_Chirac2.txt'))

def specific_word(word):
    return word