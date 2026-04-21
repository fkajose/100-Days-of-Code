#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
from art import logo

def num_type():
    factors = []
    for num in range(1, number):
        if number % num == 0:
            factors.append(num)
    if factors == [1]:
        return "a prime"
    elif number % 2 == 0:
        return "an even"
    else:
        return "an odd"
        
print(logo)
number = random.randint(1, 100)
print(f"I'm thinking of {num_type()} number between 1 and 100. Can you guess it?")

difficulty = input("Difficulty: type 'e' for easy, 'm' for medium or 'h' for hard: ").lower()

if difficulty == "e":
    lives = 10
elif difficulty == "m":
    lives = 7
else:
    lives = 5

print(f"You have {lives} attempts remaining.")

def high_low():
    if guess > number:
        return "high"
    else:
        return "low"

while lives > 0:
    guess = int(input("Make a guess: "))
    if guess == number:
        lives = 0
        got_it = "You got it! "
    else:
        lives -= 1
        print(f"Too {high_low()}. Guess again.")
        print(f"You have {lives} attempt(s) remaining.")
        got_it = ""

print(f"{got_it}The answer was {number}.")

