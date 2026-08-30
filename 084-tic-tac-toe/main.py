# Tic Tac Toe
# Must be a command-line game
# Idea:
# 1. Display a 3x3 grid and number 1-9
# 2. Input: Player 1, Pick X or O
# 3. Assign the alternative to Player 2.
# 4. Create a 3x3 matrix; let "_" be the default state for each cell.
# 5. While loop, recursive gameplay
# 6. If P1 plays chooses location, replace that location with the equivalent in the game

import numpy as np

print("Tic Tac Toe")
print("Perfect for 2 players.")
p1_choice = ""
while p1_choice not in ["X", "O"]:
    p1_choice = input("Player 1: X or O? ").upper()

p2_choice = "X" if p1_choice == "O" else "O"
print(f"Player 1 is {p1_choice}. Player 2 is {p2_choice}")

print("Here is your board. Select a number to play in that position.")
game_array = np.array([["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]])
print("\n", game_array, "\n")

num_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]


def play(player: int, marker: str):
    while True:
        player_input = input(f"Player {player}: Select a number>> ")

        # Check if the number is valid AND hasn't been taken yet
        if player_input in num_list and player_input in game_array:
            # Replace the string number with the player's marker
            game_array[game_array == player_input] = marker
            break  # Exit the loop since a valid move was made
        else:
            print("Invalid Choice or spot already taken! Try again.")

    print("\n", game_array, "\n")
    return play_on()


def play_on():
    X_win = ["X"] * 3
    O_win = ["O"] * 3

    # diagonal checks
    diag = np.diag(game_array)
    anti_diag = np.diag(np.fliplr(game_array))

    if all(diag == X_win) or all(anti_diag == X_win):
        print("X wins!")
        return False
    elif all(diag == O_win) or all(anti_diag == O_win):
        print("O wins!")
        return False

    # row check
    for row in game_array:
        if all(row == X_win):
            print("X wins!")
            return False
        elif all(row == O_win):
            print("O wins!")
            return False

    # col check
    for num in range(len(game_array)):
        col = game_array[:, num]
        if all(col == X_win):
            print("X wins!")
            return False
        elif all(col == O_win):
            print("O wins!")
            return False

    return True


playing = True
while playing:
    playing = play(1, p1_choice)
    if playing:
        playing = play(2, p2_choice)
