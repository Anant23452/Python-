list=[4,7,5,4,3,6,8,9,10,12,15,20,25,30,35,40,45,50]
larger_number=list[0]
for i in list:
    if i>larger_number:
        larger_number=i

print("The largest number in the list is:", larger_number)  # Output: The largest number in the list is: 50
# This code iterates through the list and finds the largest number by comparing each element with the