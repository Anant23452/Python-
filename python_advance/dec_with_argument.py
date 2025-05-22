def repeat(n):
    def decorator(func):
        def wrapper(a):
            for i in range(n):
                func(a)
        return wrapper
    return decorator
@repeat(3)
def say_hello(a):
    print(f"hello {a}")
""" 
It repalces the functino say_hellp with this:
def decorator(func):
    def wrapper(a);
        for i in range(3):
            say_hello(a)
    return wrapper
"""

say_hello("John")