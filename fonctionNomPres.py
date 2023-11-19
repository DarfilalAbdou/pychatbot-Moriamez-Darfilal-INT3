import os

def list_of_files(directory, extension):
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names

directory = "./speeches"
files_names = list_of_files(directory, ".txt")
print(files_names)


def last_names(liste_fichiers):
    last_names =[]
    for i in liste_fichiers:
        name = i.split("_")
        last_names.append(name[1][:len(name[1])-4])

    return last_names

def full_names(last_names):
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


def replace(tab_speech):
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

