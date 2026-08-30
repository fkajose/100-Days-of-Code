"""
Tic Tac Toe - A Command-Line Game

A two-player implementation of the classic Tic Tac Toe game with optional AI opponent.
Players take turns marking positions on a 3x3 grid, with the first player to get three
in a row (horizontally, vertically, or diagonally) winning the game.

Features:
- Player vs Player mode
- Player vs AI mode with intelligent strategy
- Clear visual board display with position numbers
- Win/Loss/Draw detection

Game Flow:
1. Player 1 selects X or O as their marker
2. Player 2 (or AI) is assigned the alternative marker
3. Players alternate turns selecting positions 1-9 on the grid
4. Game ends when someone wins or the board is full (draw)
"""

import numpy as np
import random

print("Tic Tac Toe")
print("Perfect for 2 players. Or play with AI")
ai_active = input("Play with AI? Y/N: ").upper()

X_marker = "❌"
O_marker = "⭕"
blank_marker = "⏹️"

# =====================================================
# Functions Live Here
# =====================================================


def select_marker():
    """Prompts Player 1 to select X or O marker and assigns the alternative to Player 2.

    Returns:
        tuple: (p1_choice, p2_choice) - The markers chosen for Player 1 and Player 2.
    """
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
    return p1_choice, p2_choice


game_array = np.full((3, 3), blank_marker)
check_array = np.array([["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]])


def display_boards(board, guide):
    """Displays the current game board and position guide side-by-side.

    Args:
        board: numpy array representing the current game state.
        guide: numpy array showing the position numbers (1-9).
    """
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


def find_winning_or_blocking_move(board, marker):
    """Checks rows, columns, and diagonals for a spot to complete a trio.

    Args:
        board: numpy array representing the current game state.
        marker: The marker to search for (X or O).

    Returns:
        str: The position number (1-9) to complete the trio, or None if no such move exists.
    """
    # Check rows and columns
    for i in range(3):
        # Rows
        row = board[i, :]
        if np.sum(row == marker) == 2 and np.sum(row == blank_marker) == 1:
            return check_array[i, np.where(row == blank_marker)[0][0]]

        # Columns
        col = board[:, i]
        if np.sum(col == marker) == 2 and np.sum(col == blank_marker) == 1:
            return check_array[np.where(col == blank_marker)[0][0], i]

    # Diagonal 1 (\)
    diag1 = np.diag(board)
    if np.sum(diag1 == marker) == 2 and np.sum(diag1 == blank_marker) == 1:
        idx = np.where(diag1 == blank_marker)[0][0]
        return check_array[idx, idx]

    # Diagonal 2 (/)
    diag2 = np.diag(np.fliplr(board))
    if np.sum(diag2 == marker) == 2 and np.sum(diag2 == blank_marker) == 1:
        idx = np.where(diag2 == blank_marker)[0][0]
        # Map flipped column index back to original
        return check_array[idx, 2 - idx]

    return None


def ai_player(ai_marker, human_marker):
    """Determines the AI player's next move using strategic prioritization.

    Strategies (in order):
    1. Win if possible
    2. Block opponent's winning move
    3. Take center (position 5)
    4. Take corners (1, 3, 7, 9)
    5. Take sides (2, 4, 6, 8)

    Args:
        ai_marker: The marker used by the AI.
        human_marker: The marker used by the human player.

    Returns:
        int: The position number (1-9) for the AI's move, or None if no moves available.
    """
    available_moves = check_array[game_array == blank_marker]
    if len(available_moves) == 0:
        return None  # Tie game / no moves left

    # Strategy Step 1: Can AI win this turn?
    win_move = find_winning_or_blocking_move(game_array, ai_marker)
    if win_move in available_moves:
        return int(win_move)

    # Strategy Step 2: Does AI need to block the human?
    block_move = find_winning_or_blocking_move(game_array, human_marker)
    if block_move in available_moves:
        return int(block_move)

    # Strategy Step 3: Take Center if available
    if "5" in available_moves:
        return 5

    # Strategy Step 4: Take Corners (1, 3, 7, 9)
    corners = [c for c in ["1", "3", "7", "9"] if c in available_moves]
    if corners:
        return int(random.choice(corners))

    # Strategy Step 5: Take Sides (2, 4, 6, 8)
    sides = [s for s in ["2", "4", "6", "8"] if s in available_moves]
    if sides:
        return int(random.choice(sides))


def play(player: int, marker: str, ai=False, ai_marker=None, human_marker=None):
    """Handles a single player's turn and updates the game board.

    Args:
        player: Player number (1 or 2).
        marker: The marker for this player (X or O).
        ai: Boolean indicating if this is an AI player.
        ai_marker: The marker used by the AI (required if ai=True).
        human_marker: The marker used by the human player (required if ai=True).

    Returns:
        bool: True if the game should continue, False if game is over.
    """
    while True:
        try:
            player_input = (
                ai_player(ai_marker, human_marker)
                if ai
                else int(input(f"Player {player} >> "))
            ) - 1

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
    """Checks if the game should continue by testing win conditions and draw.

    Returns:
        bool: True if the game should continue, False if game is over (win or draw).
    """
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

    # Draw criterion
    if len(check_array[game_array == blank_marker]) == 0:
        print("➖ Its a draw!!")
        return False

    return True


def start_game(p1, p2, ai_plays=None):
    """Starts and controls the main game loop.

    Args:
        p1: Marker for Player 1.
        p2: Marker for Player 2.
        ai_plays: Indicates if AI is playing and which player ('first', 'second', or None).
    """
    playing = True
    while playing:
        if ai_plays == "first":
            playing = play(1, p1, ai=True, ai_marker=p1, human_marker=p2)
            if playing:
                playing = play(2, p2)
        elif ai_plays == "second":
            playing = play(1, p1)
            if playing:
                playing = play(2, p2, ai=True, ai_marker=p2, human_marker=p1)
        else:
            playing = play(1, p1)
            if playing:
                playing = play(2, p2)


# =====================================================
# Main Game Loop Lives Here
# =====================================================
if ai_active == "Y":
    cointoss = random.randint(0, 1)
    markers = [X_marker, O_marker]
    if cointoss == 0:
        print("AI is Player 1")
        ai_marker = markers[random.randint(0, 1)]
        player_marker = X_marker if ai_marker == O_marker else O_marker
        print(f"AI chooses {ai_marker}. Player is {player_marker}")
        start_game(ai_marker, player_marker, ai_plays="first")

    else:
        print("Human is Player 1.")
        start_game(*select_marker(), ai_plays="second")


else:
    start_game(*select_marker())
