import random
from client import *
from professionals import *
from event import *
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
    professionals = []
    events = []
    time = 0
    
    for i in range(0, numUsers):
        client = generateUser(ID)
        clients.append(client)
        ID += 1    
    
    for i in range(0, numPros):
        professional = generateProfessionals(ID)
        professionals.append(professional)
        ID += 1
        
    for i in range(0, numEvents):
        newTime = (100/numEvents)
        event = generateEvents(clients, time, newTime)
        events.append(event)
        time += newTime
        
        rdata = ""
        data = ""
        rdata += "==============================================  Clients  ================================================\n"
        data += "clients\n"
        for i in clients:
            rdata += str(i) + "\n"
            data += repr(i) + "\n"
        data += "<=====>\n"
        rdata += "===========================================================================================================\n"
        data += "tradies\n"
        rdata += "=====================================================  Tradies  ==============================================================\n"
        for i in professionals:
            rdata += str(i) + "\n"
            data += repr(i) + "\n"
        data += "<=====>\n"
        rdata += "======================================================================================================================================\n"
        data += "events\n"
        rdata += "====================================================  Events  ===========================================\n"
        for i in events:
            rdata += str(i) + "\n"
            data += repr(i) + "\n"
        data += "<=====>"
        rdata += "=========================================================================================================\n"
        
    with open("test_data.txt", "w") as f:
        f.write(data)

    with open("readable_test_data.txt", "w") as rf:
        rf.write(rdata)
   

def generateUser(id):
        name = ("{} {}".format(random.choice(userNames), random.choice(userNames)))
        return Client(id, name, 100, random.randint(0,1), random.randint(0, 100), random.randint(0, 100))

def generateProfessionals(id):
    name = ("{} {}".format(random.choice(buisnessNames), random.choice(buisnessTags)))
    return Professional(id, name, 100, random.randint(0,1), random.randint(0, 100), random.randint(0, 100), random.randint(0, 100), random.randint(0, 100), random.randint(0, 100), random.randint(0, 4))


def generateEvents(clients, time, newTime):
    return Event(random.choice(clients).getId(), time, newTime, (50 + random.randint(0, 50)), random.randint(0, 4))


if __name__ == "__main__":
    clients = int(input("Number of Clients: "))
    tradies = int(input("Number of Tradies: "))
    events = int(input("Number of Events: "))
    generator(clients, tradies, events)