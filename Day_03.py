#Day_03 <Operators and expression>

#1.Calculate the area of the circle 
import math 

radius = int(input("Enter the Radius of the circle "))
area = math.pi *(radius ** 2)
print(area)

""" Output
Enter the Radius of the circle 4
50.26548245743669 """

#2.Simple Interest calcualator

p = int(input("Enter the amount :"))
r = int(input("Enter the rate :"))
t = int(input("Enter the time in years :"))

SI = (p*r*t)/100
print("Simple Interest :",SI)

""" output

Enter the amount :15000
Enter the rate :3
Enter the time in years :2
simple Interest : 900.0 """

#3.Fahrenheit to celsius

f = int(input("Enter the temperature in Fahrenheit :"))
celcius = (f - 32)*5/9
print (celcius)

""" Output
Enter the temperature in Fahrenheit :200
93.33333333333333  """ 

#4.Calculate the discount in the amount
amount = int(input("Enter the Price :"))
discount_percentage = int(input("Enter the discount :"))
discount = amount *( discount_percentage/100)
discount_amount = amount - discount
print("On the original amount dicount of : " + str(discount) + " and the total amount after discount is :" + str(discount_amount))

""" Output 
Enter the Price :1000
Enter the discount :20
On the original amount dicount of : 200.0 and the total amount after discount is :800.0"""