from matplotlib  import pyplot as plt
# Data for the bar plot
x = ["A", "B", "C", "D", "E"]
y = [3, 7, 5, 8, 6]

x2=["cat1", "cat2", "D", "C", "cat5"]
y2=[1, 2, 3, 4, 5]

x3 =[1,2,3,4,5]
y3 =[2,3,5,7,11]



# Create a bar plot
plt.bar(x,y, color='blue', width=0.4)
plt.bar(x2,y2,color='red',width=.25, 
        align='center')
plt.plot(x3,y3,'g',label='line one', linewidth=5)
plt.title("Bar Plot Example")
plt.xlabel("Categories")    
plt.ylabel("Values")
plt.show()