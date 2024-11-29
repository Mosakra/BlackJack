# BlackJack
Project file structure

BlackjackProject/

│
├── main.py                # Main entry point for the game
├── deck.py                # Functions for deck creation and card management
├── db.py                  # Manages player money storage and updates
├── Game_Logic.py          # Core gameplay mechanics and logic
├── money.txt         # Persistent storage of the player's balance
└── README.md              # Documentation

main.py


Serves as the primary script to launch the game.
Manages:
Game initialization and player balance setup.
The main game loop, ensuring each round progresses smoothly with player and dealer turns.
Coordination of essential functions for card distribution, bet validation, and balance updates.

deck.py


Contains utility functions for creating and managing the card deck.
Primary Functions:
initialize_deck(): Builds a standard 52-card deck with suits, ranks, and corresponding values.
deal_card(hand, deck, num=1): Transfers a specified number of cards from the deck to a hand.

db.py


Handles the storage and retrieval of the player's balance across sessions.
Core Functions:
money_check(): Reads the current balance from a file. If the file is missing, initializes with a default value.
write_money(amount): Updates and saves the player's balance after every round.
Ensures robust file operations to avoid data corruption or loss.

Game_Logic.py


Houses the game's core mechanics and rules.
Key Features:
start_round(money): Prepares the game by dealing cards to both the player and the dealer.
is_blackjack(hand): Determines if a hand is a Blackjack (Ace and a 10-value card).
dealer_play(deck, dealer_hand): Automates the dealer's turn, hitting until their hand reaches a minimum value of 17.
calculate_value(hand): Computes the total hand value, accounting for the flexible Ace (1 or 11).

money.txt

A text file that stores the player's money between games.
Start with a default amount, like 100, if the file is not found.
