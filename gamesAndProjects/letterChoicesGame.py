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

#~~~~~~~~~~~~~~~~~~test~~~~~~~~~~~~~~~~~~~~~~
if __name__ == '__main__':
    # add your tests here
    import random


    def choose_word(words):
        return random.choice(words)
    #this function choose one of the given words

    def initiallize_word(word):
        return ['_'] * len(word)
    #create the starting line with no letters

    def update_word(word, guessed_word, letter):
        for i in range(len(word)):
            if word[i] == letter:
                guessed_word[i] = letter
        return guessed_word
    #added the correct letter to the answer line

    def print_word(word):
        print("the word is:",(''.join(word)))
    #print the answer line without the []

    def letter_choices_game(words):
        word = choose_word(words)
        guessed_word = initiallize_word(word)
        lives = 5

        print("welcome to a letter choice game")
        print_word(guessed_word)

        while True:
            guess = input("guess a letter: ")
            if guess in word:
                guessed_word = update_word(word, guessed_word, guess)
                print_word(guessed_word)
                if '_' not in guessed_word:
                    print("חיילך לאורייתא! רואים שאתה מתלמידי מיגו המובחרים ;)")
                    break
            else:
                lives -= 1
                print(f"wrong guess :( you have {lives} lives remaining.")
                if lives == 0:
                    print("game over. try harder next time!")
                    print(f"the word was: {word}")
                    break


words = ["apple", "banana", "orange"]
letter_choices_game(words)

#~~~~~~~~~~~$~~~~~~~~~