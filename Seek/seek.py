f = open("seek/seek.txt", "w+")
f.write("This is a test file.\n")
f.seek(6)  # Move the cursor to the 6th byte
print(f.read())  # Read 4 bytes from the current position  
f.close()