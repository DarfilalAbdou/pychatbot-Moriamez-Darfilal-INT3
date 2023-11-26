from TF_IDF_matrix import *
from fonctionNomPres import*

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
    list_of_pres = []
    cpt = 0
    most_said_pres = []
    files_names = list_of_files('./cleaned', ".txt")
    for i in files_names:
        if word in TF(i).keys():
            list_of_pres.append(i)
            if TF(i)[word] > cpt:
                cpt = TF(i)[word]
                most_said_pres = [i]

    list_of_pres = full_names(last_names(list_of_pres))

    if most_said_pres[-5:] == '1.txt' or most_said_pres[-5:] == '2.txt':
        most_said_pres = full_names(last_names(most_said_pres))[-1:]
    else:
        most_said_pres = full_names(last_names(most_said_pres))

    return list_of_pres, most_said_pres

print('\nThe presidents that use the word Nation are:')
display_names(specific_word('nation')[0])
print("\nThe one that uses it the most is:")
print(specific_word('nation')[1][0])


def first_to_talk(word):
    list_of_pres = specific_word(word)[0]
    oldest = ''
    if list_of_pres == []:
        oldest = 'None'
    else:
        if 'Valery Giscard dEstaing' in list_of_pres:
            oldest = "Valery Giscard d'Estaing"
        elif 'François Mitterrand1' in list_of_pres or 'François Mitterrand2' in list_of_pres:
            oldest = 'François Mitterrand'
        elif 'Jacques Chirac1' in list_of_pres or 'Jacques Chirac2' in list_of_pres:
            oldest = 'Jacques Chirac'
        elif 'Nicolas Sarkozy' in list_of_pres:
            oldest = 'Nicolas Sarkozy'
        elif 'François Hollande' in list_of_pres:
            oldest = 'François Hollande'
        else:
            oldest = 'Emmanuel Macron'

    print (list_of_pres)

first_to_talk('le')