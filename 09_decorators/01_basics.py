from functools import wraps
def my_decorator(func):
    @wraps(func)
    def wrapper():
        print("Before the function call.")
        func()
        print("After the function call.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")
    
say_hello()
print(say_hello.__name__)  # Output: say_hello