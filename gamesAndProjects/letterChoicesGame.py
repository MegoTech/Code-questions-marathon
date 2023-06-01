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
    import random

    # 5. Complex task: Write a program that simulates a simple game of hangman.

    # The user starts with 5 lives
    num_of_lives = 5
    # The program should randomly choose a word from a list of words,
    list_of_words = ["apple", "banana", "orange"]
    word = random.choice(list_of_words)
    # Display the word with underscores in place of the letters.
    underscore = len(word) * "-"
    # The game should continue until the user correctly guesses the word or runs out of lives.
    while num_of_lives > 0:
        print(f"Thw word is: {underscore}")
        # The user should then be prompted to guess a letter.
        letter = input("Guess a letter: ")
        # If the letter is in the word,
        if letter in word:
            # the program should replace the corresponding underscore with the letter
            location = word.find(letter)
            underscore = underscore[:location] + letter + underscore[location + 1:]
            word = word[:location] + "-" + word[location + 1:]
            # If user has won
            if "-" not in underscore:
                print("Congratulations, you guessed the word!")
                # Exit game
                num_of_lives = 0
        # If the letter is not in the word,
        else:
            # the program should subtract a life
            num_of_lives -= 1
            print(num_of_lives)
            # If user has lost
            if num_of_lives == 0:
                print("Game Over!")

    pass