from functions import *

print("To try our features, select 1\n"
      "To talk with our chatbot, select 2\n"
      "To quit, select -1\n")

directory = "./cleaned"
files_names = list_of_files(directory, "txt")

menu=int(input("Choose your action : "))
while menu != -1:
      if menu == 2:
            starters = {"Pourquoi":"Car, ","Comment":"Après analyse, ","Peux-tu":"Oui bien sûr, ", }
            question_asked = input('Ask your question : ')
            relevant_file = (relevant(m, TF_IDF_question(question_asked), list_of_files("./cleaned", "txt")))[1]
            answer= sentence_with_word(relevant_file, most_relevant_word(question_asked))
            #Check the first word of the question to get the appropriate question starter
            list=question_asked.split(" ")
            if list[0] in starters:
                  #Add the starter at the beinning and the dot at the end
                  answer=starters[list[0]]+answer + "."

            print(answer)


      if menu == 1 :
            print("Please select a number to go through the menu \n  Menu : \n"
                  "To quit the application select -1\n"
                  "To quit the menu, select 0\n"
                  "To display all the names select 1\n"
                  "To create a cleaned version of all the text files in the folder select 2\n"
                  "To display the list of words in a given file select 3\n"
                  "To display the IDF score of all word in a corpus of files select 4\n"
                  "To display the TF score of all word in a file select 5\n"
                  "To display the TF-IDF matrix of a corpus of files select 6 \n"
                  "To display the least important words in a corpus of files select 7\n"
                  "To display the word with the highest TF-IDF score is, select 8\n"
                  "To display the most repeted word by Chirac is, select 9 \n"
                  "To display the name of the presidents who used the word Nation"
                  "and repeted it the most times, select 10\n"
                  "To display the name of the first president who talked about climate, select 11\n"
                  "To display the words that all president said w/o the unimportant ones, select 12\n"
                  "If you want to see the menu again, select 13")

            menu = int(input("Choose the feature you want to try:"))
            while menu != 0:

                  if menu == 13:
                        print("Please select a number to go through the menu \n  Menu : \n"
                              "To quit the application select -1\n"                        
                              "To quit the menu, select 0\n"
                              "To display all the names select 1\n"
                              "To create a cleaned version of all the text files in the folder select 2\n"
                              "To display the list of words in a given file select 3\n"
                              "To display the IDF score of all word in a corpus of files select 4 \n"
                              "To display the TF score of all word in a file select 5\n"
                              "To display the TF-IDF matrix of a corpus of files select 6 \n"
                              "To display the least important words in a corpus of files select 7\n"
                              "To display the word with the highest TF-IDF score is, select 8\n"
                              "To display the most repeted word by Chirac is, select 9\n"
                              "To display the name of the presidents who used the word Nation"
                              "and repeted it the most times, select 10\n"
                              "To display the name of the first president who talked about climate, select 11\n"
                              "To display the words that all president said w/o the unimportant ones, select 12\n"
                              "If you want to see the menu again, select 13")

                  if menu == 1:
                        display_names((full_names((last_names(files_names)))))

                  if menu == 2 :
                        replace(files_names)

                  if menu == 3 :
                        file_name=input("Give the name of a file")
                        print(list_of_words(directory,file_name))

                  if menu == 4:
                        print(IDF_scores(directory))

                  if menu == 5:
                        file_name = input("Give the name of a file (ex: Nomination_Hollande.txt) ")
                        print(TF(directory,file_name))

                  if menu == 6:
                        dico = matrix(directory)
                        for i in dico.keys():
                              print(i, dico[i])

                  if menu == 7:
                        print('the least important words are:')
                        print(least_important(matrix(directory)))

                  if menu == 8:
                        print("\nthe word with the highest TF_IDF score is:")
                        print(highest_score(matrix(directory)))

                  if menu == 9:
                        name = input("Fo which president do you want to know his most repeated word? (Last name)")
                        print('\nThe most repeated word by ' + name + ' is:')
                        print(most_repeated_word(name))

                  if menu == 10:
                        word = input("What word are you looking for?")
                        if specific_word(word) == ([],[]):
                              print('Noone said that word')
                        else:
                              print('\nThe presidents that used the word ' + word + ' are:')
                              display_names(specific_word(word)[0])
                              print("\nThe one that uses it the most is:")
                              print(specific_word(word)[1][0])

                  if menu == 11:
                        word = input("What word are you looking for?")
                        if first_to_talk(word) == '':
                              print('Noone said that word')
                        else:
                              print('The first one to say this word was:')
                              print(first_to_talk(word))

                  if menu == 12:
                        print(important(directory))

                  menu = int(input("Choose your action : "))

      menu=int(input("To try our features, select 1\n"
            "To talk with our chatbot, select 2\n"
            "To quit, select -1\n"))
