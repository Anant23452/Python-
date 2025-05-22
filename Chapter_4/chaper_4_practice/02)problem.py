marks =[]

f1 = int(input("Enter the first mark:"))
marks.append(f1)

f2 = int(input("Enter the second mark:"))
marks.append(f2)

f3 = int(input("Enter the third mark:"))
marks.append(f3)

print("The marks are:",marks)
marks.sort()
print("The sorted marks are:",marks)