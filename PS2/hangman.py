# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    """
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    """
    is_guessed = True
    for char in secret_word:
        if char in letters_guessed:
            continue
        else:
            is_guessed = False
    return is_guessed


def get_guessed_word(secret_word, letters_guessed):
    """
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    """
    guessed_word = []
    for char in secret_word:
        if char in letters_guessed:
            guessed_word.append(char)
        else:
            guessed_word.append("_")
    guessed_word_str = " ".join(guessed_word)
    return guessed_word_str


def get_available_letters(letters_guessed):
    """
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    """
    available_letters = []
    for char in string.ascii_lowercase:
        if char in letters_guessed:
            continue
        else:
            available_letters.append(char)
    available_letters_str = "".join(available_letters)
    return available_letters_str


def hangman(secret_word):
    """
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    Follows the other limitations detailed in the problem write-up.
    """

    # Initialize variables and print welcome message.
    length = len(secret_word)
    guesses_remaining = 6
    warnings = 3
    letters_guessed = []
    avail_letters = get_available_letters(letters_guessed)

    print("Welcome to the game Hangman!")
    print(f"I am thinking of a word that is {length} letters long.")

    while not is_word_guessed(secret_word, letters_guessed):
        print("-------------")
        if guesses_remaining == 1:
            print(f"You have {guesses_remaining} guess left.")
        else:
            print(f"You have {guesses_remaining} guesses left.")
        print(f"Available letters: {avail_letters}")

        guess = input("Please guess a letter: ")

        # Validate user input is an alpha character
        if not str.isalpha(guess):
            if warnings > 0:
                warnings -= 1
            else:
                guesses_remaining -= 1
                if guesses_remaining == 0:
                    break
            print(f"Oops! That is not a valid letter. You have {warnings} warnings left: {get_guessed_word(secret_word, letters_guessed)}")

        else:
            # Check to see if user input has already been guessed
            guess = guess.lower()
            if guess in letters_guessed:
                if warnings > 0:
                    warnings -= 1
                    print(f"Oops! You've already guessed that letter. You have {warnings} warnings left: {get_guessed_word(secret_word, letters_guessed)}")
                else:
                    guesses_remaining -= 1
                    if guesses_remaining == 0:
                        break
                    print(f"Oops! You've already guessed that letter. You have no warnings left so you lose one guess: {get_guessed_word(secret_word, letters_guessed)}")

            else:
                # Check if guessed letter is in secret word.
                letters_guessed.append(guess)
                avail_letters = get_available_letters(letters_guessed)
                if guess not in secret_word:
                    if guess in "a,e,i,o,u":
                        guesses_remaining -= 2
                    else:
                        guesses_remaining -= 1
                    if guesses_remaining == 0:
                        break
                    print("Oops! That letter is not in my word.")
                    print(f"Please guess a letter: {get_guessed_word(secret_word, letters_guessed)}")
                else:
                    print(f"Good guess: {get_guessed_word(secret_word, letters_guessed)}")

    # Outcome of a losing game
    if guesses_remaining == 0:
        print(f"Sorry, you ran out of guesses.  The word was: {secret_word}")

    # Outcome of a winning game
    if is_word_guessed(secret_word, letters_guessed):
        print("Congratulations, you won!")
        score = guesses_remaining * len(secret_word)
        print(f"Your total score for this game is: {score}")


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
# (hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------


def match_with_gaps(my_word, other_word):
    """
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise:
    """
    my_word = my_word.replace(" ", "").strip()
    if len(my_word) != len(other_word):
        return False
    for index, char in enumerate(my_word):
        if my_word[index] == other_word[index]:
            continue
        else:
            return False
    return True


def show_possible_matches(my_word):
    """
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    """
    match_list = []
    for word in wordlist:
        if match_with_gaps(my_word, word):
            match_list.append(word)
    match_list = " ".join(match_list)
    print(match_list)


def hangman_with_hints(secret_word):
    """
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word.

    Follows the other limitations detailed in the problem write-up.
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass


# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.

    secret_word = choose_word(wordlist)
    hangman(secret_word)

###############

# To test part 3 re-comment out the above lines and
# uncomment the following two lines.

# secret_word = choose_word(wordlist)
# hangman_with_hints(secret_word)
