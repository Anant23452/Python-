f = open("practice/readline.txt", "r")

while True:
    
    line = f.readline()
    if not line:
     break
    print(line.strip())
f.close()