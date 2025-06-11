#Day_11 <Modules and Math>

#1.Use math module to calculate square root , factorial ,sin
import math 

#calculate square root
number = 16 
sqrt = math.sqrt(number)
print(f"Square root of {number}:{sqrt}")

#calculate factorial
number = 5 
factorial = math.factorial(number)
print(f"Factorial of {number}:{factorial}")

#calculate sine
angle_in_radians = math.pi/2
sin = math.sin(angle_in_radians)
print(f"Sine of {angle_in_radians} radians : {sin}")

#calculate sine of angle in 90 degrees 
angle_in_degrees = 90
angle_in_radians = math.radians(angle_in_degrees)
sin = math.sin(angle_in_radians)
print(f"Sine of {angle_in_degrees} degrees :{sin}")

""" Output 
Square root of 16:4.0
Factorial of 5:120
Sine of 1.5707963267948966 radians : 1.0
Sine of 90 degrees :1.0 """

#2.Create your 0wn module with 2 utility functions

def add_numbers(a,b):
     #Return the sum of two numbers 
     return a + b
def multiply_numbers(a,b):
     #Return the product of two numbers
     return a * b
    