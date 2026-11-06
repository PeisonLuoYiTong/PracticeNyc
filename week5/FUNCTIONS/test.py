from Functions import square_a_number, cube_a_number, letter_grade, count_digits, cosmetic_colors_green

grade = int(input("input your grade(1-100): "))
print(cosmetic_colors_green(letter_grade(grade)))#tghis is sick
# grade_letter = letter_grade(grade)
# print(cosmetic_colors_green(grade_letter))

digit = input("count your digits: ")
print(count_digits(digit))

square = int(input("square a number: "))
print(square_a_number(square))

cube = int(input("cube a number: "))
print(cube_a_number(cube))