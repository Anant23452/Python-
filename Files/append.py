# This program demonstrates how to append data to a file in Python.
#john address and where he work all time 
f = open("john_doe.txt","a")
string ='''
John doe intially lived in phoenix,arizona .He is ver nice guy
He is a software engineer and he is working in a company called google
'''
f.write(string)
f.close()