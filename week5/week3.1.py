# Improve the previous program to keep the score and ask the user if the want to play again. Each time display the current score.

# =============================
# Rock-Paper-Scissors. Write a program where user plays R, P, or S, then the system selects R, P, or S for the computer and display who wins. 
import random


exit = False
pc_score = 0
player_score = 0


while not exit:
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
        pc_score += 1
    if guess == "Rock" and computer_guess == "Scissors":
        print_result()
        print("VICTORY")
        player_score += 1
    if guess == "Paper" and computer_guess == "Rock":
        print_result()
        print("VICTORY")
        player_score += 1
    if guess == "Paper" and computer_guess == "Scissors":
        print_result()
        print("DEFEAT")
        pc_score += 1
    if guess == "Scissors" and computer_guess == "Rock":
        print_result()
        print("DEFEAT")
        pc_score += 1
    if guess == "Scissors" and computer_guess == "Paper":
        print_result()
        print("VICTORY")
        player_score += 1

    print(f"\033[92mYour Score\033[0m: \033[93m{player_score}\033[0m VS \033[91mComputer Score\033[0m: \033[93m{pc_score}\033[0m")

    exit = input("Care to Try Again? Y/N: ").upper()
    if exit == "N" or exit == "n":
        print("Better Luck Next Time!")
        exit = True
    else:
        exit = False