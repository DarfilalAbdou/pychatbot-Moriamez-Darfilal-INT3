import os
import math

def list_of_files(directory, extension): #function to extract the file names in a list form
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names

def list_of_words(file_name): #creates a list of the words in a given .txt file
    f = open(("./cleaned/"+file_name) ,"r",encoding='utf-8')
    lines = f.readline()
    words = lines.split(" ")
    while '' in words:
        words.remove('')
    f.close()
    return words

#calculates the IDF scores of each words in a list of list of the words used in each speech
def IDF_scores(directory): #we give ./cleaned
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

def TF(fichier): #counts the number of words present in a given .txt file and returns it in the form of a dictionnary
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

#makes a matrix with for each row, the total words in all the documents, and for each column the corresponding document
def matrice(directory): #we give './cleaned'
    idf_scores = IDF_scores(directory)
    dico_mat = {}   #we start with a dictionnary where the keys are the words and the values are empty lists
    for i in idf_scores.keys():
        dico_mat[i] = []

    files_names = list_of_files(directory, ".txt")
    for file in files_names:    #for each file
        tf = TF(file)           #we take its words occurence (term frequency)
        for key in idf_scores.keys():   #and we compare its terms with their IDF scores
            if key in tf.keys():
                dico_mat[key].append(idf_scores[key]*tf[key])
            else:   #if a word with a IDF score is not in the document, then its occurence does not exist but its TF-IDF wore has to be 0
                dico_mat[key].append(0)

    #remove triple quotes to have a readable display with first the word, then it's list of tf-idf score for each document
    '''for k in dico_mat.keys():
        print(k,dico_mat[k])'''

    MAT = []    #we now convert the dictionnary to a matrix as asked, but it is less readable
    for lists in dico_mat.values():
        MAT.append(lists)
    #return MAT
    return dico_mat


#for i in matrice('./cleaned'): #displays the matrix, its content row by row, but without the first pair of [] that make it a list of list
#    print(i)