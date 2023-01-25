from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)
print("Welcome to the Blind Auction Program. 🕵️️")

def highest_bid():
    max_bid = 0
    winner = ""
    for key in bidder_info:
        value = bidder_info[key]
        if value > max_bid:
            max_bid = value
            winner = key
    print(f"The winner is {winner} with a bid of ${max_bid}")

bidder_info = {}
other_bidders = "yes"
while other_bidders == "yes":
    name = input("What is your name?: ")
    bid = float(input("What is your bid? $"))
    bidder_info[name] = bid
    other_bidders = input("Are there other bidders? (Type 'yes' or 'no')\n").lower()
    clear()

highest_bid()
