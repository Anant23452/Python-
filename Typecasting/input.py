a = input("Enter a number:")
# print(a+3)
 # This will cause an error because input() returns a string
# To fix this, we need to convert the input to an integer by typcasting
a =int(a)
print(a+3) # Now this will work because a is an integer
# The same can be done with float and complex numbers