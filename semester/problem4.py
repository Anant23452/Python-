from shlex import join
n = input("Enter a string: ")
words = n.split()  # Split the string into words
sort = sorted(words)  # Sort the words in alphabetical order
print("Sorted words:", sort)  # Print the sorted list of words
# joined = join(sort)
# print("Joined words:", joined)  # Print the joined string of sorted words