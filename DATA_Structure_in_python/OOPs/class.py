#class : class is a blueprint or a template for creating objects.
# eg- form for a exam that contain name , age electives,father's etc 

#object- specific instance created fromt eh template(class) 
# eg - form which contains the data for john doe

class employee:
    campany = "Google" #class variable

    def getSalary(self):# self is a reference to the current instance of the class
        return 1000 #instance method

e = employee()#creatina an object of employee class 
print(e.campany) #accessing class variable
print(e.getSalary())#accessing instance method