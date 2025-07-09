from matplotlib import pyplot as plt
x=['Audi', 'BMW', 'Mercedes', 'Toyota', 'Honda']
y=[2,3,5,7,11]

plt.hist(x,bins=5,alpha=0.7, color='blue', edgecolor='black', label='Car Brands')
plt.legend()
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability







plt.xlabel("Car Brands")
plt.ylabel("Number of Cars Sold")
plt.title("Histogram of Car Sales")
plt.show()
