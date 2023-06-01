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

def random_word(words):
    """
    Selects a random word from a list of words.

    Args:
        words (list): A list of words.

    Returns:
        str: A randomly selected word from the list.
    """
    return random.choice(words)
def hidden_word(word):
    """
    Generates a string with underscores representing hidden letters of a word.

    Args:
        word (str): The word to be hidden.

    Returns:
        str: A string with underscores (_) of the same length as the word.
    """
    return "_" * len(word)
def check_correct(let, word, choice):
    """
    Checks if a guessed letter is correct and updates the hidden word.

    Args:
        let (str): The guessed letter.
        word (str): The current state of the hidden word.
        choice (str): The word to guess.

    Returns:
        str: The updated hidden word with correctly guessed letters revealed.
    """
    if let not in choice:
        return word
    for i in range(len(choice)):
        if choice[i] == let:
            word = word[:i] + let + word[i+1:]
    return word
def check_life(let, choice, life):
    """
    Checks if a guessed letter is incorrect and reduces a life if necessary.

    Args:
        let (str): The guessed letter.
        choice (str): The word to guess.
        life (int): The current number of remaining lives.

    Returns:
        int: The updated number of remaining lives.
    """
    if let not in choice:
        life -= 1
    return life
def check_sit(word, life):
    """
    Checks the current game situation to determine if the game should continue.

    Args:
        word (str): The current state of the hidden word.
        life (int): The current number of remaining lives.

    Returns:
        bool: True if the game should end, False otherwise.
    """
    if "_" in word and life > 0:
        return False
    elif "_" not in word and life > 0:
        print("Congratulations, you guessed the word!")
        return True
    elif life == 0:
        print("Game over")
        print("   ___________")
        print("   |         _|_")
        print("   |        /   \\")
        print("   |       |     |")
        print("   |        \\_ _/")
        print("   |         _|_")
        print("   |        / | \\")
        print("   |         / \\")
        print("___|___     /   \\")
        return True
def hangman_game():
    """
    Executes the Hangman game.

    The player needs to guess letters in a randomly chosen word. They have a limited number
    of lives, and each incorrect guess reduces the remaining lives. The game continues until
    the player guesses the word correctly or runs out of lives.
    """
    words = ["apple", "banana", "orange"]
    choice = random_word(words)
    life = 5
    hidden = hidden_word(choice)
    print("Welcome to the game!")
    print(hidden)

    while True:
        let = input(f"You have {life} life, please choose a letter: ")
        hidden = check_correct(let, hidden, choice)
        life = check_life(let, choice, life)
        if check_sit(hidden, life):
            break
        print(hidden)

hangman_game()

#~~~~~~~~~~~~~~~~~~test~~~~~~~~~~~~~~~~~~~~~~
if __name__ == '__main__':
    # add your tests here
    pass