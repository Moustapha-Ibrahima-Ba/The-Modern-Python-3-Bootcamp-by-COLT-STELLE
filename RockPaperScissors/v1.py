# ....... ROCK-PAPER-SCISSORS .........
print("... ROCK ...")
print("... PAPER ...")
print("... SCISSORS ...")

# Inputs
player1 = input("player1, make your move: ")
player2 = input("player2, make your move: ")

if player1 == player2:
	print("it is a tie!")
# rock
elif player1 == "rock":
	if player2 == "paper":
		print("player2 wins!")
	elif player2 == "scissors":
		print("player1 wins!")
# paper
elif player1 == "paper":
	if player2 == "rock":
		print("player1 wins!")
	elif player2 == "scissors":
		print("player2 wins!")
# scissors
elif player1 == "scissors":
	if player2 == "rock":
		print("player2 wins!")
	elif player2 == "paper":
		print("player1 wins!")
else:
	print("Something went wrong")
