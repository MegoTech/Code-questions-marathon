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

import random as rm
def choice_word_mendi_yacobovitz(words):
    word = rm.choice(words)
    return word
def start_mendi_yacobobvitz(word):
    print("Welcome to the game")
    res_list = []
    for i in range(len(word)):
        res_list.append('-')
    print(*res_list)
    return res_list
def play_game_mendi_yacobobvitz(res_list, word):
    """""
    the function ask from the plyer to guess a letter, and checks if this letter is correct and writes this in a place.
    """""
    while True:
        letter = input("guess a letter: ")
        try:
            if 123 > ord(letter.lower()) > 96:
                break
        except SyntaxError:
            print("Error")
        except TypeError:
            print("error")

    # checks if this letter is correct and writes this in a place
    if letter in word:
        for i in range(len(res_list)):
            if res_list[i] == '-':
                if word[i] == letter:
                    res_list[i] = letter
                break
    return res_list
def main():
    choice_word_mendi_yacobovitz(words=[])
    start_mendi_yacobobvitz(word)
    play_game_mendi_yacobobvitz(res_list, word)

#~~~~~~~~~~~~~~~~~~test~~~~~~~~~~~~~~~~~~~~~~
if __name__ == '__main__':
    word = choice_word_mendi_yacobovitz(words=["apple", "banana", "orange"])
    res_list = start_mendi_yacobobvitz(word)
    n = 5
    while n != 0:
        second_list = res_list[::]
        res_list = play_game_mendi_yacobobvitz(res_list, word)
        print("the word is: ", *res_list)

        # checks if the player guessed all word
        if '-' not in res_list:
            print("Well done")
            break

        # checks if the player guessed a correct letter
        if second_list == res_list:
            n -= 1
    if n == 0:
        print("game over")

