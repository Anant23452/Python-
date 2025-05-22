# create a list contaning the table of 5
#first method to print table
table =[]
for i in range(1,11):
    table.append(5*i)
print(table)

#second method to print table
table1 = [5*i for i in range(1,11)]
print(table1)