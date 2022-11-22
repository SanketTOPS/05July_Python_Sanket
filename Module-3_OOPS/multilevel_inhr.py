class grand_father:
    house=0
    gold=0

    def g_getdata(self):
        self.house=input("Enter House details:")
        self.gold=input("Enter Gold details:")

class father(grand_father):
    car=0
    bal=0

    def f_getdata(self):
        self.car=input("Enter Car details:")
        self.bal=input("Enter Bank balance details:")

class son(father):
    def allprop(self):
        print("HOuse:",self.house)
        print("Gold:",self.gold)
        print("Car:",self.car)
        print("Bank Balance:",self.bal)
    
sn=son()
sn.g_getdata()
sn.f_getdata()
sn.allprop()