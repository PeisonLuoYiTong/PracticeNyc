import csv
from datetime import datetime

def display_menu(name):
    print("===== EXPENSES TRACKER =====")
    print(f"Welcome, {name}.")
    print("press 1 to Add Expense")
    print("press 2 to see Total Expenses in certain Category")
    print("press 3 to see Total Expenses")
    print("press 0 to Exit")

def add_expense(file):
    print("Adding Expense:")
    cate = input("Please enter Category Purchased: ")
    try:
        expe = float(input("Please enter Money Spent: "))
    except ValueError:
        print("try again")
    date = str(datetime.now())
    # print(date)
    file.write(f"{cate},{expe},{date}\n")
    # with open("week6/categories.csv", "a") as categories, open("week6/categories.csv", "r") as categories_reader, open("week6/categories.csv", "w", newline="") as categories_write_dangerous:
    #     is_cate_exist = False
    #     for row_number, row in enumerate(categories_reader, start = 2):
    #         if cate == row[1]:
    #             is_cate_exist = True
    update_category_total(cate,expe)
    print("Expense Logged Succsessfully")
    
def update_category_total(category, amount):
    totals = {}
    # read the current totals
    with open("week6/categories.csv", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            totals[row["category"]] = float(row["total"])

    # add to the existing category total or create a new total
    if category in totals:
        totals[category] += amount
    else:
        totals[category] = amount

    # rewrite the file with the updated totals
    with open("week6/categories.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["category", "total"])
        for category_name, total in totals.items():
            writer.writerow([f"{category_name}", f"{total}"])

def total_expenses_of_category():
    print("===== YOUR CATEGORIES =====")
    categories = {}
    with open("week6/expenses.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            cate = row['category']
            expe = row['amount']
            date = row['datetime']
            categories[cate] = f"{expe}$, {date}"
        print(categories)
    

# total_expenses_of_category()

# print("Adding Expense:")
# cate = input("Please enter Category Purchased: ")
# try:
#     expe = float(input("Please enter Money Spent: "))
# except ValueError:
#     print("try again")
# date = str(datetime.now())
# # print(date)
# file.write(f"{cate},{expe},{date}\n")
# print("Expense Logged Succsessfully")

print(datetime.now())