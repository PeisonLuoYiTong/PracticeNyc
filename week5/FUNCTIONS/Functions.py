# Write two functions to calculate and return a) the square, b) the cube of a given number. 
# Write a function letter_grade(grade) which will receive a number 0-100 and return the letter grade according to this table: (see table.txt)

# Write a function to count and return the digits in a string count_digits(s). For example count_digits('abc3ui6bc8p') should return 3.

def square_a_number(a) -> int:
    """square: make a number times itself."""
    squared = a * a
    return squared

def cube_a_number(a) -> int:
    """cube: make a number times itself 3 times."""
    cubed = a * a * a
    return cubed

def letter_grade(grade) -> int:
    """receive a number 0-100 and return the letter grade according to table.txt"""
    match grade:
        case n if 1 <= n <= 59:
            result = "F"
        case n if 60 <= n <= 66:
            result = "D"
        case n if 67 <= n <= 69:
            result = "D+"
        case n if 70 <= n <= 72:
            result = "C-"
        case n if 73 <= n <= 76:
            result = "C"
        case n if 77 <= n <= 79:
            result = "C+"
        case n if 80 <= n <= 83:
            result = "B-"
        case n if 83 <= n <= 89:
            result = "B+"
        case n if 90 <= n <= 93:
            result = "A-"
        case n if 94 <= n <= 100:
            result = "A"
        case _:
            result = "invalid grade"
    return result

def count_digits(n) -> any:
    p = 0
    for i in n:
        if i.isnumeric():
            p += 1
    return p

# user_input = input("count your digits: ")
# print(count_digits(user_input))

def cosmetic_colors_green(whatever):
    result = "\033[92m" + whatever + "\033[0m"
    return result