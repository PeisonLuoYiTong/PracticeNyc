def create_name(first, last) :
    first = first.capitalize()
    last = last.capitalize()
    return first +" " + last

#ask user for first and last name
first_name = str(input("type your first name: "))
last_name = input("type your last name: ")

#full_name = create_name("spongebob", "squarepants")
full_name = create_name(first_name, last_name)

print(f"Welcome, {full_name}")