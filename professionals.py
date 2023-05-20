from users import User
from math import sqrt

class Professional(User):
    def __init__(self, id, name, balance, subscriber, xcoord, ycoord, skill, reliability, speed, trade):
        self.id = id
        self.name = name
        self.balance = balance
        self.subscriber = subscriber
        self.xcoord = xcoord
        self.ycoord = ycoord
        self.nextEvent = None
        self.currentEvent = None
        self.skill = skill
        self.reliability = reliability
        self.speed = speed
        self.rating = 0
        self.amountRated = 0
        self.trade = trade
        
    def __repr__(self):
        return "{},{},{},{},{},{},{},{},{},{},{},{},{},{}".format(self.id, self.name, self.balance, self.subscriber, self.xcoord, self.ycoord, self.nextEvent, self.currentEvent, self.skill, self.reliability, self.speed, self.rating, self.amountRated, self.trade)

    def getSkill(self):
        return self.skill
    
    def setSkill(self, skill):
        self.skill = skill
        
    def getReliability(self):
        return self.reliability
    
    def setReliability(self, reliability):
        self.reliability = reliability
        
    def getSpeed(self):
        return self.speed
    
    def setSpeed(self, speed):
        self.speed = speed

    def getcurrentEvent(self):
        return self.nextEvent
    
    def setcurrentEvent(self, currentEvent):
        self.currentEvent = currentEvent
 
    def getNextEvent(self):
        return self.nextEvent
    
    def setNextEvent(self, nextEvent):
        self.nextEvent = nextEvent
       
    def getTrade(self):
        return self.trade
    
    def setTrade(self, trade):
        self.trade = trade
    
    def calculateTravel(self, clientXCoord, clientYCoord):
        return round(sqrt((clientXCoord - self.xcoord)**2 + (clientYCoord - self.ycoord)**2), 2)