from users import User
from math import sqrt

class Professional(User):
    def __init__(self, id, name, balance, subscriber, xcoord, ycoord, nextEvent, skill, reliability, speed, rating, amountRated):
        self.id = id
        self.name = name
        self.balance = balance
        self.subscriber = subscriber
        self.xcoord = xcoord
        self.ycoord = ycoord
        self.nextEvent = nextEvent
        self.skill = skill
        self.reliability = reliability
        self.speed = speed
        self.rating = rating
        self.amountRated = amountRated
        
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
        
    def getEvent(self):
        return self.nextEvent
    
    def calculateTravel(self, clientXCoord, clientYCoord):
        return round(sqrt((clientXCoord - self.xcoord)**2 + (clientYCoord - self.ycoord)**2), 2)