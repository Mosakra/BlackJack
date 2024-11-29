suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}

def initialize_deck():
    deck = []
    for suit in suits:
        for rank in ranks:
            deck.append([suit, rank, values[rank]])
    return deck

def main():
    deck = initialize_deck()
    print(f"Deck length: {len(deck)}")
    print(f"First card in deck: {deck[0]}")

if __name__ == "__main__":
    main()