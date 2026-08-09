"""
Grocery Shopping List
---------------------
A simple console application that demonstrates the use of Python
LISTS (to store grocery items) and FUNCTIONS (to organize each
piece of behavior into its own reusable block).

Each menu action is handled by its own function, and the grocery
list itself is just a plain Python list that gets passed around
between functions.
"""

import os

STORAGE_FILE = os.path.join(os.path.dirname(__file__), "grocery_list.txt")


# ---------------------------------------------------------------
# File handling functions
# ---------------------------------------------------------------

def load_list():
    """Read the saved grocery list from disk into a Python list."""
    items = []
    if os.path.exists(STORAGE_FILE):
        with open(STORAGE_FILE, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    items.append(line)
    return items


def save_list(items):
    """Write the current list of items to disk, one per line."""
    with open(STORAGE_FILE, "w", encoding="utf-8") as f:
        for item in items:
            f.write(item + "\n")


# ---------------------------------------------------------------
# List-manipulation functions
# ---------------------------------------------------------------

def view_items(items):
    """Print every item currently in the list, numbered."""
    if not items:
        print("Your shopping list is empty.")
        return

    print("\nCurrent items:")
    for index, item in enumerate(items, start=1):
        print(f"{index}. {item}")


def add_item(items):
    """Ask the user for a new item and append it to the list."""
    item = input("Enter item to add: ").strip()
    if item:
        items.append(item)
        print(f"Added: {item}")
    else:
        print("No item entered.")


def remove_item(items):
    """Ask the user which item number to remove, then pop it from the list."""
    if not items:
        print("Nothing to remove. The list is empty.")
        return

    view_items(items)
    choice = input("Enter the item number to remove: ").strip()

    if not choice.isdigit():
        print("Invalid input.")
        return

    index = int(choice) - 1
    if 0 <= index < len(items):
        removed = items.pop(index)
        print(f"Removed: {removed}")
    else:
        print("Invalid item number.")


def clear_list(items):
    """Empty the entire list after asking for confirmation."""
    confirm = input("Clear all items? (y/n): ").strip().lower()
    if confirm == "y":
        items.clear()
        print("List cleared.")
    else:
        print("Clear canceled.")


# ---------------------------------------------------------------
# Menu / program flow functions
# ---------------------------------------------------------------

def display_menu():
    """Print the list of available options to the user."""
    print("\nGrocery Shopping List")
    print("1. View items")
    print("2. Add item")
    print("3. Remove item")
    print("4. Clear list")
    print("5. Save and exit")


def get_menu_choice():
    """Prompt the user for a menu selection and return it."""
    return input("Choose an option: ").strip()


def handle_choice(choice, items):
    """
    Run the function that corresponds to the user's menu choice.
    Returns True if the program should keep running, False to exit.
    """
    if choice == "1":
        view_items(items)
    elif choice == "2":
        add_item(items)
    elif choice == "3":
        remove_item(items)
    elif choice == "4":
        clear_list(items)
    elif choice == "5":
        save_list(items)
        print("List saved. Goodbye.")
        return False
    else:
        print("Enter a valid option.")

    return True


def main():
    """Program entry point: loads the list, then runs the menu loop."""
    items = load_list()
    running = True

    while running:
        display_menu()
        choice = get_menu_choice()
        running = handle_choice(choice, items)


if __name__ == "__main__":
    main()