"""a program designed to be like Wordle"""

__author__: str = "730560970"


def contains_char(search_string: str, char_search: str) -> bool:
    """determines if letter is in word guess"""
    assert (
        len(char_search) == 1
    ), f"len('{char_search}') is not 1"  # Ensure char_search is a single character
    index: int = 0
    while index < len(search_string):  # this will loop through all of search_string
        if (
            search_string[index] == char_search
        ):  # If char_search is found in search_string
            return True  # Return True if the character is found
        index += 1  # Move to the next charactern
    return False  # Return False if character is not found


def emojified(guess: str, secret: str) -> str:
    """determines if guess is correct or incorrect"""
    assert len(guess) == len(
        secret
    ), "Guess must be same length as secret"  # Ensure guess and secret are same length
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    index: int = 0
    string: str = ""
    while index < len(guess):  # this loops through all of guess
        if (
            guess[index] == secret[index]
        ):  # if guess at letter is same as secret at that letter, green box
            string += GREEN_BOX
        elif contains_char(
            secret, guess[index]
        ):  # otherwise if letter is somewhere in word, yellow box
            string += YELLOW_BOX
        else:  # if letter is not in word, white box
            string += WHITE_BOX
        index += 1
    return string


def input_guess(expected_length: int) -> str:
    """prompts user for guess of expected length until correct length is entered"""
    guess: str = input(
        f"Enter a {expected_length} character word:"
    )  # Prompt user for guess

    while (
        len(guess) != expected_length
    ):  # If the guess length doesn't match expected length, ask again
        guess = input(f"That wasn't {expected_length} chars! Try again:")

    return guess


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    guessed_correctly: bool = False  # Track if the user has guessed the word correctly
    turn_number: int = 1  # Track the current turn number

    while (
        turn_number <= 6 and guessed_correctly != True
    ):  # The loop will run until 6 turns or the user guesses correctly
        print(f"=== Turn {turn_number}/6 ===")
        guess: str = input_guess(len(secret))
        print(emojified(guess, secret))
        if guess == secret:  # If the guess is correct
            print(f"You won in {turn_number}/6 turns!")
            guessed_correctly = True
            return None  # Exit the function (game over)
        turn_number += 1
    print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")  # Start the game with "codes" as the secret word
