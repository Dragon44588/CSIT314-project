class Event:
    def __init__(self, clientId, startTime, serviceTime, performance, trade):
        self.clientId = clientId
        self.startTime = startTime
        self.serviceTime = serviceTime
        self.performance = performance
        self.nextEvent = None
        self.trade = trade

    def __repr__(self):
        return "{},{},{},{},{},{}".format(self.clientId, self.startTime, self.serviceTime, self.performance, self.nextEvent, self.trade)
        

    def getClientId(self):
        return self.clientId
    
    def getStartTime(self):
        return self.startTime
    
    def setStartTime(self, startTime):
        self.startTime = startTime

    def getserviceTime(self):
        return self.serviceTime
    
    def setStartTime(self, serviceTime):
        self.serviceTime = serviceTime
    
    def getPerformance(self):
        return self.performance
    
    def setPerformance(self, performance):
        self.performance = performance
        
    def getNextEvent(self):
        return self.nextEvent
    
    def setNextEvent(self, nextEvent):
        self.nextEvent = nextEvent

    def getNextTrade(self):
        return self.trade
    
    def setNextEvent(self, trade):
        self.trade = trade