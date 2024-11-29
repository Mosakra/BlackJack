import random
import db
from deck import initialize_deck, deal_card
from game_logic import start_round, is_blackjack, dealer_play, calculate_value


def display_title():
    print("BLACKJACK!")
    print("Blackjack payout is 3:2\n")


def handle_ace_in_hand(hand):
    ace_handled = False
    for card in hand:
        if card[1] == 'A' and not ace_handled:
            print("\nYour hand contains an Ace.")
            while True:
                choice = input("Do you want it to count as 1 or 11? (1/11): ")
                if choice in ['1', '11']:
                    card[2] = int(choice)
                    ace_handled = True
                    break
                else:
                    print("Invalid choice. Please enter 1 or 11.")

def is_blackjack(hand):
    return calculate_value(hand) == 21 and len(hand) == 2

def dealer_play(deck, dealer_hand):
    while calculate_value(dealer_hand) < 17:
        deal_card(dealer_hand, deck, 1)
        print("\nDealer's Cards:")
        for card in dealer_hand:
            print(f"{card[1]} of {card[0]}")
    return calculate_value(dealer_hand)

def main():
    display_title()
    money = db.money_check()

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

            db.write_money(money)
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
        db.write_money(money)

        if money < 5:
            print("\nYou're out of money.")
            if input("Would you like to buy more chips? (y/n): ").lower() == 'y':
                money += float(input("Enter amount to add to balance: $"))
            else:
                print("Thanks for playing! Goodbye!")
                break
        elif input("\nPlay again? (y/n): ").lower() != 'y':
            print("\nCome back soon!")
            print("Bye!")
            break
        

if __name__ == "__main__":
    main()