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

* When users have input their name successfully, they will then be faced with a choice of difficulties:

![Screenshot of difficulty choice:](assets/readme/input_validation/cd_open.png)

* If they do not input the correct character, either 1, 2, or 3, then the following happens:

![Screenshot of invalid input](assets/readme/input_validation/cd_invalid_input.png)

* If they enter the correct input, such as below...:

![Screenshot of correct input](assets/readme/input_validation/cd_correct_input.png)

* They will then pass to the game stage, with confirmation of their chouce printed at the top of the terminal.

![Screenshot of confirmation of correct choice](assets/readme/input_validation/cd_confirmation.png)

![]()


### Guess letter input

* If a user enters a letter, and that letter has not already been guessed, and the letter appears in the word, then they receive the following messages:

![Screenshot showing successful guess:](assets/readme/input_validation/letter_input_correct.png)

* If a user enters a letter that has already been guessed, they will see the following messages printed:

![Screenshot showing letter already guessed:](assets/readme/input_validation/letter_already_guessed.png)

* If a user enters a letter, and this does not appear in the word, then they will see the following messages:

![Screenshot showing an incorrect guess:](assets/readme/input_validation/incorrect_answer.png)

* If a user enters an invalid guess, i.e a number or a symbol, then they will receive the following message:

![Screenshot showing an invalid guess:](assets/readme/input_validation/invalid_guess.png)


### End game input

* Upon finishing a game, either winning or losing, the user will have the choice as to whether or not to play again:

![Screenshot of end game options:](assets/readme/input_validation/end_game_options.png)

* If the user inputs y, as in the screenshot below:

![Screenshot of input of y on end game function:](assets/readme/input_validation/end_game_y.png)

* They will be re-directed to the choose difficulty function, and can start a new game:

![Screenshot showing the result of an input of y:](assets/readme/input_validation/restart_game_choose_difficulty.png)

* If the user enters invalid input, they will see the following message:

![Screenshot showing invalid put for the end game function:](assets/readme/input_validation/end_game_invalid_command.png)

* If the user enters n, then the game ends and they will see this message:

![Screenshot showing message on exiting the game:](assets/readme/input_validation/end_game_n.png)


## __Flowchart__


![Picture of flowchart](assets/readme/flowchart/hangman_flowchart.png)

![]()

## __Testing__

## __Bugs__

## __Credits__

* When researching this project, I did a lot of research on the best way to structure the code, e.g, should everything be within one function or not, which features should come in which order. I found [this Youtube Video](https://www.youtube.com/watch?v=m4nEnsavl6w&ab_channel=Kite) which proved very helpful. A link to the github repository used for the code in the video can be found by clicking [here](https://github.com/kiteco/python-youtube-code/tree/master/build-hangman-in-python).
* I also used [this](https://inventwithpython.com/invent4thed/chapter8.html) website in order to gather ideas for the structure of the code.
* The most complicated part of the code for me to code was on lines 186-189 on run.py. By studying both [this](https://stackoverflow.com/questions/41747017/python-hangman-removing-blanks-from-the-answer-pool-and-refining-what-can-be-in) answer and [this](https://stackoverflow.com/questions/26937153/python-hangman-replacing-letters) one on stack overflow, I was able to understand exactly what problems I was having. 



