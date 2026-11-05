# Rock-Paper-Scissors. Write a program where user plays R, P, or S, then the system selects R, P, or S for the computer and display who wins. 
import random

user_input = input("Rock, Paper, Scissors.\nR for Rock, P for Paper, S for Scissors: ").upper()
output = random.randint(1, 3)
# print(output)
guess = ""
computer_guess = ""

if user_input == "R":
    guess = "Rock"
elif user_input == "P":
    guess = "Paper"
elif user_input == "S":
    guess = "Scissors"
else:
    print("try again")

if output == 1:
    computer_guess = "Rock"
elif output == 2:
    computer_guess = "Paper"
else:
    computer_guess = "Scissors"

def print_result():
    print(f"\033[92m{guess}\033[0m VS \033[91m{computer_guess}\033[0m")

if guess == computer_guess:
    print_result()
    print("TIE")
if guess == "Rock" and computer_guess == "Paper":
    print_result()
    print("DEFEAT")
if guess == "Rock" and computer_guess == "Scissors":
    print_result()
    print("VICTORY")
if guess == "Paper" and computer_guess == "Rock":
    print_result()
    print("VICTORY")
if guess == "Paper" and computer_guess == "Scissors":
    print_result()
    print("DEFEAT")
if guess == "Scissors" and computer_guess == "Rock":
    print_result()
    print("DEFEAT")
if guess == "Scissors" and computer_guess == "Paper":
    print_result()
    print("VICTORY")