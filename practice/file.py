file = open("practice/file.txt","w")
file.write("This is a practice file.\n")

file.close()

file = open("practice/file.txt","r")
read = file.read()
print(read)
# print(file.readlines())
file.close()

file = open("practice/file.txt","a")
file.write("This is an appended line.\n")
file.close()

lines= ["anant","ankit","sachin","annnn"]



