def display_invoice(user, amount, due_date):
    print(f"Hello {user}")
    print(f"Your bill of ${amount:.2f} is due: {due_date}")

#bills of ppl in a list/tuple
bills = ["joe", "mama", "deez nuts"]
amount = [42, 50, 80]
due_date = ["18/11", "09/11", "27/11"]

#ask user input
username = str(input("whats your username:"))

#boolean for checking if username in bills list
if username in bills:
    #find position of said username in bills list, using .index() function
    position = bills.index(username)

    #print message
    display_invoice(bills[position], amount[position], due_date[position])
else:
    print(f"no account found under {username}")


