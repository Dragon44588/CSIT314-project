class Event:
    def __init__(self, clientId, startTime, serviceTime, trade):
        self.clientId = clientId
        self.professionalId = None
        self.startTime = startTime
        self.serviceTime = serviceTime
        self.endTime = 0
        self.performance = None
        self.nextEvent = None
        self.trade = trade

    def __repr__(self):
        return "{},{},{},{}".format(self.clientId, self.startTime, self.serviceTime, self.trade)
        

    def getClientId(self):
        return int(self.clientId)
    
    #Start time does not refer to the time that an event starts being processed but instead the time the event enters the system
    # i.e. The time the event enters the first come first serve queue
    def getStartTime(self):
        return float(self.startTime)
    
    def setStartTime(self, startTime):
        self.startTime = startTime

    def getServiceTime(self):
        return float(self.serviceTime)
    
    def setServiceTime(self, serviceTime):
        self.serviceTime = serviceTime
    
    def getEndTime(self):
        return int(self.endTime)
    
    def setEndTime(self, endTime):
        self.endTime = endTime

    def getPerformance(self):
        return self.performance
    
    def setPerformance(self, performance):
        self.performance = performance
        
    def getNextEvent(self):
        return self.nextEvent
    
    def setNextEvent(self, nextEvent):
        self.nextEvent = nextEvent

    def getTrade(self):
        return int(self.trade)
    
    def setTrade(self, trade):
        self.trade = trade