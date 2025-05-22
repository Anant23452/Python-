def very_slow_func():
    print("I am a very slow function")
    print("I am a very slow function")
    print("I am a very slow function")
    print("I am a very slow function")
    print("I am a very slow function")
    print("I am a very slow function")
    return 50
# if (very_slow_func()>10):
#     print("I am a very slow function")
if ((a:=very_slow_func())>10):
    print(a)
else:
    print("Its not geater than 10")

# The walrus operator (:=) allows you to assign a value to a variable as part of an expression.
# This can be useful in situations where you want to use a value multiple times without having to repeat the calculation.
while(data:=input("Enter the value:")):
    print(f"the value is {data}")
    if data == "exit":
        break