def chai_customer():
    print("welcome ! What chai would you like?")
    chai_type = yield
    while True:
        print(f"preparing your {chai_type} chai")
        chai_type = yield 
        
stall=chai_customer()
next(stall)  # prime the generator

print(stall.send("Masala"))  # place order
print(stall.send("Ginger"))  # place order