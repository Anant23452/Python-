# Input string from user
text = input("Enter any string: ")

# Create empty strings
letters = ""
digits = ""

# Separate characters
for ch in text:
    if ch.isalpha():
        letters += ch
    elif ch.isdigit():
        digits += ch

# Open file to write
with open("output.txt", "w") as file:
    file.write("Letters: " + letters + "\n")
    file.write("Digits: " + digits + "\n")

print("Data written to output.txt")
