def sum(a,b):
    c = a+b 
    global z # this will make z a global variable
    z =0 #this will refer to global z and not create a local variable
    return c

z =8 # global variable
print(sum(3,4))
print(z)