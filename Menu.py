import sys

def mainMenu():
    option = int(input("1) Play\n2) Configure\n0) Exit\n> "))
    if option in range(0, 3):
        if option == 2:
            configureMenu()
        elif option == 0:
            sys.exit(0)
    else:
        print("Invalid Option")
        mainMenu()
def configureMenu():
    option = int(input("1) Local team\n2) Visitor team\n0) Back\n> "))
    if option in range(0, 2):
        if option == 0:
            mainMenu()
        if option == 1:
            pass
        if option == 2:
            pass
    else:
        print("Invalid Option")
        mainMenu()
