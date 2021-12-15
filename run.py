import random
import os
from os import system, name


def clear():
    """
    Clear function to clean-up the terminal so things don't get messy.
    """
    os.system("cls" if os.name == "nt" else "clear")


def welcome_to_game():
    """
    This function allows people to input their name.
    """
    while True:
        global name
        name = input("Please enter your name:")
        if name.isalpha() is True:
            print(f"Hello, {name}!")
            break
        else:
            print(f"Sorry, {name} is not a valid name.Please try again.")


# Welcome message
print("Welcome to hangman!")


# def choose_difficulty():



# Gets the words from the easy.txt file and stores them in a list.
easy_words = []
get_words = open('easy.txt').read().split()
for word in get_words:
    easy_words.append(word)


def end_game():
    """
    A function that is called when the game ends.
    """
    continue_playing = input("Would you like to keep playing? y / n \n")
    if continue_playing == "y":
        print("\n")
        clear()
        main()
    elif continue_playing == "n":
        clear()
        print(f"Thanks for playing {name}, see you soon!")
    else:
        print(f"Sorry, {continue_playing} is not a valid command. Please press y or n. \n")
        end_game()

        
def main():
    """
    The main function is where the bulk of the game runs. It begins by setting
    global variables, which will then be used in the loop.
    """
    word_to_guess = random.choice(easy_words)
    hidden_word = "_" * len(word_to_guess)
    already_guessed_letters = []
    lives_remaining = 10
    word_not_guessed = True
    while word_not_guessed and lives_remaining >= 1:
        """
        Start of the loop- prints a list of letters already guessed, the
        hidden word, and elicits input from the user.
        """
        print(f"Letters guessed so far: {already_guessed_letters} ")
        print(hidden_word)
        print()
        guess = input("Please enter a letter:\n")
        if len(guess) == 1 and guess.isalpha():
            """
            The first condition of the loop checks if the input is a
            single, alphabetical character.
            """
            if guess in already_guessed_letters:
                """
                Within this first condition, the next step is to check if
                the letter has already been played, and return users to
                the beginning if that is the case.
                """
                print(f"You have already guessed {guess} ")
            elif guess not in word_to_guess:
                """
                If the letter fulfills the above 2 conditions, but is not
                in the word_to_guess variable, then the letter is
                appended to the list of already guessed letters, and a
                life is deducted.
                """
                print(f"Bad luck! {guess} is not in the word!")
                already_guessed_letters.append(guess)
                lives_remaining -= 1
                if lives_remaining == 0:
                    """
                    If the number of lives remaining reaches 0, then the
                    word_to_guess is revealed, and the end_game function
                    is called.
                    """
                    print(f"Oh no!{name}, you've run out of lives!\nThe correct word was {word_to_guess}! ")
                    end_game()
                elif lives_remaining == 1:
                    """
                    If the number of lives remaining reaches 1, then
                    a warning message is printed.
                    """
                    print(f"Watch out, {name} ! You only have one life left!")
                else:
                    """
                    Finally, if the number of lives remaining is between 2 and
                    9, then a generic message is printed
                    """
                    print(f"You have {lives_remaining} lives remaining.")
            else:
                """ 
                If the letter guessed fulfills the initial criteria,i.e it is a
                single alphabetical character, has not been guessed before, and
                passes the elif statement on line 64, it must be in the word.
                The original word is converted into a list, and each letter
                is assigned an integer value. If the guess is the same as a
                letter, then the value of the convert_to_list is
                modified accordingly. Finally, the list is converted back into
                a string with the correct letters inserted. If that was the
                last letter required to complete the word, then the end_game
                function is called.
                """
                print(f"Well done, {guess} is in the word!\n")
                already_guessed_letters.append(guess)
                convert_to_list = list(hidden_word)
                # for index, underscore in enumerate(hidden_word):
                #     print(index, underscore)
                for i, letter in enumerate(word_to_guess):
                    if guess == letter:
                        convert_to_list[i] = guess
                        hidden_word = ("".join(convert_to_list))
                if "_" not in hidden_word:
                    word_not_guessed = not True
                    print(f"Congratulations {name} ! You found the word: {word_to_guess} \n")
                    end_game()
        else:
            """
            An else statement designed to catch any incorrect input.
            """
            print(f"Sorry, {guess} is not a valid guess.")


welcome_to_game()


main()
