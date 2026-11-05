#Password Check: Write a program which ask user to give a password and check if the password is strong. A strong password will have at least 8 characters, upper and lower case characters, digits, and special characters (!@#$%^&), at least one of each category. 

user_input = input("(password must have at least 8 characters, upper and lower case characters, digits, and special characters, password cannot contain spaces.)\ninput your password: ")

special_characters = ["!","@","#","$","%","^","&"]

password_strength = 0
have_special_character = False
good_length_password = False
have_uppercase = False
have_lowercase = False
have_digit = False
have_space = False

confirmation_password = ""

for i in user_input:
    if i in special_characters:
        have_special_character = True
    if i.islower():
        have_lowercase = True
    if i.isupper():
        have_uppercase = True
    if i.isnumeric():
        have_digit = True
    if i.isspace():
        have_space = True


if len(user_input) >= 8:
    password_strength += 1
    good_length_password = True

if have_special_character and good_length_password and have_uppercase and have_lowercase and have_digit and not have_space:
    print("wooow nice password")
    confirmation_password = input("type it again to confirm: ")
    if confirmation_password == user_input:
        print("wooooooooooooooooooooooooooooooooooooooow good")
    else:
        print("try again bruh")
else:
    # print(f"bhruhhhhhhhhh bad password:\nuppercase:{have_uppercase}\nlowercase:{have_lowercase}")
    print("bhruhhhhhhhhh bad password")
    print(f"length:{good_length_password}")
    print(f"uppercase:{have_uppercase}")
    print(f"lowercase:{have_lowercase}")
    print(f"have digit:{have_digit}")
    print(f"special character:{have_special_character}")
    print(f"have space?:{have_space}")

# print(have_special_character)

# i tried to use if i == i.upper(): btu that doiesnt work cuz integar is equal to the .upper() method of itsel;f