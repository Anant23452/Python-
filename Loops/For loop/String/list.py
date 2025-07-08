cars=['audi','bmw','benz','toyota']
c=0;
for car in cars:
 print(car, end=" ")
 c=c+1
print(f"\nTotal cars: {c}")  # Print the total number of cars
print("length of cars:", len(cars))  # Print the length of the list
#  list cpmprehension= [car for car in cars]
cars =['audi','bmw','benz','toyota']
[print(car, end=" ")for car in cars]

#range
car =['audi','bmw','benz','toyota']
for i in range(len(car)):
    print(car[i], end=" ")
