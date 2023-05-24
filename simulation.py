from users import User
from professionals import Professional
from client import Client
from event import Event
from math import sqrt
import random
from numpy import random

#client and prof subcost are global variables indicating the price to pay to subscribe
clientsubcost = 200
profsubcost = 275

#percentagecut is the percentage paid to the system whenever a not subscribed professional finishes a job 
percentagecut = 15


class Simulation(User):
    def __init__(self):
        self.busy_c = 0
        self.clients = []
        self.professionals = []
        self.events = []
        self.time = 0
        self.servicereport = "Services: \n"
        self.subscriberreport = "Subscriptions: \n"
        self.professionalreport = "Professionals: \n"

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

    def calculateTravel(self, professional, event):
        client = self.clients[int(event.clientId)]
        clientXCoord = client.getXCoord()
        clientYCoord = client.getYCoord()
        profXCoord = professional.getXCoord()
        profYCoord = professional.getXCoord()
        return round(sqrt((float(clientXCoord) - float(profXCoord))**2 + (float(clientYCoord) - float(profYCoord))**2), 2)

    #This calculates the total service time, including travel to and from the job site. Each job has a base speed and that speed is influenced by the skill of the professional.    
    def calculateServiceTime(self, event, professional):
        distance = self.calculateTravel(professional, event)
        return (professional.getSpeed()/10) / distance * 2 + event.getServiceTime() * 1.1 - 0.2 * ((professional.getSkill()-1)/50)
    
    #queueing and dequeueing system
    def enqueue(self, professional, event):

        traverseEvent = Event(-1, None, None, 0)
        traverseEvent = professional.nextEvent
        if professional.nextEvent is None:
            professional.nextEvent = event
            return

        traverseEvent = Event(-1, None, None, 0)
        traverseEvent = professional.nextEvent
        traverseEvent = professional.nextEvent
        while traverseEvent.nextEvent is not None:

            traverseEvent = traverseEvent.nextEvent
        traverseEvent.nextEvent = event
    
    def dequeue(self, professional):
        event = professional.getNextEvent()
        event.setEndTime(self.calculateServiceTime(event, professional) + self.time)
        professional.setCurrentEvent(event)
        if event.getNextEvent() is None:
            del event
        else: 
            professional.setNextEvent(event.getNextEvent())


    def finishService(self, professional):
        results = ""
        event = professional.currentEvent
        client = self.clients[int(event.clientId)]
        #when the finish time has come for the next professional with a job they get rated, they take dequeue their next job and start working on it if applicable and the next professional to finish is found

        #Creates a normal distribution to get performance. Reliability affects the flatness of the curve and skill changes the mean.
        rawperformance = max(1,min(50,random.normal(loc=int(professional.skill), scale=50/int(professional.reliability), size=(1))))
        rawperformance = str(rawperformance)
        rawperformance = rawperformance.replace('[','')
        performance = int(float(rawperformance[:5]))
        professional.currentEvent.setPerformance(performance)
        professional.setRating((professional.getRating()*professional.getAmountRated() + performance) / (professional.getAmountRated()+1))
        professional.setAmountRated(professional.getAmountRated()+1)
        
        #If the professional has nothing left in his queue they are no longer busy.
        if professional.getNextEvent() == None:
            professional.setCurrentEvent(None)
            self.busy_c -= 1
        else:
            self.dequeue(professional)

        results += "Professional ID: " + str(professional.getId()) + "\n"
        results += "Client ID: " + str(client.id) + "\n"
        results += "Time request made: " + str(event.getStartTime()) + "\n" 
        results += "Distance to job site: " + str(self.calculateTravel(professional, event)) + "\n"
        results += "Service Time: " + str(event.getServiceTime()) + "\n"
        results += "Time Finished: " + str(event.getEndTime()) + "\n"
        results += "Performance: " + str(event.getPerformance()) + "\n\n"
        self.servicereport += results
        

    #Gets the subscription status of both the client and professional then changes their balance accordingly. 
    #Subscribed clients skip paying all together while subscribed professionals do not have their pay deducted.
    #After payment is completed a 1/5 chance is rolled for the client and professional independantly to subscribe.
    #Think of it as them realising the benefits of subscribing.     
    def payment(self, professional, client):
        results = "SERVICE FINISH \n"
        results += "Client Id: " + str(client.getId()) + "\n"
        results += "Client Subscriber Status: "
        if client.getSubStatus() == 0:
            client.setBalance(client.getBalance() - professional.getPrice())
            results += "Unsubscribed \n"
            results += "Amount total: $" + str(professional.getPrice()) + "\n"
            results += "Client Balance: $" + str(client.getBalance()) + "\n"
        else:
            results += "Unsubscribed, $" + str(professional.getPrice()) +  " payment not needed\n"
            results += "Amount total: $0 \n"
        results += "Client Balance: $" + str(client.getBalance()) + "\n \n"
        results += "Professional Subscriber Status: "
        if professional.getSubStatus() == 0:
            professional.setBalance(professional.getBalance() + professional.getPrice()* 1-(percentagecut/100))
            results += "Unsubscribed, " + str(percentagecut) + "% paid to system as commission \n"
            results += "Payment to Professional: $" + str(professional.getPrice()* 1-(percentagecut/100)) + "\n"
        else:
            results += "Subscribed, " + str(percentagecut) + "% paid to system as commission \n"
            results += "Payment to Professional: $" + str(professional.getPrice()) + "\n"
            professional.setBalance(professional.getBalance() + professional.getPrice())
        results += "Professional Balance: $" + str(professional.getBalance()) + "\n \n \n"
        if 1 == random.randint(1, 5):
            client.setBalance(client.getBalance() - clientsubcost)
            client.setSubStatus(1)
            self.subscriberreport += "Client Id: " + str(client.getId()) + "\n"
            self.subscriberreport += "Time: " + str(professional.currentEvent.getEndTime()) + "\n"
            self.subscriberreport += "Cost: " + str(clientsubcost) + "\n"
            self.subscriberreport += "Balance: " + str(client.getBalance()) + "\n\n"


        if 1 == random.randint(1, 5):
            professional.setBalance(professional.getBalance() - profsubcost)
            professional.setSubStatus(1)
            self.subscriberreport += "Professional Id: " + str(professional.getId()) + "\n"
            self.subscriberreport += "Time: " + str(professional.currentEvent.getEndTime()) + "\n"
            self.subscriberreport += "Cost: " + str(profsubcost) + "\n"
            self.subscriberreport += "Balance: " + str(professional.getBalance()) + "\n\n"
        self.servicereport += results

    def report(self):
        results = ""
        for professional in self.professionals:
            results += "Professional Id: " + str(professional.getId()) + "\n"
            if professional.getSubStatus() == 1:
                results += "Subscriber Status: Subscribed \n"
            else:
                results += "Subscriber Status: Unsubscribed \n"
            results += "Skill: " + str(professional.getSkill()) + "\n"
            results += "Reliability: " + str(professional.getReliability()) + "\n"
            results += "Speed: " + str(professional.getSpeed()) + "\n"
            results += "Amount of jobs serviced: " + str(professional.getAmountRated()) + "\n"
            results += "Average Rating: " + str(professional.getRating()) + "\n\n"
  

        self.professionalreport += results

    #Main driving code for the simulation
    def simulate(self):
        print("Simulate")
        professionals = self.professionals
        self.prof_c = len(professionals)
        nextFinish = None
        #Iterates through every event and allocates them to a respective professional. The system prioritises professionals that are not busy, and if all within the 50km radius are busy they queue instead. 
        #It prioritises the closest professional. Maybe if we had time we could change it so it further prioritises professionals who have the lowest queue. 
        for event in self.events:
            #At the start of the iteration of an event, it checks through all the working professionals and sees if they should be done by now.
            #If they are done, they finish the service and payments are made.
            while nextFinish is not None and nextFinish.currentEvent is not None and float(event.startTime) < float(nextFinish.currentEvent.endTime):
                self.time = float(nextFinish.currentEvent.endTime)
                self.payment(nextFinish, self.clients[int(nextFinish.currentEvent.clientId)])
                self.finishService(nextFinish) 

                timerecord = 999999999999
                timerecordid = -1 
                for professional in self.professionals:
                    if professional.currentEvent != None:
                        if professional.currentEvent.getServiceTime() < timerecord:
                            timerecord = professional.getCurrentEvent.getServiceTime()
                            timerecordid = professional.getId()
                if timerecordid == -1:
                    continue
                else:
                    nextFinish = professionals[int(timerecordid)]

            #If there are professionals who are not busy in the system, it looks through all the professionals that aren't busy and finds the closest one.
            distancerecord = 50
            distanceid = 0
            allbusyrad = 0
            if self.prof_c > self.busy_c:
                for professional in self.professionals:
                    distance = self.calculateTravel(professional, event)
                    if distance < distancerecord and professional.getTrade() == event.getTrade() and professional.getCurrentEvent() is None:
                        distancerecord = distance
                        distanceid = professional.getId()
                if distancerecord == 50:
                    allbusyrad = 1
        

            if self.prof_c <= self.busy_c or allbusyrad == 1:
                
                allbusyrad = 0
                for professional in self.professionals:    
                    distance = self.calculateTravel(professional, event)
                    if distance < distancerecord and event.getTrade() == professional.getTrade():
                        distancerecord = distance
                        distanceid = professional.getId()
                if distancerecord == 50:
                    print("No professional within 50km")


            professional = professionals[distanceid]
            if professional.currentEvent is None:

                event.setEndTime(self.calculateServiceTime(event, professional) + self.time)
                professional.currentEvent = event
                if nextFinish is None or nextFinish.currentEvent is None or event.endTime < float(nextFinish.currentEvent.endTime):
                    nextFinish = professional

            else:
                self.enqueue(professional, event)
        self.report()
        print(self.servicereport)
        print(self.subscriberreport)
        print(self.professionalreport)
        results = self.servicereport
        results += self.subscriberreport
        results += self.professionalreport
        with open("results.txt", "w") as f:
            f.write(results)
        
    def readFile(self):
        with open('test_data.txt') as data_file:
        
            lines = data_file.readlines()[1:]
            for line in lines:
                if line == "clients\n":
                    continue
                if line == "<=====>\n":
                    break
                clientval = line.split(",")
                self.clients.append(Client(clientval[0], clientval[1], clientval[2], clientval[3], clientval[4]))

            
            trigger = 0
            for line in lines:
                if trigger == 0:

                    if "tradies" in line:
                        trigger = 1

                    continue

                if line == "<=====>\n":
                    break
                profval = line.split(",")
                self.professionals.append(Professional(profval[0], profval[1],profval[2],profval[3],profval[4],profval[5],profval[6],profval[7],profval[8], profval[9]))

            
            trigger = 0
            for line in lines:
                if trigger == 0:
                    if line == "events\n":
                        trigger = 1
                    continue
                if line == "events\n":
                    continue
                if "<=====>" in line:
                    break
                line = line.replace('(', '').replace(')','')
                eventval = line.split(",")
                self.events.append(Event(eventval[0], eventval[1], eventval[2], eventval[3]))


    

        

#This is code to read in the test_data.txt file and turn it into the arrays, not sure where it should go
if __name__ == "__main__":
    simulator = Simulation()
    simulator.readFile()
    simulator.simulate()










