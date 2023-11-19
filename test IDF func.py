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


def IDF(directory):
    IDFscores = {}
