class chai:
    temperature="hot"
    strenght="strong"
    
cutting=chai()
print(cutting.temperature)

cutting.temperature="mild"
cutting.cup="small"
print("after changing:", cutting.temperature)
print("cup size is " ,cutting.cup)
print("direct look into the class:" , chai.temperature)

del cutting.temperature
del cutting.cup
print(cutting.temperature)
print(cutting.cup)