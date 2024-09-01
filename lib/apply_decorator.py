def decorator_func(func):
    def wrapper(*args, **kwargs):
        print('Decorator Applied')
        return func(*args, **kwargs)
    return wrapper  # This should be outside the wrapper function

def apply_decorator(func):
    return decorator_func(func)

@apply_decorator
def say_hello(name):
    """Function to greet someone."""
    print(f'Hello, {name}!')

# Call the decorated function
say_hello('Keith')
