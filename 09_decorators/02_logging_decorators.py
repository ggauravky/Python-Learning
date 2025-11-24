from functools import wraps

def log_activity(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        print(f"Arguments: args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} returned: {result}")
        return result
    return wrapper

@log_activity
def add(a, b):
    return a + b

@log_activity
def multiply(a, b):
    return a * b

# Example usage
add(3, 5)
multiply(4, 6)