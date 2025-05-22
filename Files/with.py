# f = open("anant.txt","r")
# content = f.read()
# print(content)
# f.close()


with open("anant.txt","r") as f: #context manager
    content = f.read()
    print(content)
    #no need to cloase the file explicity