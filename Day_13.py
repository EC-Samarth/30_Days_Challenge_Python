#Day_13<Exception Handling >

#1.Handlingdivide by zero Error
def divide_numbers(a,b):
    try:
        result = a/b
        return result
    except ZeroDivisionError:
        print("Error : Division by zero is not allowed ")
        return None
    except TypeError:
        print("Error :Invalid input type .Both input must be numbers.")
        return None
    except Exception as e :
        print(f"An unexpected error occured :{e}")
        return None
    
#Example Usage 
print(divide_numbers(10,2)) 
print(divide_numbers(10,0))
print(divide_numbers(10,'a'))
 
""" Output 
5.0
Error : Division by zero is not allowed 
None
Error :Invalid input type .Both input must be numbers.
None """

class NegativeNumberError(Exception):
    pass


#2.Handle divide-by-zero error
try:
    a = int(input("Enter value of a : "))
    b = int(input("Enter value of b : "))
    divide = a/b
    print(divide)

except ZeroDivisionError:
    print("You can't divide a number with zero.")

""" Output 
Enter value of a : 6
Enter value of b : 0
You can't divide a number with zero. """

#3.Handle file not found error
try:
    with open("erf.txt","r") as file:
        c = file.read()
        print(c)

except FileNotFoundError:
    print("This file is not exist.")

""" Output 
This file is not exist. """

#4.Create a custom exception
def checkForNegative(x,y):
    if x<0 or y<0:
        raise NegativeNumberError("Negative number is not allowed.")
    else:
        print("The number is positive.")
        
try:
     a1 = int(input("Enter value of a1(non-negative) : "))
     b1 = int(input("Enter value of b1(non-negative) : "))
     checkForNegative(a1,b1)
     divide = a1/b1
     print(divide)

except NegativeNumberError as e:
    print(f"Error : {e}")

except ZeroDivisionError as e:
    print(f"Error : {e}")

""" Output 
Enter value of a1(non-negative) : 4
Enter value of b1(non-negative) : 5
The number is positive.
0.8 """

#5.Write a calculator that performs addition,substraction,multiplication,and division.
#                Handle invalid input using nested try blocks.
def calculator():
    try:
        n1 = int(input("Enter the value of n1 : "))
        n2 = int(input("Enter the value of n2 : "))
        operator = input("Enter the operator : ")
        try:
            if operator == '+':
                print(f"Addition : {n1+n2}")
            elif operator == '-':
                print(f"Substraction : {n1-n2}")
            elif operator == '*':
                print(f"Multiplication : {n1*n2}")
            elif operator == '/':
                print(f"Division : {n1/n2}")
        except ZeroDivisionError:
            print("You can't divide a number with zero.")

    except ValueError:
        print("Invalid input! Please enter a valid number")

    finally:
        print("Thank you for execution.")

calculator()

""" Output 
Enter the value of n1 : 4
Enter the value of n2 : 6
Enter the operator : +
Addition : 10
Thank you for execution.

Enter the value of n1 : 7
Enter the value of n2 : 8
Enter the operator : *
Multiplication : 56
Thank you for execution """
            


        
 


    