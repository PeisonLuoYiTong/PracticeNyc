# Use the data.txt we created in class. Read the file and count how many words it contains (hint: read each line, split the line by the ' ' white space, and find the length of the generated list, then add it to a total). 
# Use the same file and count the number of characters in the file.

# pull data.txt

# read file with open()

file = open("week5/FILES/data.txt", "r")
# or: with open("week5/FILES/data.txt", "r") as file:

# reminder belwo
# "r" read the file
# "w" write or deleting existing stuff
# "a" add to the end

# # for loop and when whitespace add 1 to a counter
# words = 1 # 1 for the starting word
# for line in file:
#     for character in line.strip():
#         if character == " ":
#             words += 1
# print(f"there are {words} words")

# needed 2 for loops cuz the first first loop reads a whole line as a iteration
# file.close()

# file = open("week5/FILES/data.txt", "r")
# the blocks below wouldnt execute so im closing the file and opening it again

# nvm the block above doesnt work because a new line can start without a space

# second method using .readlines() method; return all lines in the file as a list where each line is an item in the list object

words = 0
characters = 0
lines = file.readlines()
for line in lines:
    words_in_line = line.strip().split()
    # print(words_in_lines)
    words = words + len(words_in_line)
    for character in line.replace(" ", ""):
        # print(character)
        characters += 1

file.close()

print(f"there are {words} words and {characters} characters.")

