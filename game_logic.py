from deck import initialize_deck, deal_card

def start_round(money):
    deck = initialize_deck()
    bet = place_bet(money)
    player_hand = []
    dealer_hand = []
    deal_card(player_hand, deck, 2)
    deal_card(dealer_hand, deck, 2)

    print("\nDEALER'S SHOW CARD:")
    print(f"{dealer_hand[1][1]} of {dealer_hand[1][0]}\n")

    print("YOUR CARDS:")
    for card in player_hand:
        print(f"{card[1]} of {card[0]}")

    return player_hand, dealer_hand, bet, deck

def is_blackjack(hand):
    return calculate_value(hand) == 21 and len(hand) == 2

def dealer_play(deck, dealer_hand):
    while calculate_value(dealer_hand) < 17:
        deal_card(dealer_hand, deck, 1)
    return calculate_value(dealer_hand)

def calculate_value(hand):
    value = 0
    aces = 0
    for card in hand:
        if card[1] != 'A':
            value += card[2]
        else:
            aces += 1
    value += aces * 11
    while value > 21 and aces:
        value -= 10
        aces -= 1
    return value

def place_bet(money):
    while True:
        try:
            bet = float(input(f"Bet amount (Current balance: ${money}): $"))
            if bet < 5:
                print("Minimum bet is $5.")
            elif bet > 1000:
                print("Maximum bet is $1000.")
            elif bet > money:
                print(f"Insufficient funds. Your balance is ${money}.")
            else:
                return bet
        except ValueError:
            print("Invalid input. Please enter a valid number.")