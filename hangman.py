# hangman.py

import random

# List of words
words = ["python", "computer", "science", "programming", "hangman", "developer"]

# Choose random word
def choose_word():
    return random.choice(words)

# Display progress
def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

# Main game
def play_hangman():
    word = choose_word()
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman Game!")
    print("Guess the word letter by letter.")

    while attempts > 0:
        print("\nWord:", display_word(word, guessed_letters))
        print("Attempts left:", attempts)
        print("Guessed letters:", guessed_letters)

        guess = input("Enter a letter: ").lower()

        # Validation
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Good guess!")
        else:
            print("Wrong guess!")
            attempts -= 1

        # Win condition
        if all(letter in guessed_letters for letter in word):
            print("\nCongratulations! You guessed the word:", word)
            return

    # Lose condition
    print("\nGame Over! The word was:", word)

# Run game
play_hangman()
