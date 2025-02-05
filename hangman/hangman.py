# Hangman
# This version of the game requires every individual letter to be guessed,
# even if there are multiple instances.
# A random word is used from a dictionary of English words.

import nltk
import random
#nltk.download('words')
from nltk.corpus import words

word_list = words.words()

def hangman(word):
    wrong = 0
    game_stages = ["",
                   "___________          ",
                   "|         |          ",
                   "|         |          ",
                   "|         0          ",
                   "|        /|\\        ",
                   "|        / \\        ",
                   "|                    "
                   ]
    word_chars = list(word)
    board = ["__"] * len(word)
    winner = False
    print("Let's Play Hangman!")
    # Game Loop
    while wrong < len(game_stages) - 1:
        print("\n")
        message = "Guess a letter:\n"
        guess = input(message)
        try:
            if guess in word_chars:
                char_index = word_chars.index(guess)
                board[char_index] = guess
                word_chars[char_index] = "$"
            else:
                wrong += 1
            print((" ".join(board)))
            e = wrong + 1
            print("\n".join(game_stages[:e]))
            if "__" not in board:
                print("Congratulations, you win! The word was \'{}\'.".format(word))
                print(" ".join(board))
                winner = True
                break
        except:
            print("Input was not valid. It must be a letter.")
    # If player two won, do nothing, game is over
    if not winner:
        print("\n".join(game_stages[:wrong]))
        print("\nUh-oh! You've been hanged. The word was \'{}\'.".format(word))

# Start the game with a random word
random_word = random.choice(word_list)
hangman(random_word)
