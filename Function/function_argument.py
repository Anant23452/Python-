def add(a,b):# a,b are parameters
    return a+b


c = add(2,3)# 2,3 are arguments
print(c)
#default arguments jisko ham change bhi kar sakte hai uske value ko override kar sakte hai
def add(a,b,c =0):
    return a+b+c

#d = add(2,3) nothing change
d = add(2,3,4) # 2,3,4 are arguments override the parameter
print(d)

#keyword argument - which value is for which
e = add( b =2,a =4)
print(e)

