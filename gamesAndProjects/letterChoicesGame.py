from random import randint

WORD_LIST = "grip arch spiders ratty amazing coat high-pitched direction learned coordinated teeny-tiny argue standing pet territory domineering adhesive account hurry educate right flood shivering cushion aftermath shrill scream delightful internal tip hysterical month abject nostalgic flat yarn spoil sharp illegal detailed hope branch grape slave dull imperfect smiling strange spotty snails didactic collar absorbing grin writing jealous prevent nonstop placid yawn smile scandalous incandescent normal pop country disastrous roof scorch pushy delicate kneel damage round milk acceptable act guarantee view excited obnoxious righteous spare perpetual dangerous smash morning matter hover return judicious bells note queen worried acoustic berserk head remove brawny".split()
LIVES = 10


def render_word(word, guessed_letters):
    rendered_word = ''
    for l in word:
        if l in guessed_letters:
            rendered_word += l
        else:
            rendered_word += '_'
    return rendered_word

def check_victory(word, guessed_letters):
    for l in word:
        if l not in guessed_letters:
            return False
    return True

def prompt():
    return input("Please guess a letter:\n")

def main():
    lives = LIVES
    word = WORD_LIST[randint(0, len(WORD_LIST)-1)]
    guessed_letters = []
    while lives >= 0:
        guess = prompt()
        if guess in guessed_letters:
            print("You guessed that already!")
            continue
        if guess not in word:
            lives -= 1
            print('Lives:', lives)
        guessed_letters.append(guess)
        if check_victory(word, guessed_letters):
            print(word)
            print("Congratulations! you won!")
            break
        print(render_word(word, guessed_letters))
    else:
        print("Too bad! You lost!")
        print("The word was:", word)

if __name__ == '__main__':
    main()