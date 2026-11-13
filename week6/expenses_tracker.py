import csv
from datetime import datetime

from functions_expenses_tracker import display_menu,add_expense

exit = -1

while exit != 0:
    with open("week6/expenses.csv", "a") as file:
        display_menu("The Pointy Hair Boss")
        user_input = int(input("type int: "))
        reader = csv.DictReader(file)
        match user_input:
            case 1:
                add_expense(file)
            case 2:
                break
            case 0:
                exit = 0
            case _:
                print("Invalid Input")