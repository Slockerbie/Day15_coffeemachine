from art import logo
from menu import MENU as menu
import os

# For the resources assume that the machine has:
# 3 litres of water
# 2 litres of milk substitute
# 1 kilogram of coffee
resources = {
    "water": 3000,
    "milk": 2000,
    "coffee": 1000,
}

# No machine starts empty
# Float money is 20€ in coins
moneybox = {
    "TwoEuro": 0,
    "OneEuro": 0,
    "Fifty": 10,
    "Twenty": 25,
    "Ten": 50,
    "Five": 100
}


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def boot_menu():
    clear()
    print(f"{logo} \n")
    print("Coffeematic Boot Sequence")
    print("Please make a selection: ")
    print("1. Check Resources")
    print("2. Check Money Box")


if __name__ == '__main__':
    boot_menu()
