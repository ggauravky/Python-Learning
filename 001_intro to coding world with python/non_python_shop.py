class chai:
    def __init__(self, sweetness , milk_level):
        self.sweetness=sweetness
        self.milk_level=milk_level
        
    def sip(self):
        print("Sipping chai")
    
    def add_sugar(self,amount):
        print("added the suger")
    
my_chai=chai(sweetness=3,milk_level=2)

my_chai.add_sugar(3)
my_chai.add_sugar(5)

