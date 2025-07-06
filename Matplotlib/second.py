from matplotlib import pyplot as plt
from matplotlib import style
style.use('ggplot')

x =[3,5,6,7,8]
y =[2,3,5,7,11]

x2 =[1, 2, 3, 4, 5]
y2 =[1, 4, 6, 8, 11]

plt.plot(x,y,'g',label='line one', linewidth=5)
plt.plot(x2,y2,'r',label='line two', linewidth=5)

plt.title("Two Lines on the Same Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()

plt.grid(True,color='r', linestyle='--', linewidth=0.5)
plt.show()

