import random
import ascii_art
# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]

def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    # Display the snowman stage for the current number of mistakes.
    #print(ascii_art.STAGES[mistakes])
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


def play_game():
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0

    print("Welcome to Snowman Meltdown!")

    display_game_state(mistakes, secret_word, guessed_letters)

    while True:
        guess = input("Guess a letter: ").lower()

        # Ignore repeated guesses
        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try another letter.")
            continue

        if guess in secret_word:
            print("You guessed:", guess)
            guessed_letters.append(guess)

            display_game_state(mistakes, secret_word, guessed_letters)

            if all (letter in guessed_letters for letter in secret_word):
                print("Congratulations on saving the snowman!")
                break
        else:
            mistakes += 1
            if mistakes >= ascii_art.MAX_MISTAKES:
                print("Sorry, you could not save the snowman!"
                      " The secret word was:", secret_word)
                display_game_state(mistakes, secret_word, guessed_letters)
                break