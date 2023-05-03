from users import User

class Client(User):
    def __init__(self, id, balance, subscriber, xcoord, ycoord):
        self.id = id
        self.balance = balance
        self.subscriber = subscriber
        self.xcoord = xcoord
        self.ycoord = ycoord
        self.jobs = []

    

    def subscribe(self):
        print("Currently a subscriber?: {}".format(self.subStatus))
        
    def payOnDemand(self):
        print("pay on demand")

    def appendJob(self, job):
        self.jobs.append(job)
        
    