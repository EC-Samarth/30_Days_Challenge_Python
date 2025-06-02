#Day 2 <Data types and Typecasting>

#1.Convert string into int and float 
a="34"
print (float(a))
print (int(a))


#2.Check the datatype using type()
s = 22.0
print (type(s))


#3.Round a float to 2 decimal places
num = 3.14159 
rounded_num = format(num,2)
print(rounded_num)  #Output:3.14

#4.Imlicit type casting 
a= 5           #int
b = 2.0        #float
result = a + b #result is float 
print(result)  #Output:7.0


#5.Explicit type casting
a = 5.5    #float
b = int(a) #explicit type casting in int 
print(b)   #Output :5
