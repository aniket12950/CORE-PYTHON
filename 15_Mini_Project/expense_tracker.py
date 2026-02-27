"""
Project: Smart Expense Tracker
Description: Track daily expenses and generate summary report
"""

import csv
import os
from datetime import datetime

FILE_NAME = "expenses.csv"


def add_expense():
    date = datetime.now().strftime("%Y-%m-%d")
    category = input("Enter category (Food, Travel, Bills, etc.): ")
    amount = float(input("Enter amount: "))
    note = input("Enter note: ")

    file_exists = os.path.isfile(FILE_NAME)

    with open(FILE_NAME, mode="a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Date", "Category", "Amount", "Note"])
        writer.writerow([date, category, amount, note])

    print(" Expense added successfully!")


def show_report():
    if not os.path.exists(FILE_NAME):
        print(" No expense data found.")
        return

    total = 0
    category_summary = {}
    highest_expense = 0
    highest_record = None

    with open(FILE_NAME, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            amount = float(row["Amount"])
            total += amount

            category = row["Category"]
            category_summary[category] = category_summary.get(category, 0) + amount

            if amount > highest_expense:
                highest_expense = amount
                highest_record = row

    print("\n Expense Report")
    print("-" * 30)
    print(f"Total Spending: ₹{total}")

    print("\nCategory-wise Spending:")
    for category, amount in category_summary.items():
        print(f"{category}: ₹{amount}")

    if highest_record:
        print("\n Highest Expense:")
        print(f"{highest_record['Date']} - {highest_record['Category']} - ₹{highest_record['Amount']} ({highest_record['Note']})")


def main():
    while True:
        print("\n=== Smart Expense Tracker ===")
        print("1. Add Expense")
        print("2. Show Report")
        print("3. Exit")

        choice = input("Choose option (1-3): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            show_report()
        elif choice == "3":
            print(" Exiting... Stay financially smart!")
            break
        else:
            print(" Invalid choice!")


if __name__ == "__main__":
    main()