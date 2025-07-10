import pandas as pd
import pandas as pd


data = {
    'Roll_No': [101, 102, 103, 104, 105, 106, 107],
    'Name': ['Anshika', 'Rahul', 'Priya', 'Vijay', 'Simran', 'Aman', 'Shruti'],
    'Age': [20, 21, 19, 22, 20, 23, 21],
    'Marks': [85, 78, 92, 65, 74, 88, 81],
    'City': ['Lucknow', 'Kanpur', 'Varanasi', 'Gorakhpur', 'Allahabad', 'Lucknow', 'Kanpur']
}
series = pd.Series(data['Marks'])

df = pd.DataFrame(data)

# Save as Excel file
df.to_excel("student_data.xlsx", index=False, sheet_name="Students")

pf =pd.read_excel("student_data.xlsx", sheet_name="Students")
print(pf)
print(series)