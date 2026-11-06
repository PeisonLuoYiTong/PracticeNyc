# Check if a word given by the user is a palindrome or not. Example of a palindromes: "kayak", "level", "was it a car or a cat i saw".

user_input = input("input word: ").upper()
# use a slice that steps backwards, -1
txt = user_input.replace(" ","")[::-1]
#  the slice staetment [::-1] means start at the end of the string and end at position 0, move with the step -1, negative one, which means one step backawrds
if txt == user_input:
    print(f"The word \033[95m{user_input}\033[0m IS a Palindrome.")
else:
    print(f"The word \033[91m{user_input}\033[0m is NOT a Palindrome.")
