class employee:
    campany = "Google" #class attribute

    def __init__(self,salary,name,campany):# constructor method
        self.salary = salary
        self.name =name
        self.campany = campany
    def get_salary(self):
        return self.salary
    
    def get_info(self):
        print(f"The name of the employee is {self.name}.slary si {self.salary}.and the company is {self.campany}")

e1 = employee(1000,"john","tesla")# will always print instance attribute whenever present
print(e1.campany)
print(employee.campany)# will always print class attribute

#object introspection
print(dir(e1))# will print all the attributes and methods of the object