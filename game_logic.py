import random
from ascii_art import STAGES

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown", "master", "javascript", "dev"]


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    """Displays the snowman stage for the current number of mistakes"""
    print(STAGES[mistakes])
    # Build a display version of the secret word.
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("💬Word: ", display_word, "\n")

def is_word_guessed(secret_word, letters_guessed):
    """Return True if all the letters in secret_word are in letters_guessed."""
    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    return True


def play_game():
    """Run the game loop"""
    mistakes_limit = 3
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0
    playing = True
    end_game = False

    # Print a pretty Game title.
    print('*' * 33)
    print("\u001b[1m⛄️Welcome to Snowman Meltdown!⛄️")
    print('*' * 33)

    # Ask user to guess a letter of secret_word
    while playing:
        display_game_state(mistakes, secret_word, guessed_letters)
        guess = input("🤔Guess a letter: ").lower()
        print("You guessed:", guess)

        if len(guess) != 1:
            print("‼️Please enter a single letter.")
            continue

        if guess in secret_word:
            guessed_letters.append(guess)
        else:
            mistakes += 1

        # Game over
        if mistakes == mistakes_limit:
            display_game_state(mistakes, secret_word, guessed_letters)
            end_game = True
            print("The snowman didn't survive! 🫠\nThe secret word was:", secret_word)

        # Victory
        if is_word_guessed(secret_word, guessed_letters):
            display_game_state(mistakes, secret_word, guessed_letters)
            end_game = True
            print("🏆Congratulations, you saved the Snowman!!! ⛄️🥳")

        # User can restart after the word is completed or mistakes == mistakes_limit
        while end_game:
            restart = input("🔄Would you like to play again? (y/n): ").lower()

            if restart == "y":
                play_game()

            elif restart == "n":
                playing = False
                end_game = False
                print("Thank you for playing! 👋")

            else:
                print('‼️Please enter only "y" or "n" as input.')
                continue
