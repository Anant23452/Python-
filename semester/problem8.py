# Open the file in read mode
with open("ABC.txt", "r") as file:
    lines = file.readlines()

# Initialize counters
line_count = len(lines)
word_count = 0
char_count = 0

# Loop through each line
for line in lines:
    word_count += len(line.split())
    char_count += len(line)

# Print results
print("Total Lines:", line_count)
print("Total Words:", word_count)
print("Total Characters:", char_count)
