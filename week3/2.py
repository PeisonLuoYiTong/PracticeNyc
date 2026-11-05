# Rock-Paper-Scissors. Write a program where user plays R, P, or S, then the system selects R, P, or S for the computer and display who wins. 
import random

user_input = input("Rock, Paper, Scissors.\nR for rock, P for paper, S for scissors: ").upper()
output = random.randint(1, 3)
# print(output)
guess = ""
computer_guess = ""

if user_input == "R":
    guess = "rock"
elif user_input == "P":
    guess = "paper"
elif user_input == "S":
    guess = "scissors"
else:
    print("try again")

if output == 1:
    computer_guess = "rock"
elif output == 2:
    computer_guess = "paper"
else:
    computer_guess = "scissors"

def print_result():
    print(f"\033[92m{guess}\033[0m VS \033[91m{computer_guess}\033[0m")

if guess == computer_guess:
    print_result()
    print("TIE")
if guess == "rock" and computer_guess == "paper":
    print_result()
    print("DEFEAT")
if guess == "rock" and computer_guess == "scissors":
    print_result()
    print("VICTORY")
if guess == "paper" and computer_guess == "rock":
    print_result()
    print("VICTORY")
if guess == "paper" and computer_guess == "scissors":
    print_result()
    print("DEFEAT")
if guess == "scissors" and computer_guess == "rock":
    print_result()
    print("DEFEAT")
if guess == "scissors" and computer_guess == "paper":
    print_result()
    print("VICTORY")