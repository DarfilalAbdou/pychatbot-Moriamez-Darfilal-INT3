from TF_IDF_matrix import *
from fonctionNomPres import *
from math import log


def least_important(dico):
    list_of_words = []
    for i in dico.keys():
        if sum(dico[i]) == 0:
            list_of_words.append(i)
    return list_of_words


"""print('the least important words are:')
print(least_important(matrice('./cleaned')))"""


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


"""print("\nthe socre with the highest TF_IDF score is:")
print(highest_score(matrice('./cleaned')))"""


def most_repeated_word(file1, file2):
    occu1 = TF('./cleaned', file1)
    occu2 = TF('./cleaned', file2)

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


"""print('\nthe most repeated word by Chirac is:')
print(most_repeated_word('Nomination_Chirac1.txt','Nomination_Chirac2.txt'))"""


def specific_word(word):
    list_of_pres = []
    cpt = 0
    most_said_pres = []
    files_names = list_of_files('./cleaned', ".txt")
    for i in files_names:
        if word in TF('./cleaned',i).keys():
            list_of_pres.append(i)
            if TF('./cleaned',i)[word] > cpt:
                cpt = TF('./cleaned',i)[word]
                most_said_pres = [i]

    list_of_pres = full_names(last_names(list_of_pres))

    if most_said_pres[-5:] == '1.txt' or most_said_pres[-5:] == '2.txt':
        most_said_pres = full_names(last_names(most_said_pres))[-1:]
    else:
        most_said_pres = full_names(last_names(most_said_pres))

    return list_of_pres, most_said_pres


"""print('\nThe presidents that use the word Nation are:')
display_names(specific_word('nation')[0])
print("\nThe one that uses it the most is:")
print(specific_word('nation')[1][0])"""


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

    print(list_of_pres)


# first_to_talk('le')

# A private function that create, in a private folder, a merged version of each speech so it's one per person
# Example Chirac1 and Chirac2 is merged into one Chirac
def __merge(start, destination):

    lastname = last_names(list_of_files(start, "txt"))
    listfile = list_of_files(start, "txt")
    # For each file we check if it correspond to a name.
    for i in listfile:
        for j in lastname:
            if j in i:
                # If it does we open the file in "cleaned" to read
                f = open(start + "/" + i, "r", encoding="utf-8")
                # We open in "a" so the content can get written on top of each other
                f1 = open(destination + "/" + j + ".txt", "a", encoding="utf-8")
                line = f.readline()
                """Then we write the content of the cleaned file in the merge file
                and since the name of the file is based only on the name of the president
                then each speeches is going to get merged accordingly
                """
                f1.write(" " + line)
                f.close()
                f1.close()


__merge("./cleaned","./merged")

# function to know which word every president mentioned w/o uninportant
def important(directory):
    # We take the matrice of cleaned and merged to compare their "least_important"
    idfscore = least_important(matrice(directory))

    idfscore2 = least_important(matrice("./merged"))
    l = []
    for j in idfscore2:
        """if a word is in matrice merged and not in matrice cleaned, 
        then all the president talked about it either in the first or second speech 
        """
        if j not in idfscore:
            l.append(j)
    return l


print(important("./cleaned"))

print(least_important(matrice("./cleaned")))
