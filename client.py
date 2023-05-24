from users import User

class Client(User):
    def __init__(self, id, name, subscriber, xcoord, ycoord):
        self.id = id
        self.name = name
        self.balance = 0
        self.subscriber = subscriber
        self.xcoord = xcoord
        self.ycoord = ycoord

    def __repr__(self):
        return "{},{},{},{},{}".format(self.id, self.name, self.subscriber, self.xcoord, self.ycoord)

    def subscribe(self):
        print("Currently a subscriber?: {}".format(self.subStatus))
        
    def payOnDemand(self):
        print("pay on demand")

    def appendJob(self, job):
        self.jobs.append(job)
        
    