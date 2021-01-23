# import random to choose random word from list of words
import random
# variables to prepare and initialize
word_dict = {} # dictionary for the random word
letter_dict = {} # dictionary for the letters and boolean
guesses = 8 # number of guesses

# list of words to choose from randomly
words = ['volleyball', 'setter', 'libero', 'milk', 'sunshine', 'king', 'court', 'national', 'meat', 'captain']
# list to get blanks based on word length
blanks = []
word_in_progress = []

class Word():
    # initialize a word to guess
    def __init__(self, chosen_word):
        self.chosen_word = chosen_word
        self.guesses = guesses
        
        # make the chosen_word into a split list for boolean
        word_dict = list(self.chosen_word)

        # print("initial word_dict:", word_dict)
        # putting every letter into letter_dict for boolean
        for letter in word_dict:
            letter_dict[letter] = "false"

        # print("initial letter_dict:", letter_dict)

        for letter in word_dict:
            if letter_dict[letter] == "true":
                blanks.append(letter)
            if letter_dict[letter] == "false":
                blanks.append("_")
    
        print("guess the word: ", *blanks, sep=' ')

    def guess_letter(self, guessed_letter):
        if guessed_letter in letter_dict:  
            for k, v in letter_dict.items():
                if k == guessed_letter:
                    letter_dict[k] = "true"

                    print("that's correct! your guess:", guessed_letter)
                    # print(self.chosen_word.index(guessed_letter))
                    # print("letter dictionary after correct guess:", letter_dict)

                    word_dict = list(self.chosen_word)
                    # print("word_dict in the guess_letter:", word_dict)

                    for letter in word_dict:
                        if letter_dict[letter] == "true":
                            word_in_progress.append(letter)
                        else:
                            word_in_progress.append("_")

                    print("keep guessing: ", *word_in_progress, sep=' ')
                    

        else:
            print("wrong guess! try again", *word_in_progress, sep=' ')
            self.guesses -= 1
            print(self.guesses, "guesses remaining")

    # def check_finished(self):
    #     for item in letter_dict:
    #         if letter_dict[item] == "true":
    #             return False
    #             break
    #         else:
    #             return True

word1 = Word(random.choice(words))
print("guess a letter", end=": ")
user_input = input()
word1.guess_letter(user_input)

# while guesses > 0:
#     word_game = Word(random.choice(words))
#     print("guess a letter", end=": ")
#     user_input = input()
#     word_game.guess_letter(user_input)
    
# else:
#     print("the game ended")

#### INCOMPLETE CODE -- was not able to get it working with the while loop, kept increasing the word length by adding it on. i think i need to rewrite this but with a dictionary within a dictionary?

## everything else works but it does not seem to work with the while loop - may need to rewrite everything