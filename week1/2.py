
#Ask user for a temperature in Celsius (this will be a floating point number, so you need to read with float(input("Give Celsius temperature: "). Then, calculate and print the conversion to Fahrenheit. Formula for conversion: °F = °C * 9/5 + 32 

#user input
user_input = float(input("input celsius temparture: "))

#translate to farenhiet
answer = user_input * 9/5 + 32

#give fanreheit
print(f"{user_input} celsius in farenheit is {answer}")
