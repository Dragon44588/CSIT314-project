from users import User
from math import sqrt

class Professional(User):
    def __init__(self, id, name, subscriber, xcoord, ycoord, skill, reliability, speed, price, trade):
        self.id = id
        self.name = name
        self.balance = 0
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
        self.price = price
        self.trade = trade
        
    def __repr__(self):
        return "{},{},{},{},{},{},{},{},{},{}".format(self.id, self.name, self.subscriber, self.xcoord, self.ycoord, self.skill, self.reliability, self.speed, self.price, self.trade)

    def getSkill(self):
        return int(self.skill)
    
    def setSkill(self, skill):
        self.skill = skill
        
    def getReliability(self):
        return int(self.reliability)
    
    def setReliability(self, reliability):
        self.reliability = reliability
        
    def getSpeed(self):
        return int(self.speed)
    
    def setSpeed(self, speed):
        self.speed = speed

    def getRating(self):
        return int(self.rating)
    
    def setRating(self, rating):
        self.rating = rating
    
    def getAmountRated(self):
        return int(self.amountRated)
    
    def setAmountRated(self, amountRated):
        self.amountRated = amountRated

    def getCurrentEvent(self):
        return self.nextEvent
    
    def setCurrentEvent(self, currentEvent):
        self.currentEvent = currentEvent
 
    def getNextEvent(self):
        return self.nextEvent
    
    def setNextEvent(self, nextEvent):
        self.nextEvent = nextEvent

    def getPrice(self):
        return int(self.price)
    
    def setTrade(self, price):
        self.price = price

    def getTrade(self):
        return int(self.trade)
    
    def setTrade(self, trade):
        self.trade = trade
    
    def calculateTravel(self, clientXCoord, clientYCoord):
        return round(sqrt((clientXCoord - self.xcoord)**2 + (clientYCoord - self.ycoord)**2), 2)