def money_check():
    try:
        with open("money.txt", "r") as file:
            money = float(file.read())  
    except FileNotFoundError:
        print("Error. Could not find file. Starting with default of $100")
        money = 100.0  
        write_money(money) 
    except ValueError:
        print("Error. Invalid data in file. Starting with default of $100")
        money = 100.0  
        write_money(money)  
    return money


def write_money(money):
    try:
        with open("money.txt", "w") as file:
            file.write(str(round(money, 2)))
    except Exception as e:
        print(f"Error writing money to file: {e}")