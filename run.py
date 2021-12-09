import random


def welcome_to_game():
    while True:
        name = input("Please enter your name:")
        if name.isalpha() is True:
            print(f"Hello, {name}!")
            break
        else:
            print(f"Sorry, {name} is not a valid name.Please try again.")


print("Welcome to hangman!")
welcome_to_game()

easy_words = []
get_words = open('easy.txt').read().split()
for word in get_words:
    easy_words.append(word)

print(easy_words)

word_to_guess = random.choice(easy_words)


def create_hidden_word():
    hidden_word = "_" * len(word_to_guess)
    return hidden_word


print(create_hidden_word())

"""
def main():
    already_guessed_letters = []
    lives_remaining = 10
    word_not_guessed = True
    while word_not_guessed True:
        guess = input("Please enter a letter:\n")
"""

