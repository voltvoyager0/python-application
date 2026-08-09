"""
Personal Budget Tracker
------------------------
A simple command-line application that demonstrates the use of
Python LISTS and FUNCTIONS to manage personal income and expenses.
"""

# ---------------------------------------------------------------
# Global list that stores all transactions.
# Each transaction is a dictionary: {"type", "category", "amount", "note"}
# ---------------------------------------------------------------
transactions = []


# ---------------------------------------------------------------
# FUNCTIONS
# ---------------------------------------------------------------

def add_transaction(t_type, category, amount, note=""):
    """Add a new income or expense entry to the transactions list."""
    entry = {
        "type": t_type,       # "income" or "expense"
        "category": category,
        "amount": amount,
        "note": note
    }
    transactions.append(entry)
    print(f"✅ {t_type.capitalize()} of {amount:.2f} added to '{category}'.")


def view_transactions():
    """Display all transactions currently stored in the list."""
    if not transactions:
        print("\nNo transactions recorded yet.\n")
        return

    print("\n{:<4} {:<10} {:<15} {:>10}  {}".format(
        "No.", "Type", "Category", "Amount", "Note"))
    print("-" * 55)
    for i, t in enumerate(transactions, start=1):
        print("{:<4} {:<10} {:<15} {:>10.2f}  {}".format(
            i, t["type"], t["category"], t["amount"], t["note"]))
    print()


def calculate_total(t_type):
    """Return the sum of all amounts of a given type ('income' or 'expense')."""
    return sum(t["amount"] for t in transactions if t["type"] == t_type)


def calculate_balance():
    """Return current balance = total income - total expenses."""
    return calculate_total("income") - calculate_total("expense")


def summarize_by_category():
    """Build and display a summary of expenses grouped by category."""
    categories = []          # list of unique category names seen so far
    totals = []               # parallel list of totals for each category

    for t in transactions:
        if t["type"] != "expense":
            continue
        if t["category"] in categories:
            index = categories.index(t["category"])
            totals[index] += t["amount"]
        else:
            categories.append(t["category"])
            totals.append(t["amount"])

    if not categories:
        print("\nNo expenses recorded yet.\n")
        return

    print("\nExpense Summary by Category")
    print("-" * 30)
    for cat, total in zip(categories, totals):
        print(f"{cat:<15} {total:>10.2f}")
    print()


def delete_transaction(index):
    """Remove a transaction from the list by its displayed number (1-based)."""
    if 1 <= index <= len(transactions):
        removed = transactions.pop(index - 1)
        print(f"🗑️  Removed: {removed['type']} - {removed['category']} - {removed['amount']:.2f}")
    else:
        print("⚠️  Invalid transaction number.")


def get_float_input(prompt):
    """Helper function to safely get a positive float from the user."""
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Please enter a positive number.")
                continue
            return value
        except ValueError:
            print("Invalid number, please try again.")


# ---------------------------------------------------------------
# MENU / MAIN PROGRAM LOOP
# ---------------------------------------------------------------

def show_menu():
    print("\n===== PERSONAL BUDGET TRACKER =====")
    print("1. Add income")
    print("2. Add expense")
    print("3. View all transactions")
    print("4. View balance")
    print("5. View expense summary by category")
    print("6. Delete a transaction")
    print("7. Exit")


def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-7): ").strip()

        if choice == "1":
            category = input("Income source (e.g., Salary, Gift): ")
            amount = get_float_input("Amount: ")
            note = input("Note (optional): ")
            add_transaction("income", category, amount, note)

        elif choice == "2":
            category = input("Expense category (e.g., Food, Rent): ")
            amount = get_float_input("Amount: ")
            note = input("Note (optional): ")
            add_transaction("expense", category, amount, note)

        elif choice == "3":
            view_transactions()

        elif choice == "4":
            balance = calculate_balance()
            print(f"\n💰 Current Balance: {balance:.2f}")
            print(f"   Total Income:  {calculate_total('income'):.2f}")
            print(f"   Total Expense: {calculate_total('expense'):.2f}\n")

        elif choice == "5":
            summarize_by_category()

        elif choice == "6":
            view_transactions()
            if transactions:
                try:
                    num = int(input("Enter transaction number to delete: "))
                    delete_transaction(num)
                except ValueError:
                    print("Please enter a valid number.")

        elif choice == "7":
            print("Goodbye! 👋")
            break

        else:
            print("Invalid option, please choose 1-7.")


if __name__ == "__main__":
    main()