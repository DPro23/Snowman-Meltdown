import random
from ascii_art import STAGES

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    # Display the snowman stage for the current number of mistakes.
    print(STAGES[mistakes])
    # Build a display version of the secret word.
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("Word: ", display_word)
    print("\n")


def play_game():
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0

    # For now, display the initial game state.
    print("Welcome to Snowman Meltdown!")
    # Prompt user for one guess (logic to be enhanced later)
    while True:
        display_game_state(mistakes, secret_word, guessed_letters)
        guess = input("Guess a letter: ").lower()
        print("You guessed:", guess)

        if guess in secret_word:
            guessed_letters.append(guess)
        else:
            mistakes += 1

        if mistakes == 3:
            print("The snowman didn't survive! The secret word was:", secret_word)
            display_game_state(mistakes, secret_word, guessed_letters)
            break

        elif len(guessed_letters) == len(secret_word):
            print("Congratulations, you saved the Snowman!!!")
            break
