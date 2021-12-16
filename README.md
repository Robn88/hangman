# Hangman

Hangman is a word-guessing game, that runs in a terminal. The objective of the game is to find the word by guessing letters.

The live version of the website can be found by clicking [here](https://pyth-hangman.herokuapp.com/).

##  __How to play__

This game is modelled on the classic paper and pencil game of the same name. After inputting their name and choosing the difficulty, players will be presented with a series of underscores, and told how many letters are in the word. They then have 10 lives, and must successfuly find all of the letters in the word before they run out.

##  __Features__

The game features a welcome message before the name input:
![Welcome message and name input:](assets/readme/welcome_screen.png)

Upon entering a name, it presents the user wih a choice of difficulty:
![Choose difficulty input:](assets/readme/choose_difficulty.png)

Finally, the word is printed and its length is declared:
![Game start screenshot:](assets/readme/game_start.png)

##  __Input validation__

### Username input

* The user must enter a valid username, which is composed uniquely of alphabetical characters:

![Screenshot of name input with valid name](assets/readme/input_validation/name_input.png)

* If this is the case, then a greeting is printed with the name:

![Screenshot of the valid name passing through with a greeting printed:](assets/readme/input_validation/name_input_succeeded.png)

* However, if the input is invalid, using a non-alphabetical character such as a number or a symbol, the following message is printed:

![Screenshot of message printed upon invalid name entry:](assets/readme/input_validation/invalid_name_message.png)


### Choose difficulty input

* TO BE DONE WHEN BUG FIXED



### Guess letter input

* If a user enters a letter, and that letter has not already been guessed, and the letter appears in the word, then they receive the following messages:

![Screenshot showing successful guess:](assets/readme/input_validation/letter_input_correct.png)

* If a user enters a letter that has already been guessed, they will see the following messages printed:

![Screenshot showing letter already guessed:](assets/readme/input_validation/letter_already_guessed.png)

* If a user enters a letter, and this does not appear in the word, then they will see the following messages:

![Screenshot showing an incorrect guess:](assets/readme/input_validation/incorrect_answer.png)

* If a user enters an invalid guess, i.e a number or a symbol, then they will receive the following message:

![Screenshot showing an invalid guess:](assets/readme/input_validation/invalid_guess.png)


![]()