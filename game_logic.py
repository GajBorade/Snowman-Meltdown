import random
import ascii_art

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """
    Selects a random word from the list.

    :return: A random word from the list.
    """
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    """
    Displays the current state of the game including:
    - The snowman ASCII art corresponding to the number of mistakes.
    - The secret word with guessed letters revealed and unguessed letters shown as underscores.

    :param mistakes: int
        The number of incorrect guesses the player has made so far.
    :param secret_word: str
        The word the player is trying to guess.
    :param guessed_letters: list of str
        The letters that the player has guessed correctly or incorrectly.

    :return: None
        Prints the current snowman stage and the word display to the console.
    """
    # Display the snowman stage for the current number of mistakes.
    print(ascii_art.STAGES[min(mistakes, len(ascii_art.STAGES) - 1)])

    # Build a display version of the secret word.
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("Word: ", display_word)
    print("\n")


def get_valid_guess(guessed_letters):
    """
    Prompts the user to enter a single alphabetical letter as a guess.
    Ensures that the input is:
      - Exactly one character
      - Alphabetical (A-Z or a-z)
      - Not already guessed

    :param guessed_letters: list of str
        The letters that have already been guessed, used to prevent duplicates.

    :return: str
        A single lowercase letter representing the user's valid guess.
    """
    while True:
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetical character.")
            continue

        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try another letter.")
            continue

        return guess


def confirm_replay():
    """
    Prompts the user to confirm a replay.
    Only accepts 'y' or 'n' (case-insensitive) as valid input.

    :return: bool
        True if user wants to replay, False otherwise.
    """
    while True:
        replay = input("Do you want to play again? (y/n):").strip().lower()
        if replay == "n":
            print("Thank you for playing."
                  "Have a nice day!"
            )
            return False

        elif replay == "y":
            return True

        else:
            print("Please enter either 'y' or 'n' (case-insensitive).")


def play_game():
    """
    Runs the Snowman Meltdown game loop.

    Game flow:
      1. Selects a random secret word.
      2. Initializes the list of guessed letters and mistake counter.
      3. Displays the current game state (snowman ASCII art and masked word).
      4. Continuously prompts the player for guesses until:
         - The word is fully guessed (win), or
         - The maximum number of mistakes is reached (loss).
      5. Updates the guessed letters list and mistake counter.
      6. Displays messages for repeated guesses, correct guesses, or game over.

    :return: None

    """
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0

    print("Welcome to Snowman Meltdown!")

    display_game_state(mistakes, secret_word, guessed_letters)

    while True:
        guess = get_valid_guess(guessed_letters)

        if guess in secret_word:
            print("You guessed:", guess)
            guessed_letters.append(guess)

            display_game_state(mistakes, secret_word, guessed_letters)

            if all(letter in guessed_letters for letter in secret_word):
                print("Congratulations on saving the snowman!")
                break
        else:
            mistakes += 1
            display_game_state(mistakes, secret_word, guessed_letters)
            if mistakes >= ascii_art.MAX_MISTAKES:
                print(
                    "Sorry, you could not save the snowman!" " The secret word was:",
                    secret_word,
                )
                break
