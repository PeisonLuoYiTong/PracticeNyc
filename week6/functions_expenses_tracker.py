import csv
from datetime import datetime

def display_menu(name) -> str:
    print("===== EXPENSES TRACKER =====")
    print("press 1 to Add Expense")
    print("press 2 to see Total Expenses in certain Category")
    print("press 3 to see Total Expenses")
    if name == "The Pointy Hair Boss":
        print("press 4 to Bulk Buy Regaine")
    print("press 0 to Exit")

def add_expense(file):
    print("Adding Expense:")
    cate = input("Enter Category Purchased: ")
    try:
        expe = float(input("Enter Money Spent: "))
    except ValueError:
        print("try again")
    date = str(datetime.now())
    # print(date)
    file.write(f"{cate.capitalize()},{expe},{date}\n")
    # with open("week6/categories.csv", "a") as categories, open("week6/categories.csv", "r") as categories_reader, open("week6/categories.csv", "w", newline="") as categories_write_dangerous:
    #     is_cate_exist = False
    #     for row_number, row in enumerate(categories_reader, start = 2):
    #         if cate == row[1]:
    #             is_cate_exist = True
    # write_into_categories_csv(cate,expe)
    print("Expense Logged Succsessfully")

def total_expenses_of_category():
    print("===== YOUR CATEGORIES =====")
    categories = {}
    with open("week6/expenses.csv") as file:
        reader = csv.DictReader(file)
        is_cate_exist = False
        cate = input("Enter Category: ").capitalize()
        total = 0
        for row in reader:
            if cate == row['category']:
                print(f"You Purchased a {cate} for {row['amount']} on {row['datetime']}.")
                is_cate_exist = True
                total += float(row["amount"])
        if not is_cate_exist:
            print("Category Not Found.")
        else:
            print(f"Total amount of {cate} Purchased: {total}")
            # cate = row['category']
            # expe = row['amount']
            # date = row['datetime']
            # categories[cate] = f"{expe}$, {date}"

def v2_total_expenses_of_category():
    """The better function to v1"""
    with open("week6/expenses.csv") as file:
        reader = csv.DictReader(file)
        cate = input("Enter Category: ").capitalize()
        is_cate_exist = False
        times_item_purchased = 0
        total = 0
        for row in reader:
            if cate == row['category']:
                is_cate_exist = True
                print(f"You Purchased a {row['category']} for {row['amount']}$ on {row['datetime']}")
                total += float(row["amount"])
                times_item_purchased += 1
        if not is_cate_exist:
            print("Category Not Found.")
        else:
            print(f"You Purchased {row['category'].capitalize()} {times_item_purchased} times")
            total = f"{total:.2f}"
            print(f"Total:{c_color(total, 3)}$")

# i know im close, but im stuck here
# def write_into_categories_csv(cate, expe):
#         # exercise said to load categories from another file so i guess im writing this block below but idk what exercise wants me to do
        
#         totals = {}
#         with open("week6/categories.csv", newline="") as cate_file_reader:
#             cate_reader = csv.DictReader(cate_file_reader)
#             # keep = {}
#             for row in cate_reader:
#                 # if cate == row['category']:
#                     totals[row['category']] = float(row['total'])
#                 #     # print(totals)
#                 # else:
#                 #     keep[row['category']] = float(row['total'])
#             if cate == totals[row['category']]:
#                 totals[row['category']] += expe
#             else:
#                 totals[row['category']] = expe

#         with open("week6/categories.csv", "w", newline="") as cate_file:
#             writer = csv.writer(cate_file)
#             writer.writerow(["category","total"])
#             for category_name, num in totals.items():
#                 writer.writerow([category_name, f"{num:.2f}"])

#okay thjis is the easy part
def calculate_total_spent():
    with open("week6/expenses.csv") as file:
        reader = csv.DictReader(file)
        total = 0
        for row in reader:
            total += float(row['amount'])
        total = f"{total:.2f}"
        return total

def c_color(string:str, n:int):
    """c stands for change, passes string and n stands for color number"""
    # print(f"\033[9{n}m{string}\033[0m")
    result = f"\033[9{n}m{string}\033[0m"
    return result

def bulk_buy_hairgrowth_product(n:int):
    with open("week6/expenses.csv", "a") as file:
        for times in range(n):
            file.write(f"Regaine,57.89,{str(datetime.now())}\n")
    print(f"{n} Regaine Successfully Purchased.")

    
if __name__ == "__main__":
    v2_total_expenses_of_category()

# i came back next day and realized the block below is completely not needed mb
# def update_category_total(category, amount):
#     totals = {}
#     # read the current totals
#     with open("week6/categories.csv", newline="") as file:
#         reader = csv.DictReader(file)

#         for row in reader:
#             totals[row['category']] = float(row['total'])

#     # add to the existing category total or create a new total
#     if category in totals:
#         totals[category] += amount
#     else:
#         totals[category] = amount

#     # rewrite the file with the updated totals
#     with open("week6/categories.csv", "w", newline="") as file:
#         writer = csv.writer(file)
#         writer.writerow(["category", "total"])
#         for category_name, total in totals.items():
#             writer.writerow([f"{category_name}", f"{total}"])

# a with block doesnt create a separate variable scope, it manages the file, but it doesnt hide variables created inside it

# File "c:\Users\123\Desktop\LocalScripts\Homework\week6\functions_expenses_tracker.py", line 94, in write_into_categories_csv
#     writer.writerow(f"{str(category_name)}", f"{num:.2f}")
#     ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# TypeError: writer.writerow() takes exactly one argument (2 given)
# it should only take 1 argument which means it should be 

# print(datetime.now())