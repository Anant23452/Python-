# Two type of modules in python:
# -Build in modules
# -extenral modules
import math
import os
import mymodule # import mymodule 

print(math.sqrt(16))
print(math.factorial(5))
mymodule.hello() #printing the content inside mymodule
print(mymodule.__name__) # printing the name of the module

#for external modules installation
#pin install <module_name>