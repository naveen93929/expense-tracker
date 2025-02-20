# expense_tracker.py

import csv
import os
import matplotlib.pyplot as plt  
from datetime import datetime

def add_expense():
    print("\nAdd New Expense")

    # Validate date input
    while True:
        date_input = input("Enter the date (dd-mm-yyyy): ")
        try:
            date_obj = datetime.strptime(date_input, "%d-%m-%Y")
            date_str = date_obj.strftime("%d-%m-%Y")
            break
        except ValueError:
            print("Invalid date format. Please try again.")

    # Get category input
    category = input("Enter the category (e.g., Food, Rent, etc.): ").title()

    # Validate amount input
    while True:
        amount_input = input("Enter the amount: ")
        try:
            amount = float(amount_input)
            break
        except ValueError:
            print("Invalid amount. Please try again.")

    # Get description input
    description = input("Enter a brief description: ")

    # Check csv file
    file_exists = os.path.isfile("expenses.csv")

    # Write to csv file
    with open('expenses.csv', 'a', newline='') as csvfile:
        fieldnames= ['Date', 'Category', 'Amount', 'Description']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if not file_exists:
            writer.writeheader()

        writer.writerow({
            'Date': date_str,
            'Category': category,
            'Amount': amount,
            'Description': description
        }) 
    
    print("Expense added successfully!\n")

def view_expenses():
    print("\nAll Recorded Expenses:\n")

    if not os.path.isfile('expenses.csv'):
        print("No expenses recorded yet.\n")
        return
    with open('expenses.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        total = 0.0

        for row in reader:
            print(f"Date: {row['Date']}, Category: {row['Category']}, Amount: ${float(row['Amount']):.2f}, Description: {row['Description']}")
            total += float(row['Amount'])
    print(f"\nTotal Expenses: ${total:.2f}\n")
    
def analyze_by_category():
    print("\nAnalyzing Expenses by Category\n")

    if not os.path.isfile('expenses.csv'):
        print("No expenses recorded yet.\n")
        return
    category_input = input("Enter the category to analyze: ").title()

    with open('expenses.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        total = 0.0
        count = 0

        for row in reader:
            if row['Category'].lower() == category_input.lower():
                print(f"Date: {row['Date']}, Amount: ${float(row['Amount']):.2f}, Description: {row['Description']}")
                total += float(row['Amount'])
                count += 1

    if count > 0:
       print(f"\nTotal Expenses in {category_input}: ${total:.2f}\n")
    else:
       print(f"No expenses found in category '{category_input}'.\n")

def analyze_by_date():
    print("\nAnalyze Expenses by Date Range")

    if not os.path.isfile('expenses.csv'):
        print("No expenses recorded yet.\n")
        return
    
    # Validate start date
    while True:
        start_date_input = input("Enter the start date (dd-mm-yyyy): ")
        try:
            start_date = datetime.strptime(start_date_input, "%d-%m-%Y")
            break
        except ValueError:
            print("Invalid date format. Please try again.")

    # Validate end date
    while True:
        end_date_input = input("Enter the end date (dd-mm-yyyy): ")
        try:
            end_date = datetime.strptime(end_date_input, "%d-%m-%Y")
            break
        except ValueError:
            print("Invalid date format. Please try again.")

    with open('expenses.csv','r') as csvfile:
        reader = csv.DictReader(csvfile)
        total = 0.0
        count = 0

        for row in reader:
            expense_date = datetime.strptime(row['Date'], "%d-%m-%Y")
            if start_date <= expense_date <= end_date:
                print(f"Date: {row['Date']}, Category: {row['Category']}, Amount: ${float(row['Amount']):.2f}, Description: {row['Description']}")
                total += float(row['Amount'])
                count += 1
    
    if count > 0:
        print(f"\nTotal Expenses between {start_date_input} and {end_date_input}: ${total:.2f}\n")
    else:
        print("No expenses found in this date range.\n")

def visualize_expenses():
    print("\nVisualize Expenses")

    if not os.path.isfile('expenses.csv'):
        print("No expenses recorded yet.\n")
        return
    # Gather data
    categories = {}
    with open('expenses.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            category = row['Category']
            amount = float(row['Amount'])
            categories[category] = categories.get(category, 0) + amount
    
    # Prepare data for pie chart
    labels = categories.keys()
    sizes = categories.values()

    # Plotting
    plt.figure(figsize=(8, 8))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%')
    plt.title('Expenses by Category')
    plt.show()

def main():
    print("Welcome to the Expense Tracker")
    while True:
        print("=== Personal Expense Tracker ===")
        print("1. Add New Expense")
        print("2. View All Expenses")
        print("3. Exit")
        print("4. Analyze Expenses by Category")
        print("5. Analyze Expenses by Date Range")
        print("6. Visualize Expenses")

        choice = input("Choose your option (1-6): ")
       
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            print("Exiting the Expense Tracker. Goodbye!")
            break
        elif choice == "4":
            analyze_by_category()
        elif choice == "5":
            analyze_by_date()
        elif choice == "6":
            visualize_expenses()
        else:
            print("Invalid option. Please try again.\n")

if __name__ == "__main__":
    main()
