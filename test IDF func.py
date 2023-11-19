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


f1 = open("./cleaned/Nomination_Chirac1.txt","r",encoding='utf-8')
f2 = open("./cleaned/Nomination_Hollande.txt","r", encoding='utf-8')

IDF_score = {}

lines = f1.readline()
print(lines)
mots = lines.split(" ")
while '' in mots:
    mots.remove('')
print(mots)
