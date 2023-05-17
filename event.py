class Event:
    def __init__(self, clientId, startTime, serviceTime, performance, nextEvent, trade):
        self.clientId = clientId
        self.startTime = startTime
        self.serviceTime = serviceTime
        self.performance = performance
        self.nextEvent = nextEvent
        self.trade = trade

    def getClientId(self):
        return self.clientId
    
    #Start time does not refer to the time that an event starts being processed but instead the time the event enters the system
    # i.e. The time the event enters the first come first serve queue
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