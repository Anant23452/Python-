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

file = open("practice/file.txt","r")
line = file.readline()
line2 = file.readlines()
print(line)
print(line2)
file.close()



