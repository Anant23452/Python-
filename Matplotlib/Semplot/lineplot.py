from matplotlib import pyplot as plt

x=[1,2,3,4,5,4,6]
y=[9,8,7,5,4,3,2]

x1=[7,6,4,3,2,11,5]
y1=[2,3,7,11,9,6,5]


plt.plot(x1,y1,label="line 2",color="green",linewidth=4,marker='x')


plt.plot(x,y,label="line 1",color="red",linewidth=2,linestyle ="--",marker='o')
plt.legend()

plt.title("line plot")
plt.xlabel("x-axis")
plt.ylabel("y-axis")

plt.show()
