import random
from client import *
from professionals import *
#require 20 tradies(proffessionals) and 20 clients

#User variables
#
#ID
#name
#Balance
#Subscriber
#Xcoord
#Ycoord
#jobs
#
#Professionals variables
#
#ID
#Balance
#Subscriber
#Xcoord
#Ycoord
#nextEvent
#skill
#reliability
#speed
#rating
#ammountRated

userNames = ['Liam', 'Noah', 'Oliver', 'Elijah','James','William','Benjamin','Lucas','Henry','Theodore','Jack','Levi',
         'Alexander','Jackson','Mateo','Daniel','Michael','Mason','Sebastian','Ethan','Logan','Owen','Samuel','Jacob',
         'Asher','Aiden','John','Joseph','Wyatt','David','Leo','Luke','Julian','Hudson','Grayson','Matthew','Ezra',
         'Gabriel','Carter','Isaac','Jayden','Luca','Anthony','Dylan','Lincoln','Thomas','Maverick','Elias','Josiah',
         'Charles','Caleb','Christopher','Ezekiel','Mike','hunt','Isaiah','Andrew','Joshua','Nathan','Nolan','Adriana',
         'Cameron','Santiago','Eli','Aaron','Ryan','Angel','Cooper','Waylon','Easton','Kai','Christian','Landon','Colton',
         'Roman','Axel','Brooks','Jonathan','Robert','Jameson','Ian','Everett','Greyson','Wesley','Jeremiah','Hunter',
         'Leonardo','Jordan','Jose','Bennett','Silas','Nicholas','Parker','Beau','Weston','Austin','Connor','Carson',
         'Dominic','Xavier']

buisnessNames = ['concrete', 'brickies', 'carpentry', 'lumber', 'jims construction', 'trades']
buisnessTags = ['Inc', 'PTY LTD', 'LTD', 'Limited']

def generator(numUsers, numPros, numEvents):
    ID = 1
    clients = []
    for i in range(1, numUsers + 1):
        name = ("{} {}".format(random.choice(userNames), random.choice(userNames)))
        sub = random.randint(0, 1)
        if sub == 1:
            sub = False
        else:
            sub = True
        client  = Client(ID, name, 100, sub, random.randint(0, 100), random.randint(0, 100))
        clients.append(client)

        for i in clients:
            print(i)
    


def generateUser():
    print("gen")

def generateProfessionals():
    print("gen")

generator(10, 0, 0)