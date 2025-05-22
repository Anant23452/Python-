#string formatting
template = "Hello, my name is {} and I am {} years old."
a = "anant"
a1= 20
b = "ram"
b1 = 30
c = "shyam"
c1 = 40

s1 = template.format(a, a1)
print(s1)
s2 = template.format(b,b1)
print(s2)
s3 = template.format(c,c1)
print(s3)

#using f-string
print(f"Hello, my name is {a} and I am {a1} years old.")
print(f"Hello, my name is {b} and I am {b1} years old.")