number =[1,23,4,5,6,7,8,9,10]
def square(n):
    return n*n
new = map(square,number)
# map() returns a map object (which is an iterator)
new = list(map(square,number))
new = list(map(lambda x: x*x,number))
# lambda function is a small anonymous function
print(new)