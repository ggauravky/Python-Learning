from functools import wraps

def log_function_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling function '{func.__name__}' with arguments: {args} and keyword arguments: {kwargs}")
        result = func(*args, **kwargs)
        print(f"Function '{func.__name__}' returned: {result}")
        return result
    return wrapper

def require_authentication(func):
    @wraps(func)
    def wrapper(user, *args, **kwargs):
        if not user.get('is_authenticated', False):
            print("Authentication required to access this function.")
            return None
        return func(user, *args, **kwargs)
    return wrapper

@log_function_call
@require_authentication

def view_profile(user):
    return f"User Profile: {user.get('name', 'Unknown')}"

# Example usage
authenticated_user = {'name': 'Alice', 'is_authenticated': True}
view_profile(authenticated_user)
