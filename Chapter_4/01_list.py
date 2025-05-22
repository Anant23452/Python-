friends =["apple", "banana", "cherry", 5, 234, 3.14,False,"ankit"]
print(friends[1])
friends[2] ="mango"
print(friends)  #unlike strings,lists are mutable
print(friends[1:4]) #slicing
print(friends[-1]) #negative indexing
l1 = [1,2,6,7,4,8,555,44,9]
# l1.sort() #sorts the list in ascending order
# print(l1)
# l1.sort(reverse=True) #sorts the list in descending order
# print(l1)
l1.insert(2,100) #inserts 100 at index 2
print(l1)

l1.pop(2) #removes the element at index 2
print(l1)