from functools import wraps

def log_activity(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"🚀Calling function: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"✅Function {func.__name__} returned: {result}")
        return result
    return wrapper

@log_activity
def brew_chai(type,milk="whole"):
    print(f"Brewing a cup of {type} chai.. and adding {milk} milk.")

    
   
brew_chai("masala")