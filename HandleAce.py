def handle_ace_in_hand(hand):
    for card in hand:
        if card[1] == 'A':
            print("\nYour hand contains an Ace.")
            while True:
                choice = input("Do you want it to count as 1 or 11? (1/11): ")
                if choice in ['1', '11']:
                    card[2] = int(choice)
                    break
                else:
                    print("Invalid choice. Please enter 1 or 11.")

def main():
    hand = [['Hearts', 'A', 11]]
    handle_ace_in_hand(hand)
    print(f"Updated Hand: {hand}")


if __name__ == "__main__":
    main()