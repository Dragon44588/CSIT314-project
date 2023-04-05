from users import *
from professionals import *

spacer = "-"*50


def index():
    while True:

        print(spacer)
        username = input("Username: ")
        password = input("Password: ")

        if username.lower() == "trade":
            loginTrade()
        
        elif username.lower() == "client":
            loginUser()
        
        else:
            print("incorrect login")

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