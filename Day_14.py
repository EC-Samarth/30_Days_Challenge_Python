#Day_14 <Built in functions >
#1.use of map , filter , reduce 

#Map
numbers = [ 1,2,3,4,5]
squared_numbers = list(map(lambda x:x**2 , numbers))
print(squared_numbers)
""" Output 
[1, 4, 9, 16, 25]"""

#filter 
even_numbers = list(filter(lambda x:x%2 ,numbers))
print(even_numbers)
""" Output
[1, 3, 5] """

#reduce
from functools import  reduce
sum_of_numbers = reduce(lambda x,y : x+y ,numbers)
print(sum_of_numbers) #Output: 15

#2.use zip and enumarte 

#Zip
names = ['Sam','Ram','Ros']
ages= [20 ,21,23]
for name,age in zip(names,ages):
    print(f"{name}:{age}")

""" Output 
Sam:20
Ram:21
Ros:23 """

#Enumerate 
fruits =['apple','banana','cherry']
for index,fruit in enumerate(fruits):
    print(f"{index}:{fruit}")
""" Output 
Sam:20
Ram:21
Ros:23 """

#Enumerate with start index 
for index, fruit in enumerate(fruits,start=1):
    print(f"{index}:{fruit}")
""" Output 
1:apple
2:banana
3:cherry """

#3.use any and all functions

#Any
numbers=[1,2,3,4,5]
has_even = any(num%2 ==0 for num in numbers)
print(has_even) #Output:True

#All 
numbers = [2,4,6,8,10]
all_even = all(num%2 ==0 for num in numbers)
print(all_even) #Output:True

#Example with Strings
words = ["hello","world","python"]
has_long_word = any(len(word) > 5 for word in words)
print(has_long_word) #Output:True 

all_long_words = all(len(word) < 3 for word in words)
print(all_long_words) #Output:False