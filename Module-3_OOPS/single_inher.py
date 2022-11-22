class father:
    car=0
    bal=0
    def getdata(self):
        self.car=input("Enter car detail:")
        self.bal=input("Enter bank balance details:")

class son(father):
    def usePrope(self):
        print("Total Car:",self.car)
        print("Total Bank Balance:",self.bal)

sn=son()
sn.getdata()
sn.usePrope()