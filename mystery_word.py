import re
import random


def easy_words(word_list):
    """
    Returns a filtered version of the word list with words only containing
    4-6 characters.
    """
    # TODO
    return [word for word in word_list if 2 < len(word) < 7]


def medium_words(word_list):
    """
    Returns a filtered version of the word list with words only containing
    6-8 characters.
    """
    # TODO
    return [word for word in word_list if 5 < len(word) < 9]


def hard_words(word_list):
    """
    Returns a filtered version of the word list with words only containing
    8+ characters.
    """
    # TODO
    return [word for word in word_list if 7 < len(word)]


def random_word(word_list):
    """
    Returns a random word from the word list.
    """
    # TODO
    return random.choice(word_list)


def display_word(word, guesses):
    """
    Returns a string that including blanks (_) and letters from the given word,
    filling in letters based upon the list of guesses.

    There should be spaces between each blank _ and each letter. Each letter
    should be capitalized for display.

    For example, if the word is BOMBARD and the letters guessed are a, b,
    and d, this function should return 'B _ _ B A _ D'.
    """
    # TODO
    list_word = list(word)
    for idx, c in enumerate(list_word):
        if c not in guesses:
            list_word[idx] = '_'
    return ' '.join(list_word).upper()


def is_word_complete(word, guesses):
    """
    Returns True if the list of guesses covers every letter in the word,
    otherwise returns False.
    """
    # TODO
    for letter in word:
        if letter not in guesses:
            return False
    return True


def get_words():
    words = open('/usr/share/dict/words').read()
    words = re.sub(r'[^A-Za-z\s]', '', words).lower().split()
    return words


def get_word(level):
    word = ''
    if level == '1':
        # Easy
        word = random_word(easy_words(get_words()))
    elif level == '2':
        # Medium
        word = random_word(medium_words(get_words()))
    else:
        word = random_word(hard_words(get_words()))

    return word

def play_again():
    while True:
        answer = input("Would you like to play again? y or n: ").lower()
        if answer not in ('y', 'n'):
            continue
        if answer == 'y':
            main()
        print("Later gater...")
        exit()


def play(chances, word):
    while chances > 0:
        guesses = []
        while True:
            # Check chances
            if chances > 1:
                print("\nYou've got {} chances left.\n".format(chances))
                if chances < 8:
                    print("So far, you've guessed: {}\n".format(', '.join(guesses)))
            elif chances == 1:
                print("\nLast chance!\n")
            else:
                print("\nHa... you lost! Your dreams of dominating Wheel of Fortune have been dashed.")
                print("\nThe word was: {}\n\n".format(word))
                play_again()

            # Get guess and validate
            guess = input("Please guess a letter: ")
            if len(guess) > 1 or guess.isdigit() == True:
                print("\nOops... {} is not letter.\n".format(guess))
                continue
            if guess in guesses:
                print("\nOops... you've already guessed {}".format(guess))
                continue 
            guesses.append(guess)

            # Check guess against word
            if guess in word:
                print("\nNice guess.\n")
                if is_word_complete(word, guesses):
                    print("hmmm... looks like you've won. Congratulations I reckon.\n\n")
                    play_again()
            else:
                print("\nTry again.\n")
                chances -= 1
            print(display_word(word, guesses))


def main():
    """
    Runs when the program is called from the command-line.

    1. Prompts the user for a difficulty level
    2. Sets up the game based upon the difficulty level
    3. Performs the game loop, consisting of:
       a. Printing the word in progress, using _ for unguessed letters
       b. Printing the number of guesses remaining
       c. Printing the letters that have been guessed so far
       d. Prompting the user for a letter to guess
    4. Finishing the game and displaying whether the user has won or lost
    5. Giving the user the option to play again
    """
    # TODO
    divider = "-" * 35
    print("\nWelcome to the Mystery Word game.")
    print(divider)
    level = '0'
    while level not in ('1', '2', '3', '4'):
        level = input("""Please select a level:

1. Easy
2. Medium
3. Hard
----------
4. Quit

Level: """)
    if level == '4':
        exit("\nYa'll come back now...")
    print(divider)
    word = get_word(level)
    print("Great! I've chosen a {} digit word.".format(len(word)))
    play(8, word)

if __name__ == '__main__':
    main()
