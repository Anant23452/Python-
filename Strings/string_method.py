name ="anantttt"
a = len(name) # length of string
print(a) 
print(name.upper()) # convert string to upper case
print(name.lower()) # convert string to lower case
print(name.replace("a","A")) # replace a with A in string
print(name.find("a")) # find the first occurrence of a in string


text = "anant,banant,canant"
print(text.split(",")) # split the string into a list of strings using , as separator
print(text.split("a")) # split the string into a list of strings using a as separator

name = "Hello Python!"
print(name[::2])