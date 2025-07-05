# f = open("practice/ap.txt","r")
# while True:
#     line = f.readline()
#     if not line:
#         break
#     print(line)

f = open("practice/readline.txt", "w")
line =['line 1\n', 'line 2\n', 'line 3\n']
f.writelines(line)
f.close()