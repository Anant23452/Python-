n = int(input("Enter a number: "))
a,b =0,1
flag =False

while a<=n:
    if a ==n:
        flage =True
        break
    a,b = b,a+b

if flag:
    print(n,"is a fibonacci number")
else:
    print(n,"is not a fibonacci number")