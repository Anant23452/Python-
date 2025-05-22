import os

a = os.listdir("dir")
print(a)
#current working directory
print(os.getcwd())
#is diretory available or not
print(os.path.exists("dir"))

os.remove("sample.txt")

