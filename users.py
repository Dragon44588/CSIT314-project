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