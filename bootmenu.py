from clear import clear
from art import logo
from resources import goods, money


def check_resources():
    boot_menu("Not Implemented")


def check_money():
    boot_menu("Not Implemented")


def check_card_reader():
    boot_menu("Not Implemented")


def boot_menu(message):
    clear()
    print(f"{logo} \n")
    print("Coffeematic Boot Sequence \n")
    if len(message) > 0:
        print("")
        print(message)
        print("")
    print("1. Check Resources")
    print("2. Check Money Box")
    print("3. Check Card Reader Connection")
    print("4. Start Service")
    print("5. Shutdown \n")

    selection = input("Please make a selection: ")

    if selection == "1":
        check_resources()
    elif selection == "2":
        check_money()
    elif selection == "3":
        check_card_reader()
    elif selection == "4":
        boot_menu("Not Implemented")
    elif selection == "5":
        print("Shutting Down")
        exit(0)
    else:
        boot_menu(f"The selection of {selection} is invalid! Please make another selection.")
