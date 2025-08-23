🃏 Simple Blackjack Game

A simple command-line Blackjack game written in Python.
The player competes against the dealer to reach 21 without going over.

🚀 Features

Player can draw or pass cards.

Dealer automatically draws until reaching at least 19.

Ace is always counted as 11 (simplified rules).

Detects Blackjack (21 on first draw).

Announces winner: You Win / You Lose / Tie.

📦 Installation

Clone this repository:

git clone https://github.com/your-username/blackjack-game.git
cd blackjack-game


Make sure you have Python 3 installed:

python --version


Run the game:

python main.py

🎮 How to Play

Start the game by typing s.

You will receive 2 random cards, the dealer also gets 2 (one is hidden).

Choose whether to:

draw → take another card

pass → let the dealer play

If your total goes over 21, you bust and lose immediately.

The dealer draws cards until reaching at least 19.

Whoever is closer to 21 without going over wins.

📖 Rules Simplification

The game doesn’t yet handle Ace = 1 or 11 switching (it’s always 11).

No betting system or multiple players (just player vs dealer).

🛠️ Project Structure
blackjack-game/
│
├── main.py     # game loop, player input, setup
├── game.py     # game logic (dealer draw, winner check, score print)
├── art.py      # ASCII art for game logo
└── README.md   # this file
