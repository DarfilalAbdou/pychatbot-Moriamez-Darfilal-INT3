from functions import *

print("Please select a number to go through the menu \n  Menu : \n"
      "To quit the menu, select 0\n"
      "To display all the names select 1\n"
      "To create a cleaned version of all the text files in the folder select 2`\n"
      "To display the list of words in a given file select 3\n "
      "To display the IDF score of all word in a corpus of files select 4 \n"
      "To display the TF score of all word in a file select 5\n"
      "To display the TF-IDF matrix of a corpus of files select 6 \n"
      "To display the least important words in a corpus of files select 7\n"
      "To display the word with the highest TF-IDF score is, select 8\n "
      "To display the most repeted word by Chirac is, select 9 \n"
      "To display the name of the presidents who used the word Nation"
      "and repeted it the most times, select 10\n"
      "To display the name of the first president who talked about climate, select 11\n"
      "To display the words that all president said w/o the unimportant ones, select 12\n"
      "If you want to see the menu again, select 13")

directory = "./cleaned"
files_names = list_of_files(directory, "txt")

menu=int(input("Choose your action : "))
while menu!=0:

      if menu == 13:
            print("Please select a number to go through the menu \n  Menu : \n"
                  "To quit the menu, select 0\n"
                  "To display all the names select 1\n"
                  "To create a cleaned version of all the text files in the folder select 2`\n"
                  "To display the list of words in a given file select 3\n "
                  "To display the IDF score of all word in a corpus of files select 4 \n"
                  "To display the TF score of all word in a file select 5\n"
                  "To display the TF-IDF matrix of a corpus of files select 6 \n"
                  "To display the least important words in a corpus of files select 7\n"
                  "To display the word with the highest TF-IDF score is, select 8\n "
                  "To display the most repeted word by Chirac is, select 9 \n"
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
            file_name = input("Give the name of a file")
            print(TF(directory,file_name))

      if menu == 6:
            print(matrice(directory))

      if menu == 7:
            print('the least important words are:')
            print(least_important(matrice(directory)))

      if menu == 8:
            print("\nthe word with the highest TF_IDF score is:")
            print(highest_score(matrice(directory)))

      if menu == 9:
            print('\nthe most repeated word by Chirac is:')
            print(most_repeated_word('Nomination_Chirac1.txt','Nomination_Chirac2.txt'))

      if menu == 10:
            print('\nThe presidents that used the word Nation are:')
            display_names(specific_word('nation')[0])
            print("\nThe one that uses it the most is:")
            print(specific_word('nation')[1][0])

      if menu == 11:
            first_to_talk('climat')

      if menu == 12:
            print(important(directory))

      menu = int(input("Choose your action : "))
