#mro -> Method Resolution Order

class A:
    label = "A: base class A"

class B(A):
    label = "B: derived class B"
    
class C(A):
    label = "C: derived class C"
    
class D(B, C):
    pass

cup=D()
print(cup.label)  # Output: B: derived class B
print(D.mro())    # Output: [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
# In the above example, class D inherits from both B and C. When we access the label attribute from an instance of D, Python follows the MRO to determine which label to use. Since B is listed before C in the inheritance list of D, the label from B is used.

print(D.__mro__)  # Output: (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
# The __mro__ attribute provides the same information as the mro() method but in tuple form.
# The MRO is determined using the C3 linearization algorithm, which ensures a consistent order of method resolution in the presence of multiple inheritance.
# Understanding MRO is crucial when designing class hierarchies in Python, especially when multiple inheritance is involved, as it affects how methods and attributes are resolved.

