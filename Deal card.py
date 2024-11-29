def deal_card(hand, deck, num=1):
    for _ in range(num):
        hand.append(deck.pop())

def main():
    deck = [['Hearts', '2', 2], ['Diamonds', '3', 3], ['Clubs', '4', 4]]
    hand = []
    deal_card(hand, deck, 2)
    print(f"Hand: {hand}")
    print(f"Remaining deck: {deck}")

if __name__ == "__main__":
    main()