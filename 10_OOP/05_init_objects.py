class chaiorder:
    def __init__(self,type_,size):
        self.type=type_  #_ to avoid conflict with keyword type
        self.size=size
    
    def summery(self):
        return f"a {self.size} ml {self.type} chai"
    
order=chaiorder("masala",200)
print(order.summery())  

order_two=chaiorder("ginger",150)
print(order_two.summery())