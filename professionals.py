from users import User
from math import sqrt

class Professional(User):
    def __init__(self, id, balance, subscriber, xcoord, ycoord, currentEvent, nextEvent, skill, reliability, speed, rating, amountRated, trade):
        self.id = id
        self.balance = balance
        self.subscriber = subscriber
        self.xcoord = xcoord
        self.ycoord = ycoord
        self.currentEvent = currentEvent
        self.nextEvent = nextEvent
        self.skill = skill
        self.reliability = reliability
        self.speed = speed
        self.rating = rating
        self.amountRated = amountRated
        self.trade = trade

        
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