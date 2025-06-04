# Day_04 <Strings>

#1. Reverse a string 
string = input("Enter any string :")
print(''.join(reversed(string)))     #first type 
print(string[::-1])                  #Second type

""" Output
Enter any string :Hello World
dlroW olleH
dlroW olleH """

#2.Count the vowel in the string
str = input("Enter the String : ")
vowels ="aeiouAEIOU"
count = len([char for char in str if char in vowels])
print(count )
print("Yes,Their is a vowel in the string" if count!=0 else "No, Their is no vowel in the string")

""" Output
Enter the String : hello
2
Yes,Their is a vowel in the string """


#3.check the string is palidrome
str = input("Enter the string : ")
print(str == str[::-1])                #this is not for case sensitive 
print(str.lower() == str.lower()[::-1]) #this is case sensitive
"""this code checks if the string is equal to its reverse .If they are equal ,the string is a palidrome"""

""" Output
Enter the string : Maam
False
True 

Enter the string : madam
True
True """