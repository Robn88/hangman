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


def main():
    hidden_word = "_" * len(word_to_guess)
    print(hidden_word)
    print(word_to_guess)
    already_guessed_letters = []
    # lives_remaining = 10
    word_not_guessed = True
    while word_not_guessed:
        print(hidden_word)
        guess = input("Please enter a letter:\n")
        if len(guess) == 1 and guess.isalpha():
            if guess in already_guessed_letters:
                print(f"You have already guessed {guess} ")
            elif guess not in word_to_guess:
                print(f"Bad luck! {guess} is not in the word!")
                already_guessed_letters.append(guess)
                print(f"Already guessed: {already_guessed_letters} ")
            else:
                print(f"Well done, {guess} is in the word!")
                already_guessed_letters.append(guess)
                convert_to_list = list(hidden_word)
                for index, underscore in enumerate(hidden_word):
                    print(index, underscore)
                for i, letter in enumerate(word_to_guess):
                    print(i, letter)
                    if guess == letter:
                        convert_to_list[i] = guess
                        hidden_word = ("".join(convert_to_list))
                                        
                    # if letter != "_" and guess == letter:
                    #     word_to_guess[i] = letter
                    #     print("".join(word_to_guess))
        

main()


"""
def practice():
    letters = [c for c in word_to_guess]
    print(letters)
    guess = input("Please enter a letter:\n")
    for i, letter in enumerate(word_to_guess):
        if guess == letter:
            print("That is correct!")
            break
        else:
            print("That is incorrect!")


practice()
"""
