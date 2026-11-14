import csv
from datetime import datetime

from functions_expenses_tracker import display_menu, add_expense, v2_total_expenses_of_category, c_color, calculate_total_spent, bulk_buy_hairgrowth_product

exit = -1
name = "The Pointy Hair Boss"
print(f"Welcome, {name}.")
while exit != 0:
    with open("week6/expenses.csv", "a") as file:
        display_menu(name)
        try: user_input = int(input("Enter Choice:"))
        except ValueError: print(f"{c_color("Invalid", 1)} Input")
        reader = csv.DictReader(file)
        match user_input:
            case 1:
                add_expense(file)
            case 2:
                v2_total_expenses_of_category()
            case 3:
                total = calculate_total_spent()
                print(f"Total Money Spent: {c_color(total, 2)}$")
            case 4:
                how_much_lol = int(input("How many Regaine would you like to purchase?: "))
                bulk_buy_hairgrowth_product(how_much_lol)
            case 0:
                print("Exiting...")
                exit = 0
            case _:
                print(f"{c_color("Invalid", 1)} Number")