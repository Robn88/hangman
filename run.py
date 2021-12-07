# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

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
