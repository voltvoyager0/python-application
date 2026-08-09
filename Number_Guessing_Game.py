"""
Number Guessing Game
Demonstrates the use of functions and lists in Python.
"""

import random


def get_computer_number(low, high):
    """Generate and return a random number between low and high (inclusive)."""
    return random.randint(low, high)


def get_player_guess(low, high):
    """Prompt the player for a guess and validate it's an integer in range."""
    while True:
        raw_input_value = input(f"Guess a number between {low} and {high}: ")
        try:
            guess = int(raw_input_value)
        except ValueError:
            print("That's not a valid number. Try again.")
            continue

        if guess < low or guess > high:
            print(f"Please enter a number between {low} and {high}.")
            continue

        return guess


def check_guess(guess, target):
    """Compare the guess to the target and return a hint string."""
    if guess < target:
        return "Too low!"
    elif guess > target:
        return "Too high!"
    else:
        return "Correct!"


def print_guess_history(history):
    """Print all guesses made so far, using the list of past guesses."""
    print("Your guesses so far:", ", ".join(str(g) for g in history))


def play_round(low=1, high=100):
    """Play a single round of the guessing game. Returns the number of attempts."""
    target = get_computer_number(low, high)
    guess_history = []          # list storing every guess made this round
    attempts = 0

    print("\nI'm thinking of a number... Let's see if you can find it!")

    while True:
        guess = get_player_guess(low, high)
        guess_history.append(guess)   # add guess to the list
        attempts += 1

        result = check_guess(guess, target)
        print(result)

        if result == "Correct!":
            print(f"You got it in {attempts} attempts.")
            print_guess_history(guess_history)
            return attempts

        print_guess_history(guess_history)


def play_game():
    """Main game loop. Keeps a list of scores across multiple rounds."""
    scores = []   # list storing attempts taken in each round played

    print("=== Welcome to the Number Guessing Game ===")

    while True:
        attempts_taken = play_round()
        scores.append(attempts_taken)

        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != "y":
            break

    show_summary(scores)


def show_summary(scores):
    """Print a summary of all rounds played using the scores list."""
    if not scores:
        print("No rounds played. Goodbye!")
        return

    print("\n=== Game Summary ===")
    for round_number, attempts in enumerate(scores, start=1):
        print(f"Round {round_number}: {attempts} attempts")

    best = min(scores)
    average = sum(scores) / len(scores)
    print(f"\nBest round: {best} attempts")
    print(f"Average attempts: {average:.2f}")
    print("Thanks for playing!")


if __name__ == "__main__":
    play_game()