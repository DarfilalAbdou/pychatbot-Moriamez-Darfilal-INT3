from fonctionNomPres import *
from functions import *
def idf(fichier):
    f=open("cleaned/"+fichier, "r", encoding="utf-8")
    lines=f.readline()
    lines= lines.split(" ")
    occurence={}
    for i in lines:
        if len(i) >= 1:
            if i not in occurence.keys():
                occurence[i] = 1
            else:
                occurence[i] += 1
    return occurence
#print(idf())


def matrix(directory):
    list_fichier = list_of_files(directory,".txt")
    tab2 = []
    print(list_fichier)
    for k in list_fichier :
        fichier = k
        tab=[]
        for j in idf(fichier).keys():
            for i in IDF_scores(list_of_speeches_words()).keys():
                if j == i:
                    tab.append((j,idf(fichier)[j]*IDF_scores(list_of_speeches_words())[i]))
        tab2.append(tab)
    return tab2
print(matrix("./cleaned"))
print(IDF_scores(list_of_speeches_words()))

dico={"orange":2}

print(dico["orange"])
