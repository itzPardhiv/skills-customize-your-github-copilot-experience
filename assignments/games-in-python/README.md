
# 📘 Assignment: Hangman Game

## 🎯 Objective

Build a Hangman game in Python to practice string handling, loops, conditionals, and user input. The game should let players guess letters until they either solve the word or run out of attempts.

## 📝 Tasks

### 🛠️ Build Word Selection

#### Description
Create a list of words and randomly choose one as the hidden word for the game.

#### Requirements
Completed program should:

- Define a list of possible words.
- Choose a word at random from that list.
- Keep the chosen word hidden from the player.

### 🛠️ Implement Gameplay Loop

#### Description
Create the main loop that accepts letter guesses, updates the revealed word state, and tracks remaining attempts.

#### Requirements
Completed program should:

- Ask the player to guess a letter.
- Reveal correctly guessed letters in the hidden word using `_` for unknown letters.
- Track and display letters that have already been guessed.
- Reduce remaining attempts for incorrect guesses.

### 🛠️ Add End-Game Messages

#### Description
Show a winning or losing message when the player finishes the game.

#### Requirements
Completed program should:

- End the game when the player guesses the full word.
- End the game when the player runs out of attempts.
- Print a success message if the word is guessed.
- Print a game-over message and reveal the word if attempts run out.
