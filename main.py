from art import logo
from menu import MENU as menu
from bootmenu import boot_menu
import os


# For the resources assume that the machine has:
# 3 litres of water
# 2 litres of milk substitute
# 1 kilogram of coffee
RESOURCES = {
    "water": 3000,
    "milk": 2000,
    "coffee": 1000,
}

# No machine starts empty
# Float money is 20€ in coins
MONEY = {
    "TwoEuro": 0,
    "OneEuro": 0,
    "Fifty": 10,
    "Twenty": 25,
    "Ten": 50,
    "Five": 100
}

if __name__ == '__main__':
    boot_menu("")
