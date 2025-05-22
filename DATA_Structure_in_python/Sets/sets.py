s ={12,4,5,6,67}
print(s,type(s))
# print(s[3])# we cannot access the elements of set using index

s.add(23)
print(s)
s.remove(4)
print(s)
# remove will raise an error if the element is not present
# s.remove(21) # uncommenting this line will raise an error
s.discard(5) # discard will not raise an error if the element is not present
print(s)