# Code Explanation — Hangman Game (Tkinter GUI)

## 1. Basic Setup

* `MAX_ATTEMPTS = 6` → Maximum wrong guesses allowed
* `WORD_LIST` → Collection of words used in the game
* A random word is selected at the start of each game

---

## 2. Class: HangmanGUI

This class handles the entire game logic and GUI.

### Initialization (`__init__`)

* Sets up the main window (title, size, layout)

* Initializes game state:

  * `self.word` → randomly selected word
  * `self.guessed` → stores guessed letters
  * `self.attempts` → remaining attempts

* Creates UI components:

  * Canvas (for drawing hangman)
  * Labels (word display & info)
  * Entry box (user input)
  * Buttons (Guess & Restart)

* Binds **Enter key** to submit guesses

---

## 3. Drawing the Hangman

### `draw_hangman()`

* Draws the gallows (always visible)
* Adds body parts step-by-step based on mistakes:

  1. Head
  2. Body
  3. Left Arm
  4. Right Arm
  5. Left Leg
  6. Right Leg

More mistakes = more parts drawn

---

## 4. Display Update

### `update_display()`

* Updates:

  * Hangman drawing
  * Word display (`_ _ _` format)
  * Attempts left
  * Guessed letters

* Reveals letters if correctly guessed

---

## 5. User Input Handling

### `make_guess()`

* Reads input from entry box

* Validates input:

  * Must be a single alphabet
  * Must not be already guessed

* Updates game state:

  * Adds letter to guessed set
  * Reduces attempts if wrong guess

---

## 6. Win Condition

* If all letters are guessed:

  * Displays full word
  * Shows **"You won" message**
  * Disables input

---

## 7. Lose Condition

* If attempts reach 0:

  * Reveals the correct word
  * Shows **"Game Over" message**
  * Disables input

---

## 8. Input Control

### `_disable_input()`

* Disables entry and guess button after game ends

### `_enable_input()`

* Re-enables input when game restarts

---

## 9. Restart Game

### `reset_game()`

* Selects a new random word
* Clears guessed letters
* Resets attempts
* Enables input
* Updates display

---

## 10. Event Handling

* Pressing **Enter key** triggers guess submission
* Improves user experience (no need to click button every time)

---

## Overall Working

This project is a **GUI-based word guessing game**:

* User guesses letters of a hidden word
* Each wrong guess draws part of the hangman
* Game ends when:

  * Word is guessed → Win
  * Attempts run out → Lose

---

## Concepts Used

* GUI Development (Tkinter)
* Event-driven programming
* Game logic & state management
* Input validation
* Canvas drawing (graphics)

---
