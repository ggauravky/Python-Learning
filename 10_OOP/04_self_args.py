class chaiCup:
    size=150 #ml
    
    def describe(self):
        return f"a {self.size} ml chai cup"
    
size=chaiCup()
print(size.describe())
#print(chaiCup.describe()) # unbound method call error
print(chaiCup.describe(size)) # passing instance explicitly

cup_two=chaiCup()
cup_two.size=250
print(chaiCup.describe(cup_two))