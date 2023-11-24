import os
import math

def list_of_files(directory, extension): #function to extract the file names
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names

def list_of_words(file_name): #creates a list of the words in a given .txt file
    f = open(("./cleaned/"+file_name) ,"r",encoding='utf-8')
    lines = f.readline()
    mots = lines.split(" ")
    while '' in mots:
        mots.remove('')
    f.close()
    return mots

#calculates the IDF scores of each words in a list of list of the words used in each speech
def IDF_scores(directory): #on donne ./cleaned
    IDF_Score = {}

    list_of_list_of_words = []  #makes a list of the lists of words cointained in each speech
    files_names = list_of_files(directory, ".txt")
    for i in files_names:
        list_of_list_of_words.append(list_of_words(i))

    for speeches in list_of_list_of_words: #we look at each speech
        for word in speeches:   #then at each word in that speech
            if word not in IDF_Score.keys():    #we only look for new words to not have them in double
                IDF_Score[word] = 0
                for k in list_of_list_of_words:    #we count the number of speeches the words chosen appears in
                    if word in k:
                        IDF_Score[word] += 1
    for keys in IDF_Score.keys():
        IDF_Score[keys] = math.log(8/IDF_Score[keys]) #finally we calculate the logarithm of the inverse of the number of speeches each word is in
    return IDF_Score

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

def matrice(directory): #on donne './cleaned'
    idf_scores = IDF_scores(directory)
    dico_mat = {}
    for i in idf_scores.keys():
        dico_mat[i] = []

    files_names = list_of_files(directory, ".txt")
    for file in files_names:
        tf = TF(file)
        for key in idf_scores.keys():
            if key in tf.keys():
                dico_mat[key].append(idf_scores[key]*tf[key])
            else:
                dico_mat[key].append(0)

    '''for k in dico_mat.keys(): LECTURE LISIBLE AVEC MOTS PARCE QUE C'EST CHAUD SINON
        print(k,dico_mat[k])'''

    MAT = []
    for lists in dico_mat.values():
        MAT.append(lists)
    return MAT


for i in matrice('./cleaned'):
    print(i)