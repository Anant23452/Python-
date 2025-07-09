from matplotlib import pyplot as plt

days=['monday', 'tuesday', 'wednesday', 'thursday', 'friday']
sales=[20, 35, 30, 35, 27]

plt.fill_between(days,sales,color='lime', linewidth=2, alpha=0.4)

plt.title('Sales Over Days of the Week')
plt.xlabel('Days of the Week')
plt.ylabel('Sales')
plt.legend(['Sales'], loc='upper left')
plt.show()