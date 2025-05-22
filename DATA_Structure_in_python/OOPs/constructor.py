class employee:
    def __init__(self,salary,name,bond):
        self.salary = salary #create an instance attribute of name salary and assign it with salary
        self.name = name
        self.bond = bond

    def get_salary(self):
        return self.salary

    def get_info(self):
        print(f"The name of the employee is {self.name}.salary is {self.salary} and bond is {self.bond}")

e1 = employee(1000,"john",2)
print(e1.get_salary())
e1.get_info()