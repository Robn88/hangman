import random

"""
def welcome_to_game():
    while True:
        name = input("Please enter your name:")
        if name.isalpha() is True:
            print(f"Hello, {name}!")
            break
        else:
            print(f"Sorry, {name} is not a valid name.Please try again.")
"""

print("Welcome to hangman!")
# welcome_to_game()

easy_words = []
get_words = open('easy.txt').read().split()
for word in get_words:
    easy_words.append(word)


word_to_guess = random.choice(easy_words)

"""
def create_hidden_word():
    hidden_word = "_" * len(word_to_guess)
    return hidden_word


print(create_hidden_word())
"""


def end_game():
    continue_playing = input("Would you like to keep playing? y / n \n")
    if continue_playing == "y":
        print("\n")
        main()
    elif continue_playing == "n":
        print("Thanks for playing, see you soon!")
    else:
        print(f"Sorry, {continue_playing} is not a valid command. Please press y or n. \n")
        end_game()
                        

def main():
    hidden_word = "_" * len(word_to_guess)
    already_guessed_letters = []
    lives_remaining = 10
    word_not_guessed = True
    while word_not_guessed:
        print(hidden_word)
        print("\n")
        guess = input("Please enter a letter:\n")
        if len(guess) == 1 and guess.isalpha():
            if guess in already_guessed_letters:
                print(f"You have already guessed {guess} ")
            elif guess not in word_to_guess:
                print(f"Bad luck! {guess} is not in the word!")
                already_guessed_letters.append(guess)
                lives_remaining -= 1
            else:
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
                    print(f"Congratulations! You found the word: {word_to_guess} \n")
                    end_game()
                    # while True:
                    #     continue_playing = input("Would you like to keep playing? y / n \n")
                    #     if continue_playing == "y":
                    #         print("\n")
                    #         main()
                    #     elif continue_playing == "n":
                    #         print("Thanks for playing, see you soon!")
                    #         break
                    #     else:
                    #         print(f"Sorry, {continue_playing} is not a valid command. Please press y or n. \n")


main()


