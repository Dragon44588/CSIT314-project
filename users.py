class User:
    def __init__(self, id, balance, subscriber, xcoord, ycoord):
        self.id = id
        self.balance = balance
        self.subscriber = subscriber
        self.xcoord = xcoord
        self.ycoord = ycoord

    def getId(self):
        return self.id
        
    def setId(self, id):
        self.id = id
        
    def getBal(self):
        return self.balance
    
    def setBal(self, balance):
        self.balance = balance   
        
    def subStatus(self):
        return self.subscriber
    
    def setSubStatus(self, isSubbed):
        self.subscriber = isSubbed
        
    def getXCoord(self):
        return self.xcoord
    
    def setXCoord(self, xcoord):
        self.xcoord = xcoord
        
    def getYCoord(self):
        return self.ycoord
    
    def setYCoord(self, ycoord):
        self.ycoord = ycoord