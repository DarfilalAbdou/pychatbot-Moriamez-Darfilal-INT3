import os

sentences = ''
with open('./speeches/Nomination_Macron.txt', 'r', encoding="utf-8") as file:
    lignes = file.readlines()
    for ligne in lignes:
        sentences = sentences + ' '+ ligne[:-1]

print(sentences)
print(sentences.split('.'))

for i in sentences.split('.'):
    if 'climat' in i:
        print(i)
        break