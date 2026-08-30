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
X_marker = "❌"
O_marker = "⭕"
blank_marker = "⏹️"

p1_choice = ""
while p1_choice not in [X_marker, O_marker]:
    p1_choice = (
        input("Player 1: X or O? ")
        .upper()
        .replace("X", X_marker)
        .replace("O", O_marker)
    )

p2_choice = X_marker if p1_choice == O_marker else O_marker
print(f"Player 1 is {p1_choice}. Player 2 is {p2_choice}")

game_array = np.full((3, 3), blank_marker)
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


def play(player: int, marker: str):
    while True:
        try:
            player_input = int(input(f"Player {player} >> ")) - 1

            # Check if the number is valid AND hasn't been taken yet
            if 0 <= player_input < 10 and game_array.flat[player_input] == blank_marker:

                game_array.flat[player_input] = marker

                break
            else:
                print("Invalid Choice or spot already taken! Try again.")
        except ValueError:
            print("Invalid Choice or spot already taken! Try again.")

    display_boards(game_array, check_array)
    return play_on()


def play_on():
    X_win = [X_marker] * 3
    O_win = [O_marker] * 3

    # diagonal checks
    diag = np.diag(game_array)
    anti_diag = np.diag(np.fliplr(game_array))

    if all(diag == X_win) or all(anti_diag == X_win):
        print(f"{X_marker} wins!")
        return False
    elif all(diag == O_win) or all(anti_diag == O_win):
        print(f"{O_marker} wins!")
        return False

    # row check
    for row in game_array:
        if all(row == X_win):
            print(f"{X_marker} wins!")
            return False
        elif all(row == O_win):
            print(f"{O_marker} wins!")
            return False

    # col check
    for num in range(len(game_array)):
        col = game_array[:, num]
        if all(col == X_win):
            print(f"{X_marker} wins!")
            return False
        elif all(col == O_win):
            print(f"{O_marker} wins!")
            return False

    return True


playing = True
while playing:
    playing = play(1, p1_choice)
    if playing:
        playing = play(2, p2_choice)
