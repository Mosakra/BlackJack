import random

suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}

def initialize_deck():
    deck = [[suit, rank, values[rank]] for suit in suits for rank in ranks]
    random.shuffle(deck)
    return deck

def deal_card(hand, deck, num=1):
    for _ in range(num):
        hand.append(deck.pop())