rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
print("""
Welcome to Rock, Paper, Scissors!
To play this game, you choose either rock, paper, or scissors.
The computer makes a similar choice.
Note: 
-Rock beats scissors
-Scissors cuts paper
-Paper covers rock
""")
user = int(input("What do you choose?\nType 0 for rock, 1 for paper, 2 for scissors: "))
computer = random.randint(0, 2)
game = [rock, paper, scissors]
if user >= 3 or user < 0:
	print("Invalid number, you lose by default!")
else:
	print(f"""
You chose: 
	{game[user]}
Computer chose:
	{game[computer]}""")
	if user == computer:
		print("It's a draw!")
	elif (user == 0 and computer==2) or (user == 2 and computer == 0):
		if user > computer:
			print("You lose!")
		else:
			print("You win!")
	elif user < computer:
		print("You lose!")
	elif user > computer:
		print("You win!")
	