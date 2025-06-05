#Day_05 <Conditional Statment>

#1.Check if number is even or odd
a = int(input("Enter any number :"))
if (a/2==0 ):
    print("It is an even Number")
else:
    print("It is an odd number")

""" Output 
Enter any number :45
It is an odd number """

#2.Largest amon three numbers
a = int(input("Enter the first number : "))
b = int(input("Rnter the second number :"))
c = int(input("Enter the third number :"))

if (a>b & a>c):
    print("a is the largest number")
elif (b>a & b>c):
    print("b is thelargest number")
elif(c>a & c>b):
    print("c is largest number ")

""" Output 
Enter the first number : 3
Rnter the second number :4
Enter the third number :5
c is largest number  """

#3.Grade calculator based on marks
maths = int(input("Enter the marks of maths :"))
phy = int(input("Enter the marks of physics :"))
chem = int(input("Enter the marks of chemistry :"))

total = maths + phy + chem
per = total/3 

if(maths>33 & phy<33 & chem>33):
    print("pass in every subject")
    if (per>=90 & per<=100):
        print("A+ Grade")
    elif(per>=80 & per<90):
        print("A Grade")
    elif(per>=70 & per<80):
        print("B Grade")
    elif(per>=60 & per<70):
        print("C Grade")
    elif(per>=50 & per<60):
        print("D Grade")
    elif(per>=33 & per<50):
        print("F Grade")
    else:
        print("Fail,Better luck next time")
else:
    print("You failed in subject")

print("marks of maths :" +str(maths)+", marks of physics :"+str(phy)+" ,marks of Chemistry :" +str(chem))
print("percentage :",per)

""" Output
Enter the marks of maths :70
Enter the marks of physics : 30
Enter the marks of chemistry :55
You failed in subject
marks of maths :70, marks of physics :30 ,marks of Chemistry :55
percentage : 51.666666666666664"""