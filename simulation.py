from users import User
from professionals import Professional
from math import sqrt

#The clients and professionals are stored using a fixed array
#  20 and 200 respectively are the maximum amount
#The events need to be sorted by arrival time which means there are 4 options
#1. Hard code the arrival times 
#2. When generating the arrival times make sure the subsequent arrival times minimum range is more than the last arrival time (maybe make all arrival times in the range of last possible (arrival time / n) + m where n is the amount of events and m is an incrementing integer)
#3. Sorting algorithm after generation
#4. Sorting algorithm during simulation as each event enters the system.
client_c = 200
prof_c = 20
event_c = 1000
class Simulation(User):
    def __init__(self, clients, professionals):
        global client_c
        global prof_c
        self.clients = clients[client_c]
        self.professionals = professionals[prof_c]
        self.events = events[]

    def getProfessionals(self):
        return self.professionals
    
    def getClients(self):
        return self.clients
    
    def setProfObj(self, i, professional):
        self.professionals[i] = professional
        
    def setClientObj(self, i, client):
        self.clients[i] = client
    
    def getProfObj(self, i):
        return self.professionals[i]
        
    def getClientObj(self, i):
        return self.clients[i]
    
    def calculateTravel(self, clientXCoord, clientYCoord):
        return round(sqrt((clientXCoord - self.xcoord)**2 + (clientYCoord - self.ycoord)**2), 2)
    
    def calculateServiceTime(self, event, professional):
        distance = self.calculateTravel(self.clients[event.getClientId()].getXCoord(), self.clients[event.getClientId()].getYCoord())
        return (professional.getSpeed()/10) / distance * 2 + event.getServiceTime() * 1.1 - 0.2 * ((professional.getSkill()-1)/50)
    
    def enqueue(self, professional, event):
        traverseEvent = professional.getNextEvent()
        while traverseEvent.getNextEvent() is not None:
            traverseEvent = traverseEvent.getNextEvent()
        traverseEvent.setNextEvent(event)
    
    def dequeue(self, professional):
        event = professional.getNextEvent()
        professional.setCurrentEvent(event)
        if event.getNextEvent() is None:
            del event
        else: 
            professional.setNextEvent(event.getNextEvent())

    def finishService(professional):
        #when the finish time has come for the next professional with a job they get rated, they take dequeue their next job and start working on it if applicable and the next professional to finish is found
        print("ok")
        
    def simulate(self):
        time = 0
        professionals = self.professionals
        nextFinish = None
        for x in self.events:
            while x.getStartTime() < nextFinish.getCurrentEvent().getServiceTime():
                self.finishService(nextFinish)     

            distancerecord = 50
            distanceid = 0

            for y in self.professionals:
                distance = self.calculateTravel(y, x)
                if distance < distancerecord and x.getTrade() == y.getTrade():
                    distancerecord = distance
                    distanceid = y.getId()
                if distancerecord == 50:
                    print("No professional within 50km")
                    break

            professional = professionals[distanceid]
            if professional.getCurrentEvent() is None:
                x.setServiceTime(self.calculateServiceTime(x, professional) + time)
                professional.setCurrentEvent(x)
                if x.getServiceTime() < nextFinish.getCurrentEvent().getServiceTime():
                    nextFinish = professional

            else:
                self.enqueue(professional, x)



