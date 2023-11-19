import os
import math

def list_of_files(directory, extension): #function to extract the file names
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names


directory_cleaned = "./cleaned"
files_names = list_of_files(directory_cleaned, ".txt") #creates the list of the files names we're working on
print(files_names)

def Term_Frequency(words_from_speech): #return a dictionnary with the number of occurence of a word in a given list of words
    occurence = {}
    for i in words_from_speech:
        if len(i) >= 1:
            if i not in occurence.keys():
                occurence[i] = 1
            else:
                occurence[i] += 1

def list_of_words(file_name): #creates a list of the words in a given .txt file
    f = open(("./cleaned/"+file_name) ,"r",encoding='utf-8')
    lines = f.readline()
    mots = lines.split(" ")
    while '' in mots:
        mots.remove('')
    f.close()
    return mots

#uses the function above to create a list of 8 elements, containing lists of the words of the 8 speeches
list_of_list_of_words = []
for i in files_names:
    list_of_list_of_words.append(list_of_words(i))

#calculates the IDF scores of each words in a list of list of the words used in each speech
def IDF_scores(list_of_list_of_words):
    IDF_Score = {}
    for speeches in list_of_list_of_words: #we look at each speech
        for word in speeches:   #then at each word in that speech
            if word not in IDF_Score.keys():    #we only look for new words to not have them in double
                IDF_Score[word] = 0
                for k in list_of_list_of_words:    #we count the number of speeches the words chosen appears in
                    if word in k:
                        IDF_Score[word] += 1
    for keys in IDF_Score.keys():
        IDF_Score[keys] = math.log(1/IDF_Score[keys]) #finally we calculate the logarithm of the inverse of the number of speeches each word is in
    print(IDF_Score)


def TF_IDF_matric(directory):
    return