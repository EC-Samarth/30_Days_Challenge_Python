#Day_16 < Inheritence >

#1.Create a base class Person and derived class employee

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print(f"Name :{self.name}")
        print(f"Age : {self.age}")

class Employee(Person):
    def __init__(self , name ,age , employee_id,department):
        super().__init__(name,age)
        self.employee_id = employee_id
        self.department = department
    def display(self):
        super().display()
        print(f"Employee_id :{self.employee_id}")
        print(f"Departememt :{self.department}") 

person=Person("Harry",22 )
person.display()
print()
employee = Employee("Jerry",21,"E123","HR")
employee.display()
print()

""" Output 
Name :Harry
Age : 22

Name : Jerry
Age :21
Employee_id :E123
Departememt :HR """

#2.add method overiding

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print(f"Name :{self.name}")
        print(f"Age : {self.age}")
    def greet(self):
        print(f"Hello,My name is {self.name}")

class Employee(Person):
    def __init__(self , name ,age , employee_id,department):
        super().__init__(name,age)
        self.employee_id = employee_id
        self.department = department
    def display(self):
        super().display()
        print(f"Employee_id :{self.employee_id}")
        print(f"Departememt :{self.department}") 
    def greet(self):
        super().greet()
        print(f"I work in the {self.department}")

person=Person("Harry",22 )
person.display()
person.greet()
print()
employee = Employee("Jerry",21,"E123","HR")
employee.display()
employee.greet()

""" Output 
Name :Harry
Age : 22
Hello,My name is Harry

Name :Jerry
Age : 21
Employee_id :E123
Departememt :HR
Hello,My name is Jerry
I work in the HR"""

