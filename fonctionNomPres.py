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

display_names((full_names((last_names(files_names)))))