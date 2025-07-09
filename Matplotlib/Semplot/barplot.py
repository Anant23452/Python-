from matplotlib import pyplot as plt

x=['Audi', 'BMW', 'Mercedes', 'Toyota', 'Honda']
y=[2,3,5,7,11]

plt.bar(x,y,label="Vehicles",color="red",width=0.4,)
plt.legend()
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.xlabel('X-axis')
plt.ylabel("y-axis")
plt.title('Bar Plot Example')

plt.show()