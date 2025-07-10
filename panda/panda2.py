import pandas as pd
data={
    "name":["Anshika","Rahul","Priya","Vijay","Simran","Aman","Shruti"],
    "roll_no":[101,102,103,104,105,106,107],
    "age":[20,21,19,22,20,23,21],
    "marks":[85,78,92,65,74,88,81],
}

a = pd.DataFrame(data)


print(a)
# Save as Excel file
a.to_json("panda/man.json")
# Read the
#  Excel file
read = pd.read_json("panda/man.json")
print(read)
