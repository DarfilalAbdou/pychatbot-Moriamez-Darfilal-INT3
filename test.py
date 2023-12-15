from functions import *

def quest(st):
    exeption = "çàéèêëïù0123456789"
    # Start reading each lines in the doc
    lines = st
    # Turn each letter in lowercase
    lines = lines.lower()

    # delete every \n
    lines = lines.replace(chr(10), "")
    # We keep every letter and special letter in "exeption" in lines, otherwise the symbols become space
    lines = [x if (x >= "a" and x <= "z") or x in exeption else " " for x in lines]
    lines = ("".join(lines)).split(" ")
    lines=[x for x in lines if len(x)>0]
    return lines

#print(quest("Pourquoi t'es pas bo comme ça ??"))

def identify(list_word):

    dico=IDF_scores("./cleaned")
    lis=[]
    for w in list_word:
        if w in dico.keys():
            lis.append(w)
    return lis


def TF_question(question):
    occurence={}
    lis=identify(question)
    for i in question:
        if len(i) >= 1: #to not have space occurences in the dictionary
            if i not in occurence.keys():
                occurence[i] = 1
            else:
                occurence[i] += 1
    return occurence


a=TF_question(quest("Pourquoi t'es pas bo comme ça ??"))

def TF_IDF_question(question):
    TF_IDF_Score = {}
    question=quest(question)
    score_global=IDF_scores("./cleaned")
    TF = TF_question(question)
    question_list=identify(question)
    for word in score_global.keys():
        #print(word)
        if word in question_list:
            TF_IDF_Score[word] = score_global[word]*TF[word]
        else:
            TF_IDF_Score[word] = 0
    return TF_IDF_Score

print(TF_IDF_question("Pourquoi t'es pas bo comme ça ??"))


def TF_IDF_question_matrix():
    pass




