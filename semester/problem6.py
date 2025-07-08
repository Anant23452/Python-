text = input("Enter a string: ")

alpha = ""
digit = ""

for char in text:
    if char.isalpha():
        alpha = alpha + char
    elif char.isdigit():
        digit = digit + char

file = open("semester/semester.txt", "w")
file.write("Alphabets:" + str(alpha) + "\n")
file.write("Digits:" + str(digit) + "\n")
file.close()