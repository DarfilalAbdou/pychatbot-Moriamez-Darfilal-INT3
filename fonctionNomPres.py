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
    for k in tab_speech :
        f = open("speeches/"+k, "r", encoding="utf-8")
        f2 = open("cleaned/"+k, "w", encoding="utf-8")

        exeption = "çàéèêëï0123456789"
        lines = f.readline()
        while lines != "":
            lines = lines.lower()
            lines = lines.replace(chr(10), " ")
            lines = lines.replace(" ", "/")
            lines = [x if (x >= "a" and x <= "z") or x in exeption else " " for x in lines]
            lines = "".join(lines)
            f2.write(lines)
            lines = f.readline()
        f.close()
        f2.close()

