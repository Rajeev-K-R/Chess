# ♟️ Chess

A two-player desktop chess game built in **Python** using **Pygame**. The project implements the chess board, piece movement, captures, check/checkmate detection, castling, and a graphical interface for two players sharing the same machine.

> **Note:** This project is intentionally a two-player game and does **not** contain an AI engine.

## ✨ Highlights

- Interactive 8×8 chess board rendered with Pygame
- Two-player local gameplay
- Legal move generation for the pieces
- Captures and turn management
- Check and checkmate detection
- Castling
- Reset/restart the game with `Enter`
- Custom board and piece assets

## 🧠 How It Works

The game keeps the state of all 32 chess pieces using their:

- position on the board,
- colour,
- type,
- alive/captured status.

When a player selects a piece, the program computes its possible moves based on the piece's movement rules. It then filters those moves so that a move leaving the player's own king in check is rejected.

The main game loop continuously:

1. Draws the board and active pieces.
2. Reads mouse/keyboard events from Pygame.
3. Identifies the selected piece and destination square.
4. Validates the move.
5. Updates the board state and switches turns.
6. Checks for checkmate.
7. Refreshes the display.

The implementation uses coordinate-based board representation rather than relying on an external chess library.

## 🛠️ Tech Stack

- **Python**
- **Pygame**

## ▶️ Run

Install Pygame:

```bash
pip install pygame
```

Then run the game from the `Chess` directory:

```bash
cd Chess
python chess.py
```

The program expects its `Assets/` directory to remain alongside `chess.py`.

## 🎮 Controls

- **Mouse:** Select a piece and then select its destination square.
- **Enter:** Start a new game after a game has ended.
- **Close window:** Exit the game.

## 📁 Project Structure

```text
Chess/
├── Assets/
│   ├── chess_board-01.png
│   ├── chess-piece.png
│   └── Pieces/
│       ├── k.png
│       ├── q.png
│       ├── r.png
│       ├── b.png
│       ├── n.png
│       └── p.png
└── chess.py
```

## 🎥 Demo

A short gameplay video:
[▶️ Watch the Chess Demo](

https://github.com/user-attachments/assets/b0e9cf6c-4d7b-4d9c-8c2f-2204ca00c8b3

)


## 📌 Project Context

Built as a programming project to explore game development, event-driven programming, graphical interfaces, and implementation of chess movement and game-state logic from scratch.

## 📄 License

Apache-2.0
