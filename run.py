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
    word_to_guess = random.choice(easy_words)
    hidden_word = "_" * len(word_to_guess)
    already_guessed_letters = []
    lives_remaining = 10
    word_not_guessed = True
    while word_not_guessed and lives_remaining >= 1:
        print(f"You have {lives_remaining} lives remaining")
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
                if lives_remaining == 0:
                    print(f"Oh no! You've run out of lives!\nThe correct word was {word_to_guess}! ")
                    end_game()
                elif lives_remaining == 1:
                    print("Watch out! You only have one life left!")
                else:
                    print(f"You have {lives_remaining} lives remaining")
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
        else:
            print(f"Sorry, {guess} is not a valid guess.")
                    

main()


