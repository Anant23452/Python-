sentence = "lorem ipsum dolor sit amet, consectetur adipiscing elit"
words = sentence.split()  # Split the sentence into words
count =0
for word in words:
    count+=1
    print(word)  # Print each word
    # You can also perform other operations on each word if needed
print(f"Total words: {count}")  # Print the total number of words

m=0
name = "John Doe"
for c in name:
    m=m+1
    print(c,)  # Print each character in the name

print(f"Total characters: {m}")  # Print the total number of characters