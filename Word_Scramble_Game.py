"""
Word Scramble Game
-------------------
A simple console game that demonstrates the use of LISTS and FUNCTIONS
in Python.

Lists are used to:
    - store the pool of words available to play with
    - store which words have already been used in a session
    - store the player's round-by-round results (win/loss history)
    - break a word into individual letters for shuffling

Functions are used to:
    - separate each responsibility (getting words, scrambling,
      displaying rules, playing a round, showing a summary)
    - keep main() short and easy to read
"""

import random


def get_word_list():
    """Return the list of words that can appear in the game."""
    return [
        "python", "computer", "keyboard", "programming",
        "algorithm", "function", "variable", "list", "scramble"
    ]


def scramble_word(word):
    """Take a word (string) and return a scrambled version of it.

    Demonstrates converting a string into a list of letters,
    shuffling that list, then joining it back into a string.
    """
    letters = list(word)          # string -> list of letters
    if len(letters) > 1:
        while True:
            random.shuffle(letters)         # shuffles the list in place
            if "".join(letters) != word:    # avoid an "unscrambled" scramble
                break
    return "".join(letters)


def choose_word(word_list, used_words):
    """Pick a word from word_list that hasn't been used yet.

    Demonstrates building a new list (available words) using a
    list comprehension, then removing an item from a list.
    """
    available_words = [w for w in word_list if w not in used_words]

    if not available_words:          # every word has been used already
        used_words.clear()           # reset the "used" list
        available_words = list(word_list)

    word = random.choice(available_words)
    used_words.append(word)          # record that this word was used
    return word


def display_rules():
    """Print the game instructions."""
    print("=" * 45)
    print("      WELCOME TO THE WORD SCRAMBLE GAME")
    print("=" * 45)
    print("Unscramble the letters to form the correct word.")
    print("Type 'quit' at any time to exit the game.\n")


def play_round(word_list, used_words):
    """Play a single round and return True if the player guessed correctly."""
    word = choose_word(word_list, used_words)
    scrambled_word = scramble_word(word)

    print(f"\nScrambled word: {scrambled_word}")
    guess = input("Your guess: ").strip().lower()

    if guess == "quit":
        return None                  # signal that the player wants to quit
    elif guess == word:
        print("Correct! Great job!")
        return True
    else:
        print(f"Sorry, the correct word was: {word}")
        return False


def display_summary(results):
    """Print a summary of every round played, using the results list."""
    total_rounds = len(results)
    score = results.count(True)      # count() works directly on the list

    print("\n" + "=" * 45)
    print("GAME OVER")
    print("=" * 45)
    print(f"Rounds played: {total_rounds}")
    print(f"Correct answers: {score}")

    if total_rounds > 0:
        print("\nRound-by-round results:")
        for round_number, correct in enumerate(results, start=1):
            outcome = "Correct" if correct else "Incorrect"
            print(f"  Round {round_number}: {outcome}")


def main():
    display_rules()

    word_list = get_word_list()      # list of all possible words
    used_words = []                  # list tracking words already played
    results = []                     # list tracking True/False per round

    while True:
        choice = input("Press Enter to play a round or type 'quit' to exit: ")
        choice = choice.strip().lower()

        if choice == "quit":
            break

        outcome = play_round(word_list, used_words)

        if outcome is None:          # player typed 'quit' during the round
            break

        results.append(outcome)      # add this round's result to the list

    display_summary(results)


if __name__ == "__main__":
    main()