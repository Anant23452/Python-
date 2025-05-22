# write tho a file callde john doe.txt 
# it should contain data about john doe 

f = open("john_doe.txt","w")
string ='''
John Doe is a fictional character commonly used as a placeholder name in legal contexts,


'''
f.write(string)
f.close()