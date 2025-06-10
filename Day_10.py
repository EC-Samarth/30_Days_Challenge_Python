#Day_10 <Functions>

#1.Simple functions 

def greet(name):
    print(f"Hello , {name}!")
greet("Sam")                  

#Output : Hello , Sam!

#2.Function with return value 
def add(a,b):
    return a+b 
result =add(4,5)
print(result)   #9

#3.Fuctions with default arguments

def greet(name,message = "Hello"):
    print(f"{message}","{name} !")
greet("Saksham")
greet("Sak","Hi")

""" Output 
Hello {name} !
Hi {name} ! """

#4.Function with keyword Arguments
def add (*args):
    return sum(args)
result = add(1,2,3,4,5)
print(result)  
""" Output 15"""

#5.Function with keywords Arguments
def person(**kwargs):
    print (f"Name : {kwargs['name']}, Age:{kwargs['age']}")
person(name ="Janny",age = 21)
""" Output Name : Janny, Age:21"""


#6.Create a function to calculate BMI
def bmi(w,h):
    return w/(h**2)
weight = float(input("Enter your weight in kg : "))
height = float(input("Enter your height in meter : "))
print(f"Your BMI is : {bmi(weight,height)}")

""" Output '
Enter your weight in kg : 55
Enter your height in meter : 2
Your BMI is : 13.75 """

#7.lambda function 
sqr = lambda x:x**2
print(sqr(6))    #36

#8.Create a recursive function of factorial
def fact(n):
     if n<0 :
         return "Factorial of negative value is not defined"
     if n==0 or n==1:
        return 1
     else:
        return n*fact(n-1)

n3 = int(input("Enter a number:"))
print(f"Factorial of {n3} is : {fact(n3)}")

""" Output
Enter a number:4
Factorial of 4 is : 24 """