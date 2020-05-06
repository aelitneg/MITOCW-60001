# Problem Set 2, hangman.py
# Name: Andrew Gentile
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
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    for char in secret_word:
        if char not in letters_guessed:
            return False
    return True



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    guessed_word = ''
    for char in secret_word:
        if char in letters_guessed:
            guessed_word += char
        else:
            guessed_word += '_ '
    return guessed_word



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    available_letters = []
    for char in string.ascii_lowercase:
        available_letters.append(char)

    for char in letters_guessed:
        available_letters.remove(char)

    return ''.join(available_letters)
    


def is_valid_character(char):
    '''
    char: character to validate
    returns: tuple (boolean, [string]) string is only returned when False
    '''
    result = char in string.ascii_lowercase
    if not result:
        return (False, "Oops! That is not a valid letter.",)
    return (True,)



def is_previous_guess(char, letters_guessed):
    '''
    char: character to check if in letters_guessed
    letters_guessed: list (of letters) to check for char
    returns: tuple (boolean, [string],) string is only returned when False
    '''
    result = char in letters_guessed
    if result:
        return (True, "Oops! You've already guessed that letter.",)
    return (False,)



def is_secret_word(char, secret_word):
    '''
    char: character to check if in secret_word
    secret_word: string of secret word
    returns: boolean, True if char in secret_word, otherwise False
    '''
    result = char in secret_word
    if not result:
        return (False, "Oops! That letter is not in my word:",)
    return (True,)


def is_vowel(char):
    '''
    char: string (a letter) from the user
    return: boolean, True if vowel, otherwise False
    '''
    return char in ["a", "e", "i", "o", "u", "y"]



def print_welcome(secret_word):
    '''
    secret_word: string to print length
    '''
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", len(secret_word), " letters long.")
    print("You have 3 warnings left.")



def get_warning_string(warnings):
    '''
    warnings: int, number of warnings remaining
    return: string, text to print
    '''
    return "You have " + str(warnings) + " warnings left."



def get_no_warning_string():
    return "You have no warnings left, so you lose 1 guess"


def print_score(guesses, secret_word):
    '''
    guesses: int, number of guesses remaining
    secret_word: string, the secret word
    '''
    uniq = []
    for char in secret_word:
        if char not in uniq:
            uniq.append(char)
    print("Your total score for this game is", guesses * len(uniq))



def hangman(secret_word):
    '''
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
    '''
    print("DEBUG", "secret_word", secret_word)

    guesses = 6
    warnings = 3
    letters_guessed = []

    print_welcome(secret_word)

    while not is_word_guessed(secret_word, letters_guessed) and guesses > 0:
        print("-------------")
        print("You have", guesses, "guesses left.")
        print("Available letters:", get_available_letters(letters_guessed))
        
        guess = input("Please guess a letter:").lower()

        is_valid_character_result = is_valid_character(guess)
        if not is_valid_character_result[0]:
            if warnings:
                warnings -= 1
                print(
                    is_valid_character_result[1],
                    get_warning_string(warnings),
                    get_guessed_word(secret_word, letters_guessed)
                )
            else:
                guesses -= 1
                print(
                    is_valid_character_result[1], 
                    get_no_warning_string(),
                    get_guessed_word(secret_word, letters_guessed)
                )
            continue
        
        is_previous_guess_result = is_previous_guess(guess, letters_guessed)
        if is_previous_guess_result[0]:
            if warnings:
                warnings -= 1
                print(
                    is_previous_guess_result[1],
                    get_warning_string(warnings),
                    get_guessed_word(secret_word, letters_guessed)
                )
            else:
                guesses -= 1
                print(
                    is_previous_guess_result[1], 
                    get_no_warning_string(),
                    get_guessed_word(secret_word, letters_guessed)
                )
            continue
        
        letters_guessed.append(guess)

        is_secret_word_result = is_secret_word(guess, secret_word)
        if not (is_secret_word_result[0]):
            if is_vowel(guess):
                guesses -= 1
            guesses -= 1
            print(is_secret_word_result[1], get_guessed_word(secret_word, letters_guessed))
            continue

        print("Good Guess", get_guessed_word(secret_word, letters_guessed))

    if is_word_guessed(secret_word, letters_guessed):
        print("CCongratulations, you won!")
        print_score(guesses, secret_word)
    else:
        print("Sorry, you ran out of guesses.", "The word was", secret_word)
        



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    my_word = my_word.replace(' ', '')
    
    if len(my_word) != len(other_word):
        return False

    does_not_contain = []
    for i in range(0, len(my_word)):
        if my_word[i] == "_":
            does_not_contain.append(other_word[i])
        elif my_word[i] != other_word[i]:
            return False
        elif my_word[i] in does_not_contain:
            return False
    return True
    


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    possible_words = []

    for other_word in wordlist:
        if match_with_gaps(my_word, other_word):
            possible_words.append(other_word)
    
    print("possible word matches are:")
    print(possible_words)



def hangman_with_hints(secret_word):
    '''
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
    '''
    print("DEBUG", "secret_word", secret_word)

    guesses = 6
    warnings = 3
    letters_guessed = []

    print_welcome(secret_word)

    while not is_word_guessed(secret_word, letters_guessed) and guesses > 0:
        print("-------------")
        print("You have", guesses, "guesses left.")
        print("Available letters:", get_available_letters(letters_guessed))
        
        guess = input("Please guess a letter:").lower()

        if (guess == "*"):
            show_possible_matches(get_guessed_word(secret_word, letters_guessed))
            continue

        is_valid_character_result = is_valid_character(guess)
        if not is_valid_character_result[0]:
            if warnings:
                warnings -= 1
                print(
                    is_valid_character_result[1],
                    get_warning_string(warnings),
                    get_guessed_word(secret_word, letters_guessed)
                )
            else:
                guesses -= 1
                print(
                    is_valid_character_result[1], 
                    get_no_warning_string(),
                    get_guessed_word(secret_word, letters_guessed)
                )
            continue
        
        is_previous_guess_result = is_previous_guess(guess, letters_guessed)
        if is_previous_guess_result[0]:
            if warnings:
                warnings -= 1
                print(
                    is_previous_guess_result[1],
                    get_warning_string(warnings),
                    get_guessed_word(secret_word, letters_guessed)
                )
            else:
                guesses -= 1
                print(
                    is_previous_guess_result[1], 
                    get_no_warning_string(),
                    get_guessed_word(secret_word, letters_guessed)
                )
            continue
        
        letters_guessed.append(guess)

        is_secret_word_result = is_secret_word(guess, secret_word)
        if not (is_secret_word_result[0]):
            if is_vowel(guess):
                guesses -= 1
            guesses -= 1
            print(is_secret_word_result[1], get_guessed_word(secret_word, letters_guessed))
            continue

        print("Good Guess", get_guessed_word(secret_word, letters_guessed))

    if is_word_guessed(secret_word, letters_guessed):
        print("CCongratulations, you won!")
        print_score(guesses, secret_word)
    else:
        print("Sorry, you ran out of guesses.", "The word was", secret_word)
    



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    #secret_word = choose_word(wordlist)
    #hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
