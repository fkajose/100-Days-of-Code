# Tic Tac Toe

## Description

A command-line implementation of the classic Tic Tac Toe game supporting both player-vs-player and player-vs-AI modes with intelligent AI strategy.

## Key Concepts

- Game logic
- AI strategy
- NumPy arrays
- Game loops
- Collision/win detection

## How to Run

```bash
python main.py
```

## Game Modes

- **Player vs Player**: Two human players take turns
- **Player vs AI**: Play against an intelligent computer opponent
- **AI vs AI**: Watch two AI players compete (with code modification)

## Features

- Beautiful visual board display
- Emoji markers (❌ and ⭕)
- Intelligent AI with strategic prioritization
- Win/loss/draw detection
- Input validation

## AI Strategy

The AI uses a 5-step strategic approach:

1. Win if possible (complete three in a row)
2. Block opponent's winning move
3. Take center position (5)
4. Take corner positions (1, 3, 7, 9)
5. Take side positions (2, 4, 6, 8)

## What You'll Learn

This project teaches:

- Game loop implementation
- Conditional logic
- NumPy array manipulation
- Algorithm design
- User input handling
- Game state management
- AI strategy implementation
