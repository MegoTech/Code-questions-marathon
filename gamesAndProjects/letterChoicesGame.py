#5. Complex task:
# Write a program that simulates a simple game of hangman.
# The program should randomly choose a word from a list of words,
# and display the word with underscores in place of the letters.
# The user should then be prompted to guess a letter.
# If the letter is in the word,
# the program should replace the corresponding underscore with the letter.
# If the letter is not in the word,
# the program should subtract a life (the user starts with 5 lives)
# and display the updated state of the player.
# The game should continue until the user correctly guesses the word or runs out of lives.
# Use functions to organize your code.
#
# Example input/output:
# Possible words: ["apple", "banana", "orange"]
# The word is: _ _ _ _ _
# Guess a letter: a
# The word is: a _ _ _ _
# Guess a letter: r
# The word is: a p p _ _
# Guess a letter: p
# The word is: a p p _ _
# Guess a letter: l
# The word is: a p p l _
# Guess a letter: e
# Congratulations, you guessed the word!

# Tip: divide the task into smaller tasks and write a function for each task.
import random


def choose_word(lst):
    return lst[random.randint(0, len(lst) - 1)]


def show_hidden_word(secret_word, old_letters_guessed):
    new_list = list(secret_word)
    for k in range(len(secret_word)):
        if secret_word[k] not in old_letters_guessed:
            new_list[k] = "_"
    return " ".join(new_list)


def check_win(secret_word, old_letters_guessed):
    new_list = list(secret_word)
    for j in range(len(secret_word)):
        if new_list[j] not in old_letters_guessed:
            return False
    return True




#~~~~~~~~~~~~~~~~~~test~~~~~~~~~~~~~~~~~~~~~~
if __name__ == '__main__':
    # add your tests here
    list1 = ["apple", "banana", "orange"]
    guessed = []
    i = 5
    word_to_guess = choose_word(list1)
    print("The word is: ", show_hidden_word(word_to_guess, guessed))
    while i > 0:
        letter = input("Guess a letter: ")
        guessed.append(letter)
        if letter not in word_to_guess:
            i -= 1
        print("The word is: ", show_hidden_word(word_to_guess, guessed))
        if check_win(word_to_guess, guessed) is True:
            print("Congratulations, you guessed the word!")
            break