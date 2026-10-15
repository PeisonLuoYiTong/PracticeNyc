def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"Your bill of ${amount:.2f} is due: {due_date}")

#bills of ppl in a list/tuple
bills = ["joe", "mama", "deez nuts"]
amount = [42, 50, 80]
due_date = ["18/11", "09/11", "27/11"]

#ask user input
user = str(input("whats your username:"))

if user == bills[0]:
    display_invoice(bills[0], amount[0], due_date[0])
elif user == bills[1]:
    display_invoice(bills[1], amount[1], due_date[1])
elif user == bills[2]:
    display_invoice(bills[2], amount[2], due_date[2])
else:
    print(f"no account found under {user}")
