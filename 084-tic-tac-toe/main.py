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
while p1_choice not in ["❌", "⭕"]:
    p1_choice = (
        input("Player 1: X or O? ").upper().replace("X", "❌").replace("O", "⭕")
    )

p2_choice = "❌" if p1_choice == "⭕" else "⭕"
print(f"Player 1 is {p1_choice}. Player 2 is {p2_choice}")


game_array = np.full((3, 3), "⏹️")
check_array = np.array([["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]])


def display_boards(board, guide):
    print("Here is your board. Select a number to play in that position.")
    print("\n   CURRENT BOARD          POSITION GUIDE")
    print("  ━━━━━━━━━━━━━━━        ━━━━━━━━━━━━━━━")

    # Loop through the rows (0, 1, 2)
    for i in range(3):
        # Join row elements with spaces for the game board
        board_row = "  ".join(board[i])
        # Join row elements with vertical bars for a crisp grid look
        guide_row = " | ".join(guide[i])

        # Print the matching rows side-by-side
        print(f"    {board_row}                 {guide_row}")

        # Add a horizontal divider between rows, but not after the last row
        if i < 2:
            print("                   ───>     ───+───+───")
    print()


# Test the display
display_boards(game_array, check_array)

num_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]


def play(player: int, marker: str):
    while True:
        player_input = input(f"Player {player} >> ")

        # Check if the number is valid AND hasn't been taken yet
        if player_input in num_list and player_input in check_array:
            # Create the boolean mask once
            mask = check_array == player_input

            # Update both arrays using the mask
            game_array[mask] = marker
            check_array[mask] = marker
            break
        else:
            print("Invalid Choice or spot already taken! Try again.")

    display_boards(game_array, check_array)
    return play_on()


def play_on():
    X_win = ["❌"] * 3
    O_win = ["⭕"] * 3

    # diagonal checks
    diag = np.diag(check_array)
    anti_diag = np.diag(np.fliplr(check_array))

    if all(diag == X_win) or all(anti_diag == X_win):
        print("❌ wins!")
        return False
    elif all(diag == O_win) or all(anti_diag == O_win):
        print("⭕ wins!")
        return False

    # row check
    for row in check_array:
        if all(row == X_win):
            print("❌ wins!")
            return False
        elif all(row == O_win):
            print("⭕ wins!")
            return False

    # col check
    for num in range(len(check_array)):
        col = check_array[:, num]
        if all(col == X_win):
            print("❌ wins!")
            return False
        elif all(col == O_win):
            print("⭕ wins!")
            return False

    return True


playing = True
while playing:
    playing = play(1, p1_choice)
    if playing:
        playing = play(2, p2_choice)
