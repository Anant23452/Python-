from matplotlib import pyplot as plt

x=['Audi', 'BMW', 'Mercedes', 'Toyota', 'Honda']
y=[20,20,20,20,20]
# y=[2, 3, 5, 7, 11]

plt.pie(y,labels=x)

plt.legend()
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.show()