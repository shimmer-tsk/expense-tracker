import json
import os
import argparse
from datetime import date

FILE = "expenses.json"

def load_expenses():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return []

def save_expenses(expenses):
    with open(FILE, "w") as f:
        json.dump(expenses, f, indent=4)

def add_expense(amount, description, category):
    expenses = load_expenses()
    expense = {
        "amount": amount,
        "description": description,
        "category": category,
        "date": str(date.today())
    }
    expenses.append(expense)
    save_expenses(expenses)
    print(f"Added: {description} - Rs.{amount} [{category}]")

def view_expenses():
    expenses = load_expenses()
    if not expenses:
        print("No expenses yet!")
        return
    total = 0
    for i, expense in enumerate(expenses):
        print(f"{i+1}. {expense['date']} | {expense['description']} | Rs.{expense['amount']} | {expense['category']}")
        total += expense['amount']
    print(f"\nTotal: Rs.{total:.2f}")

def delete_expense(index):
    expenses = load_expenses()
    if index < 1 or index > len(expenses):
        print("Invalid number!")
        return
    removed = expenses.pop(index - 1)
    save_expenses(expenses)
    print(f"Deleted: {removed['description']}")

def main():
    parser = argparse.ArgumentParser(description="Expense Tracker")
    subparsers = parser.add_subparsers(dest="command")

    add_parser = subparsers.add_parser("add")
    add_parser.add_argument("description", type=str)
    add_parser.add_argument("amount", type=float)
    add_parser.add_argument("category", type=str)

    subparsers.add_parser("view")

    delete_parser = subparsers.add_parser("delete")
    delete_parser.add_argument("index", type=int)

    args = parser.parse_args()

    if args.command == "add":
        add_expense(args.amount, args.description, args.category)
    elif args.command == "view":
        view_expenses()
    elif args.command == "delete":
        delete_expense(args.index)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()