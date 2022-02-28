from clear import clear
from art import logo


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
    print("3. Start Service")
    print("4. Shutdown")
    selection = input("Please make a selection: ")

    if selection == "1":
        print(1)
    elif selection == "2":
        print(2)
    elif selection == "3":
        print(3)
    elif selection == "4":
        print(4)
    else:
        boot_menu(f"The selection of {selection} is invalid! Please make another selection.")
