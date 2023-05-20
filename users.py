class User:
    def __init__(self, id, name, balance, subscriber, xcoord, ycoord):
        self.id = id
        self.name = name
        self.balance = balance
        self.subscriber = subscriber
        self.xcoord = xcoord
        self.ycoord = ycoord

    def getId(self):
        return self.id
        
    def setId(self, id):
        self.id = id

    def getName(self):
        return self.name
        
    def setName(self, name):
        self.name = name
        
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