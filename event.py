class Event:
    def __init__(self, clientId, startTime, serviceTime, performance, nextEvent):
        self.clientId = clientId
        self.startTime = startTime
        self.serviceTime = serviceTime
        self.performance = performance
        self.nextEvent = nextEvent
        
    def getClientId(self):
        return self.clientId
    
    def getStartTime(self):
        return self.startTime
    
    def setStartTime(self, startTime):
        self.startTime = startTime
        
    def getPerformance(self):
        return self.performance
    
    def setPerformance(self, performance):
        self.performance = performance
        
    def getNextEvent(self):
        return self.nextEvent