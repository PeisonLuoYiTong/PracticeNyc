#Ask user to give a number and identify if the number is odd or even. Even numbers are divisible by 2, which means if divided by 2 they give a remainder of zero.

#try
try:
#tyoe number
    user_input = int(input("input your number: "))
#odd/even check
    if user_input % 2 == 0:
        print("even")
    elif user_input % 2 == 1:
        print("odd")
    else:
        print("error")
except:
    print("error")
