#Day_15 <Classes and Objects>

#1.Create a class Student with attributes and method to display info

class Student:
    def __init__(self,name,age,roll_no,course):
        self.name = name
        self.age = age
        self.roll_no = roll_no
        self.course = course

    def display(self):
        print(f"Name : {self.name}")
        print(f"Age : {self.age}")
        print(f"Roll_No. : {self.roll_no}")
        print(f"Course :{self.course}")

student1 = Student("Sam",20 ,111,"BCA")
student1.display()

""" Output 
Name : Sam
Age : 20
Roll_No. : 111
Course :BCA """

#2.Instantiate multiple students

class Student:
    def __init__(self,name,age,roll_no,course):
        self.name = name
        self.age = age
        self.roll_no = roll_no
        self.course = course

    def display(self):
        print(f"Name : {self.name}")
        print(f"Age : {self.age}")
        print(f"Roll_No. : {self.roll_no}")
        print(f"Course :{self.course}")

student1 = Student("Sam",20 ,111,"BCA\n")
student2 = Student("John",25,112,"B.Tech\n")
student3 = Student("Marry",28,113,"MBA\n")

student1.display()
student2.display()
student3.display()

""" Output 
Name : Sam
Age : 20
Roll_No. : 111
Course :BCA

Name : John
Age : 25
Roll_No. : 112
Course :B.Tech

Name : Marry
Age : 28
Roll_No. : 113
Course :MBA """