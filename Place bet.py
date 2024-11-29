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

def main():
    money = 100
    bet = place_bet(money)
    print(f"Bet placed: ${bet}")


if __name__ == "__main__":
    main()