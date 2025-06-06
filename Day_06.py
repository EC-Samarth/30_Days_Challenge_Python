#Day_o6 <Loops(for and while)>

#1.Sum of first n natural number
n = int(input("Enter the number :"))
i = 1 
sum = 0 
while(i<=n):
    sum = sum + i
    i = i + 1
print(sum)

s = 0
for i in range (1,n+1):
    s = s + i
print(s)

""" Output 
Enter the number :6
21
21 """


#2.Print multiplication table
a = int(input("Enter the number :"))
for i in range (1,11):
    print(f"{a} X {i} = {a*i}") 

""" Output
Enter the number :5
5 X 1 = 5
5 X 2 = 10
5 X 3 = 15
5 X 4 = 20
5 X 5 = 25
5 X 6 = 30
5 X 7 = 35
5 X 8 = 40
5 X 9 = 45
5 X 10 = 50 """

#3.number is prime or not 
b = int(input("Enter the number :"))
if b == 1:
    print("It is a not a prime number")
if b>1:
    for i in range (2,b):
        if b%i==0:
            print("It is not a prime Number ")
            break
    else:
        print("It is a prime Number ")

""" Output 
--Enter the number :11
It is a prime Number
--Enter the number :9
It is not a prime Number  """


#4.calculate the factorial of number 
c = int(input("Enter the number :"))
product = 1
for i in range(1,c+1):
    product = product * i 
print(f"the factorial {c} is {product}")

""" Output
Enter the number :5
the factorial 5 is 120 """

#5.check whether a number is armstrong number or not
num=int(input("Enter the number :"))
summ=0
temp=num
while temp >0: 
    digit = temp % 10 #get the last digit of the number 
    summ += digit **len(str(num)) #raise the digit t0 the power of the number of digits and add it to the sum
    temp //= 10  #remove the last digit from the number
if num ==summ:  #if the original number is equal to the sum then it an armstrong number
    print(num,"is an Armstrong number ")
else:
    print(num,"is not an Armstrong Number")

""" output 
Enter the number :371
371 is am Armstrong number  
"""