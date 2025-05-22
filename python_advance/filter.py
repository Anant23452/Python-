def is_greater_than_6(x):
    if x>6:
        return True
    else:
        return False
a = [1,2,3,4,5,6,7,8,9,10]
b =list(filter(is_greater_than_6,a))
print(b)
# filter() returns an iterator where the function returns True

b1 = list(filter(lambda x: x>4,a))
print(b1)