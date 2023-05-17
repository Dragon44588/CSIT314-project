from users import User
from math import sqrt

class Professional(User):
    def __init__(self, id, name, balance, subscriber, xcoord, ycoord, skill, reliability, speed):
        self.id = id
        self.name = name
        self.balance = balance
        self.subscriber = subscriber
        self.xcoord = xcoord
        self.ycoord = ycoord
        self.nextEvent = None
        self.skill = skill
        self.reliability = reliability
        self.speed = speed
        self.rating = 0
        self.amountRated = 0
        
    def __str__(self):
        return "ID: {:<2} Name: {:<10} Bal: ${:<5} Sub Status: {:<2} X-Coord: {:<3} Y-Coord: {:<3} Next Event: {} Skill: {:<3} Reliability: {:<3} Speed: {:<2} Rating: {:<3} Ammount Rated: {:<3}".format(self.id, self.name, self.balance, self.subscriber, self.xcoord, self.ycoord, self.nextEvent, self.skill, self.reliability, self.speed, self.rating, self.amountRated)

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