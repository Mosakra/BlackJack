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
def is_blackjack(hand):
    return calculate_value(hand) == 21 and len(hand) == 2


def main():
    hand = [['Hearts', 'A', 11], ['Clubs', '10', 10]]
    print(f"Is Blackjack: {is_blackjack(hand)}")

if __name__ == "__main__":
    main()