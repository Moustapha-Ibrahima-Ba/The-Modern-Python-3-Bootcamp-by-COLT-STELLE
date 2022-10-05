# ....... ROCK-PAPER-SCISSORS .........
print("... ROCK ...")
print("... PAPER ...")
print("... SCISSORS ...")

import random

computer_choice = random.randint(1, 3)

# Inputs
player = input("Enter your choice: ")

if player != "rock" and player != "paper" and player != "scissors":
	print("Something went wrong, choose between 'rock', 'paper', and 'scissors' ")

# rock
elif computer_choice == 1:
	computer_choice = "rock"
	print(f"The computer plays {computer_choice} ")
	if player == "paper":
		print("Congratulation, You win.")
	elif player == "scissors":
		print("Sorry, You lost.")
	elif player == computer_choice:
		print("It is a tie!")
# paper
elif computer_choice == 2: 
	computer_choice = "paper"
	print(f"The computer plays {computer_choice} ")
	if player == "rock":
		print("Congratulation, You win.")
	elif player == "scissors":
		print("Sorry, You lost.")
	elif player == computer_choice:
		print("It is a tie!")
# scissors
elif computer_choice == 3:
	computer_choice = "scissors"
	print(f"The computer plays {computer_choice} ")
	if player == "paper":
		print("Congratulation, You win.")
	elif player == "rock":
		print("Sorry, You lost.")
	elif player == computer_choice:
		print("It is a tie!")
