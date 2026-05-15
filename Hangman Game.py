import random


def display_hangman(attempts):
    stages = [
        """
           -----
           |   |
           O   |
          /|\  |
          / \  |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|\  |
          /    |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|\  |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        =========
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        =========
        """,
        """
           -----
           |   |
               |
               |
               |
               |
        =========
        """
    ]

    return stages[attempts]


# List of predefined words
words = ["python", "computer", "programming", "developer", "keyboard"]

# Randomly select a word
secret_word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Number of attempts
attempts = 6

print("\n Welcome to Hangman Game")
print("Guess the word one letter at a time.")

while attempts > 0:
    display_word = ""

    # Display guessed letters and underscores
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Remaining Attempts:", attempts)

    # Check if word is guessed completely
    if "_" not in display_word:
        print("\n Congratulations! You guessed the word correctly.")
        break

    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print(" Please enter only one alphabet letter.")
        continue

    # Check repeated guess
    if guess in guessed_letters:
        print(" You already guessed this letter.")
        continue

    guessed_letters.append(guess)

    # Check correct or wrong guess
    if guess not in secret_word:
        attempts -= 1
        print(" Wrong guess!")
    else:
        print(" Correct guess!")

# If attempts finish
if attempts == 0:
    print(f"\n Game Over! The word was: {secret_word}")