class ChaiOrder:
    def __init__(self, tea_type, sweetness, size):
        self.tea_type = tea_type
        self.sweetness = sweetness
        self.size = size

    @classmethod
    def from_dict(cls, order_data):
        return cls(
            order_data["tea_type"],
            order_data["sweetness"],
            order_data["size"],
        )
    
    @classmethod
    def from_string(cls, order_string):
        tea_type, sweetness, size = order_string.split("-")
        return cls(tea_type, sweetness, size)
    
class ChaiUtils:
    @staticmethod
    def is_valid_size(size):
        return size in ["Small", "Medium", "Large"]


print(ChaiUtils.is_valid_size("Medium"))

order1 = ChaiOrder.from_dict({"tea_type": "masala", "sweetness": "medium", "size":"Large"})

order2 = ChaiOrder.from_string("Ginger-Low-Small")

order3 = ChaiOrder("Large", "Low", "Large")

print(order1.__dict__)
print(order2.__dict__)
print(order3.__dict__)

# what is constructor? 
# A constructor is a special method in a class that is automatically called when an object of that class is created. It is typically used to initialize the object's attributes and allocate any necessary resources. In Python, the constructor method is defined using the __init__() method.

# what is class method?
# A class method is a method that is bound to the class and not the instance of the class. It takes the class itself as the first argument, conventionally named cls. Class methods are often used for factory methods that create instances of the class using different input data or formats. They are defined using the @classmethod decorator.

# what is static method?
# A static method is a method that does not receive an implicit first argument (neither self nor cls). It behaves like a regular function but belongs to the class's namespace. Static methods are used for utility functions that are related to the class but do not need to access or modify the class or instance state. They are defined using the @staticmethod decorator.