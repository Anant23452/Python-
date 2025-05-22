name ="Anant"
slic = name[-4:-1]
print(slic)
#same as 
print(name[1:4])
print(name[:4])#is same as pirnt(name[0:4 ])
print(name[1:])#is same as pirnt(name[1:5])

#sling with skipping value
word = "Amazing"
print(word[2:7:2])
#start from index 2 all the way till 7 (excluding 7) and skip every 2nd character