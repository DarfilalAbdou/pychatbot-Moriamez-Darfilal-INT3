from fonctionNomPres import *
from functions import *
def TF(fichier):
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
#print(TF())


def matrix(directory):
    list_fichier = list_of_files(directory,".txt")
    tab2 = []
    #Loop to take every text in a given file
    for k in list_fichier :
        fichier = k
        tab=[]
        """ We search the key in IF and IDF_scores 
        so that we can multiply their values when the key are the same
        """
        for j in TF(fichier).keys():
            for i in IDF_scores("./cleaned").keys():
                if j == i:
                    #Creation of the list of the form [word, TF-TDF score]
                    tab.append((j,TF(fichier)[j]*IDF_scores("./cleaned")[i]))
        #Creation of the matrix
        tab2.append(tab)
    return tab2
print(matrix("./cleaned"))
