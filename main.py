from users import *
from professionals import *

spacer = "-"*50


def index():
    print(spacer)
    print("Only Tradies")
    print(spacer)
    print("Please select one of the options below")
    print("User login (U)")
    print("Tradie login(T)")
    print(spacer)
    selection = input("Enter a selection: ")

    if selection.lower() == "u":
        loginUser()
    elif selection.lower() == "t":
        loginTrade()
    else:
        print("please enter U or T")

def loginUser():
    print(spacer)
    print("User login")
    print(spacer)


def loginTrade():
    print(spacer)
    print("Tradie login")
    print(spacer)

if __name__ == "__main__":   
    index()