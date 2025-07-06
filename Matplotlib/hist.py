from matplotlib import pyplot as plt
# Data for the pie chart
marks = [15, 30, 45, 10,15,23,54,75,34,23,5,3,6,10,75,34]
plt.hist(marks, bins=4, color='blue', edgecolor='r',label="line")
plt.title("histogram")
plt.xlabel("marks ")
plt.ylabel("numbers of students")
plt.legend()
plt.show()