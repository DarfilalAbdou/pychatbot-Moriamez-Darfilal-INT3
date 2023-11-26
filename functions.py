import os
from math import log

def list_of_files(directory, extension):
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names

def last_names(liste_fichiers):
    last_names =[]
    integer="0123456789"
    for i in liste_fichiers:
        #We split to get the part where the name is
        name = i.split("_")
        #Create a list of character w/o any numbers and then make a string out of the list
        name[1] = "".join(x for x in name[1] if not x in integer)
        last_names.append(name[1][:len(name[1])-4])
        last_names= list(set(last_names))

    return last_names

def full_names(last_names):#Display the full name
    full_names = []
    for j in last_names:
        if "Chirac" in j:
            full_names.append("Jacques " + j)
        elif "Giscard" in j:
            full_names.append("Valery " + j)
        elif "Hollande" in j:
            full_names.append("François " + j)
        elif "Macron" in j:
            full_names.append("Emmanuel " + j)
        elif "Mitterrand" in j:
            full_names.append("François " + j)
        else:
            full_names.append("Nicolas " + j)

    return full_names

def display_names(full_names):
    for i in full_names:
        print(i)


def replace(tab_speech): #Function to clean the text files
    #Do the code for each document in the list of document

    for k in tab_speech :
        f = open("speeches/"+k, "r", encoding="utf-8")

        #Write the text in a document in cleaned folder with the same name as non cleaned document
        f2 = open("cleaned/"+k, "w", encoding="utf-8")

        exeption = "çàéèêëïù0123456789"
        #Start reading each lines in the doc
        lines = f.readline()
        while lines != "":
            #Turn each letter in lowercase
            lines = lines.lower()

            #delete every \n
            lines = lines.replace(chr(10), " ")
            #We keep every letter and special letter in "exeption" in lines, otherwise the symbols become space
            lines = [x if (x >= "a" and x <= "z") or x in exeption else " " for x in lines]
            #Change list into string
            lines = "".join(lines)
            #Write the string in cleaned document
            f2.write(lines)
            lines = f.readline()
        f.close()
        f2.close()




def list_of_words(directory, file_name): #creates a list of the words in a given .txt file
    f = open((directory+"/"+file_name) ,"r",encoding='utf-8')
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
    number_of_files=len(files_names)
    for i in files_names:
        list_of_list_of_words.append(list_of_words(directory, i))

    for speeches in list_of_list_of_words: #we look at each speech
        for word in speeches:   #then at each word in that speech
            if word not in IDF_Score.keys():    #we only look for new words to not have them in double
                IDF_Score[word] = 0
                for k in list_of_list_of_words:    #we count the number of speeches the words chosen appears in
                    if word in k:
                        IDF_Score[word] += 1
    for keys in IDF_Score.keys():
        IDF_Score[keys] = log(number_of_files/IDF_Score[keys]) #finally we calculate the logarithm of the inverse of the number of speeches each word is in
    return IDF_Score


def TF(directory,fichier): #counts the number of words present in a given .txt file and returns it in the form of a dictionnary
    f=open(directory+"/"+fichier, "r", encoding="utf-8")
    lines=f.readline()
    #split to get every word in the file
    lines= lines.split(" ")
    occurence={}
    for i in lines:
        #to not have space occurences in the dictionary
        if len(i) >= 1:
            if i not in occurence.keys():
                occurence[i] = 1
            else:
                occurence[i] += 1
    f.close()
    return occurence



#makes a matrix with for each row, the total words in all the documents, and for each column the corresponding document
def matrice(directory): #we give './cleaned'
    idf_scores = IDF_scores(directory)
    dico_mat = {}   #we start with a dictionnary where the keys are the words and the values are empty lists
    for i in idf_scores.keys():
        dico_mat[i] = []

    files_names = list_of_files(directory, ".txt")
    for file in files_names:    #for each file
        tf = TF(directory, file)           #we take its words occurence (term frequency)
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


def least_important(dico):
    list_of_words = []
    for i in dico.keys():
        if sum(dico[i]) == 0:
            list_of_words.append(i)
    return list_of_words



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
        if occu1[k] > maxi:
            maxi = occu1[k]
            word = k

    return word



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


#__merge("./cleaned","./merged")


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


