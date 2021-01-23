# # import random to choose random word from list of words
# import random
# # variables to prepare and initialize
# # word_dict = {} # dictionary for the random word
# # letter_dict = {} # dictionary for the letters and boolean
# # word_data = []
# # guesses = 8 # number of guesses

# # list of words to choose from randomly
# words = ['volleyball', 'setter', 'libero', 'milk', 'sunshine', 'king', 'court', 'national', 'meat', 'captain']
# # list to get blanks based on word length
# blanks = []
# word_in_progress = []

# class Word():
#     # initialize a word to guess
#     def __init__(self, chosen_word):
#         self.chosen_word = chosen_word
#         self.word_dict = {}
#         self.letter_dict = {}
#         self.word_data = []
#         self.guesses = 8

#         print(chosen_word)
#         self.word_dict = list(self.chosen_word)
#         print(self.word_dict)

#         for letter in self.word_dict:
#             self.letter_dict['letter'] = letter 
#             self.letter_dict['guessed'] = False 
#             print(self.letter_dict)
#             self.word_data.append(self.letter_dict)

#         print("word_data:", self.word_data)

#     def check_letter(self, letter):
#         if letter in self.chosen_word:
#             for item in self.word_data:
#                 if letter == item['letter']:
#                     item['guessed'] = True
#         else:
#             self.guesses -= 1
#             print("wrong guess, try again!")

#     def print_word(self):
#         for item in self.word_data:
#             if item['guessed'] == True:
#                 print((item['letter'] + " "))
#             else:
#                 print("_ ")
#         print()

# milk = Word("milk")
# milk.check_letter("i")
# milk.print_word()
