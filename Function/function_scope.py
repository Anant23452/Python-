def sum():
    # a and b are local variables
    c = a+b 
    z =1 # it creats a local varable called z which is destroyed after this fucntion reamains
    return c 

z = 8 # z is a global variable 

print(sum(3,4))