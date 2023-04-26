from users import User

class Client(User):
    pass

    def subscribe(self):
        print("Currently a subscriber?: {}".format(self.subStatus))
        
    def payOnDemand(self):
        print("pay on demand")
        
    