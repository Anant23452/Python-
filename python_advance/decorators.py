# decorators is a function that takes a function, it creates a new functin insider ti s body(wrapper) .then it returns that new function 
def decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper
    # first method 
@decorator
def say_hello():
    print("Hello, World!")
say_hello()
print("===================================")
# second method 
f = decorator(say_hello)
f()

