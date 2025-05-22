from functools import reduce
a =[1,3,4,5,6,7,3,]
def add(x,y):
    return x+y
# reduce() applies a rolling computation to sequential pairs of values in a list
b = reduce(add,a)
print("the reduce value of a:",b)