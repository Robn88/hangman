# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
print("Welcome to hangman!")


def welcome_to_game():
    while name.isalpha() is not True:
        input(f"Sorry, {name} is not a valid name.Please try again:")
        if name.isalpha() is True:
            print(f"Hello, {name}!")
            break


name = input("Please enter your name:")
welcome_to_game()


"""
def welcome_to_game():
    name = input("Please enter your name:")
    while name.isalpha() is not True:
        input(f"Sorry, {name} is not a valid name.Please try again:")
    if name.isalpha():
        print(f"Hello, {name}!")  
"""
