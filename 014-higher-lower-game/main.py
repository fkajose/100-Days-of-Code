from replit import clear
from game_data import data
from art import logo, vs
from random import choice

option_a = choice(data)
score = 0
def game():
    
    print(logo)

    global score
    if score > 0:
        print(f"You're right! Current score: {score}.")

    def display(option, char):
        """Takes data and prints in a usable format."""
        def vowel(word):
            """Checks if word requires a or an"""
            vowels = ["a", "e", "i", "o", "u"]
            if word[0].lower() in vowels:
                return "an"
            else:
                return "a"
        
        def a_or_b():
            if char.upper() == "A":
                return "Compare"
            else:
                return "Against"
        print(f"{a_or_b()} {char.upper()}: {option['name']}, {vowel(option['description'])} {option['description']} from {option['country']}.")
    
    # selects option A
    global option_a
    follower_a = option_a['follower_count']
    display(option_a, "a")

    print(vs)

    # selects option B
    option_b = choice(data)
    while option_b == option_a:
        option_b = choice(data)
    follower_b = option_b['follower_count']
    display(option_b, "b")

    # collects user input and reassign
    user = input("Who has more followers? Type 'A' or 'B': ").upper()
    if user == "A":
        user = option_a
    elif user == "B":
        user = option_b
    else:
        print("Invalid input, mate.")
        return
    
    # checks correctness and increases score
    if max([follower_a, follower_b]) == user['follower_count']: 
        clear()
        option_a = option_b
        score += 1
        game()
    else:
        clear()
        print(logo)
        print(f"That's wrong. Final score: {score}")
        if score < 3:
            print("Oh dear!!! I'm embarassed for you.")
        elif score < 6:
            print("Pretty decent, not gonna lie.")
        else:
            print("Excellent! You own the internet.")
                
game()
