from matplotlib import pyplot as plt
# Data for the line plot
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Create a line plot
plt.plot(x,y, color='r',label='Line One', linewidth=2)
plt.title("Line Plot Example")
plt.xlabel("X-axis")    
plt.ylabel("Y-axis")
plt.scatter(x, y, color='blue', label='Data Points')
plt.legend()
plt.show()