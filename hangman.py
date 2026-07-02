"""
Hangman Game
------------
A simple text-based Hangman game.
- Player guesses a word one letter at a time.
- 6 incorrect guesses allowed.
- Word is picked randomly from a small predefined list.

Key Concepts Used: random, while loop, if-else, strings, lists
"""

import random

WORDS = ["python", "hangman", "developer", "internship", "keyboard"]

MAX_WRONG_GUESSES = 6


def choose_word(word_list):
    """Pick a random word from the list."""
    return random.choice(word_list)


def display_word(word, guessed_letters):
    """Show the word with guessed letters revealed and others as underscores."""
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()


def play_hangman():
    word = choose_word(WORDS)
    guessed_letters = []
    wrong_guesses = 0

    print("=" * 40)
    print("Welcome to Hangman!")
    print(f"The word has {len(word)} letters.")
    print(f"You have {MAX_WRONG_GUESSES} incorrect guesses allowed.")
    print("=" * 40)

    while wrong_guesses < MAX_WRONG_GUESSES:
        print("\nWord: " + display_word(word, guessed_letters))
        print(f"Wrong guesses: {wrong_guesses}/{MAX_WRONG_GUESSES}")
        print("Guessed letters: " + ", ".join(guessed_letters) if guessed_letters else "Guessed letters: none")

        guess = input("Guess a letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try a different letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print(f"Good guess! '{guess}' is in the word.")
        else:
            wrong_guesses += 1
            print(f"Wrong! '{guess}' is not in the word.")

        if all(letter in guessed_letters for letter in word):
            print("\n" + "=" * 40)
            print(f"Congratulations! You guessed the word: {word.upper()}")
            print("=" * 40)
            return
        
    print("\n" + "=" * 40)
    print("Game Over! You ran out of guesses.")
    print(f"The word was: {word.upper()}")
    print("=" * 40)


def main():
    play_again = "y"
    while play_again == "y":
        play_hangman()
        play_again = input("\nPlay again? (y/n): ").lower().strip()

    print("Thanks for playing Hangman!")


if __name__ == "__main__":
    main()