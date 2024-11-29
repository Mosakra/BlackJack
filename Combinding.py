import random

def title():
    print("BLACKJACK!")
    print("Payout 3:2")


def money_check():
    return 100

def write_money(amount):
    print(f"Money updated to ${amount}")

def initialize_deck():
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}
    deck = []
    for suit in suits:
        for rank in ranks:
            deck.append([suit, rank, values[rank]])
    return deck

def start_round(money):
    deck = initialize_deck()
    random.shuffle(deck)

    bet = place_bet(money)
    player_hand = []
    deal_card(player_hand, deck, 2)
    dealer_hand = []
    deal_card(dealer_hand, deck, 2)

    print("\nDEALER'S SHOW CARD:")
    print(f"{dealer_hand[1][1]} of {dealer_hand[1][0]}\n")

    print("YOUR CARDS:")
    for card in player_hand:
        print(f"{card[1]} of {card[0]}")

    return player_hand, dealer_hand, bet, deck

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

def deal_card(hand, deck, num=1):
    for _ in range(num):
        hand.append(deck.pop())

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


def dealer_play(deck, dealer_hand):
    while calculate_value(dealer_hand) < 17:
        deal_card(dealer_hand, deck, 1)
        print("\nDealer's Cards:")
        for card in dealer_hand:
            print(f"{card[1]} of {card[0]}")
    return calculate_value(dealer_hand)

def is_blackjack(hand):
    return calculate_value(hand) == 21 and len(hand) == 2

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
    title()
    money = money_check()

    while money >= 5:
        print(f"Money: ${money}")
        player_hand, dealer_hand, bet, deck = start_round(money)

        player_value = calculate_value(player_hand)
        dealer_value = calculate_value(dealer_hand)

        if is_blackjack(player_hand):
            print("\nYOUR CARDS:")
            for card in player_hand:
                print(f"{card[1]} of {card[0]}")
            print("Your Hand Value: 21 (Blackjack!)")

            print("\nDEALER'S CARDS:")
            for card in dealer_hand:
                print(f"{card[1]} of {card[0]}")
            print(f"Dealer's Hand Value: {dealer_value}")

            if is_blackjack(dealer_hand):
                print("\nIt's a tie! Both you and the dealer have Blackjack.")
            else:
                payout = bet * 1.5
                money += payout
                print(f"\nYou win with a natural Blackjack! Payout: ${payout:.2f}")

            continue

        while True:
            handle_ace_in_hand(player_hand)
            player_value = calculate_value(player_hand)
            if player_value > 21:
                print("\nYou busted! Dealer wins.")
                money -= bet
                break
            action = input("\nHit or stand? (hit/stand): ").lower()
            if action == 'hit':
                deal_card(player_hand, deck, 1)
                print("\nYOUR CARDS:")
                for card in player_hand:
                    print(f"{card[1]} of {card[0]}")
            elif action == 'stand':
                break

        if player_value <= 21:
            print("\nDEALER'S HAND:")
            for card in dealer_hand:
                print(f"{card[1]} of {card[0]}")

            dealer_value = dealer_play(deck, dealer_hand)

            print(f"\nYour Hand Value: {player_value}")
            print(f"Dealer's Hand Value: {dealer_value}")

            if dealer_value > 21 or player_value > dealer_value:
                print("\nYou win!")
                money += bet
            elif player_value < dealer_value:
                print("\nDealer wins!")
                money -= bet
            else:
                print("\nIt's a tie!")

        print(f"\nNew Balance: ${money}")

        if money < 5:
            print("\nYou're out of money.")
            break
        elif input("Play again? (y/n): ").lower() != 'y':
            print("\nCome back soon!")
            print("Bye!")
            break
        

if __name__ == "__main__":
    main()