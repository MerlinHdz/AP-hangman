import random
import time
from word_choices import word_list # Importing a list of words from another file


def word_generator(level, word_list):
    # This function will take the user's level choice (easy, medium or hard) and 
    # return a word based on it. 
    word_random = ''
    
    if level == "E": #4-5 characters
        while len(word_random) not in range(3,6):
            word_random = random.choice(word_list)
            return word_random.upper()
    if level == "M": #6-9
        while len(word_random) not in range(6,10):
            word_random = random.choice(word_list)
            return word_random.upper()
    if level == "H": #10+
        while len(word_random) < 10:
            word_random = random.choice(word_list)
            return word_random.upper()
    
    else: # If none of the above work (the user types something else) it'll return a random word. 
        word_random = random.choice(word_list).upper()
        return word_random

def get_guess(guessed_list):
    # This function asks the user for a letter and makes sure it's valid
    # it keeps asking for a letter until it's valid -
    # and returns the value. 
    valid_input = False
    while not valid_input:
        val = input("Please guess a letter >> ").upper()
        
        if not val.isalpha(): # To make sure it's a letter.
            print("Make sure you enter a letter!")
        elif len(val) > 1: # To make sure it's not more than 1 letter. 
            print("One letter at a time!")
        elif val in guessed_list: # To make sure the letter has not been guessed. 
            print("You already guessed that letter.")
        else:
            valid_input = True


    return val
        

def print_state(attempts):
    # Handling the "animations"
    print("     _____________")
    print("    |            |")
    print("    |           " + (" O" if attempts <= 5 else ''))
    print("    |           " + ("/" if attempts <= 4 else '') + ("|" if attempts <= 3 else '') + ('\\' if attempts <= 2 else ''))
    print("    |           " + ("/" if attempts <= 1 else '') + (' \\' if attempts == 0 else ''))
    print("    |           ")
    print("    |           ")
    print("  |-----------------|")



def main():

    # greeting.
    print("TIME TO PLAY HANGMAN!")
    time.sleep(0.5)

    #getting the user's level choice
    # Based on the user's choice, the function word_generator will return a word.
    word_level = input("Choose word length. E (easy 3-5) | M (medium 6-9) | H (Hard 10+)" + '\n' + \
    "press any other key to skip  ").upper()
    word = word_generator(word_level, word_list)
    

    #General variables
    hidden_word = ["_" for i in range(len(word))] # Creating a list with "_" that will represent the hidden word.
    guessed_letters = []
    attempts = 6
    game_active = True


    # Main Loop #
    while game_active:
        
        time.sleep(0.5)
        print_state(attempts)
        print("<< You have " + str(attempts) + " attempts remaining >>")
        print("The current word is: " + " ".join(hidden_word))
        user_guess = get_guess(guessed_letters) # this function gets the user input
    

        print("...")
        time.sleep(0.5)
       
        if user_guess in word:
            guessed_letters.append(user_guess)
            print("YOU GUESSED RIGHT, " + user_guess + " IS IN THE WORD!.")
            print("______________________________________________" + '\n')

            for i in range(len(word)):
                if word[i] == user_guess:
                    hidden_word[i] = word[i]
        else:
            print(f"YOU GUESSED WRONG, {user_guess} IS NOT IN THE WORD!.")
            print("______________________________________________" + '\n')
            attempts -= 1

        if attempts == 0:         ##
            print_state(attempts) #This is just to show the very last stage of the drawing
            print("You Lost!! You did not guess the word >> " + " ".join(word) + " <<")
            game_active = False   ##

        if "_" not in hidden_word:
            print("Congrats, You've guessed the word! 🏆 >> " + " ".join(word) + " <<")
            game_active = False
        

    if not game_active:
        play_again = input("Play Again? (Y) - YES, press any other key to exit. >> ").upper()
        if play_again == "Y":
            main()
        else:
            print("GOODBYE. ")


main() # calling main function