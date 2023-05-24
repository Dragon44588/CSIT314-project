class User:
    def __init__(self, id, name, subscriber, xcoord, ycoord):
        self.id = id
        self.name = name
        self.balance = 0
        self.subscriber = subscriber
        self.xcoord = xcoord
        self.ycoord = ycoord

    def getId(self):
        return int(self.id)
        
    def setId(self, id):
        self.id = id

    def getName(self):
        return self.name
        
    def setName(self, name):
        self.name = name
        
    def getBalance(self):
        return self.balance
    
    def setBalance(self, balance):
        self.balance = balance   
        
    def getSubStatus(self):
        return int(self.subscriber)
    
    def setSubStatus(self, isSubbed):
        self.subscriber = isSubbed
        
    def getXCoord(self):
        return float(self.xcoord)
    
    def setXCoord(self, xcoord):
        self.xcoord = xcoord
        
    def getYCoord(self):
        return float(self.ycoord)
    
    def setYCoord(self, ycoord):
        self.ycoord = ycoord