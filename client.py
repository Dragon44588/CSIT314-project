from users import User

class Client(User):
    def __init__(self, id, name, balance, subscriber, xcoord, ycoord):
        self.id = id
        self.name = name
        self.balance = balance
        self.subscriber = subscriber
        self.xcoord = xcoord
        self.ycoord = ycoord
        self.jobs = []

    def __str__(self):
        return "ID: {:<2} Name: {:<20} Balance: {:<5} Subscriber Status: {:<3} X-Coordinate: {:<3} Y-Coordinate: {:<3} Jobs: {}".format(self.id, self.name, self.balance, self.subscriber, self.xcoord, self.ycoord, self.jobs)

    def subscribe(self):
        print("Currently a subscriber?: {}".format(self.subStatus))
        
    def payOnDemand(self):
        print("pay on demand")

    def appendJob(self, job):
        self.jobs.append(job)
        
    