import os
import math

def list_of_files(directory, extension):
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names


directory_cleaned = "./cleaned"
files_names = list_of_files(directory_cleaned, ".txt")
print(files_names)

#funciton that takes the name of a file (speech) and returns a list of all the words used
def list_of_words(file_name):
    f = open(("./cleaned/"+file_name) ,"r",encoding='utf-8')
    lines = f.readline()
    mots = lines.split(" ")
    while '' in mots:
        mots.remove('')
    f.close()
    return mots

#uses the function above to create a list of 8 elements, containing lists of the words of the 8 speeches
def list_of_speeches_words():
    list_of_speeches_word = []
    for i in files_names:
        list_of_speeches_word.append(list_of_words(i))
    return list_of_speeches_word
#calculates the IDF scores of each words in a list of list of the words used in each speech
def IDF_scores(list_of_speeches_words):
    IDF_Score = {}
    for speeches in list_of_speeches_words: #we look at each speech
        for word in speeches:   #then at each word in that speech
            if word not in IDF_Score.keys():    #we only look for new words to not have them in double
                IDF_Score[word] = 0
                for k in list_of_speeches_words:    #we count the number of speeches the words chosen appears in
                    if word in k:
                        IDF_Score[word] += 1
    for keys in IDF_Score.keys():
        IDF_Score[keys] = math.log(1/IDF_Score[keys]) #finally we calculate the logarithm of the inverse of the number of speeches each word is in
    print(IDF_Score)

IDF_scores(list_of_speeches_words())