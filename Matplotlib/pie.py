from matplotlib import pyplot as plt
# Data for the pie chart

students = ['Alice', 'Bob', 'Charlie', 'David']
scores = [85, 90, 78, 92]

plt.pie(scores, labels=students , autopct='%1.1f%%', startangle=90, colors=['#ff9999','#66b3ff','#99ff99','#ffcc99'])
plt.title('Student Scores Distribution')
plt.figure(figsize=(8, 8) )
plt.show()