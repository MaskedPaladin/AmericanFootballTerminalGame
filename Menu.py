import sys

def mainMenu():
    option = input("1) Play\n2) Configure\n0) Exit")
    if option in range(0, 2):
        if option == "2":
            configureMenu()
        elif option == "0":
            sys.exit(0)
    else:
        print("Invalid Option")
        mainMenu()
def configureMenu():
    option = input("1) Local team\n2) Visitor team\n0) Back")
    if option in range(0, 2):
        if option == "0":
            mainMenu()
    else:
        print("Invalid Option")
        mainMenu()
