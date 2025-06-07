#Day_07 <Lists>

#1.Find the max and min of the list
numbers =[12,44,45,65,78,34]
max_num = max(numbers)
min_num = min(numbers)
print("Max :",max_num)
print("Min :",min_num)

""" Output 
Max : 78
Min : 12 """

#2.remove the duplicate from the list 
my_list = [1,2,2,3,4,4,5,6,6]
unique_list =list(set(my_list)) #converting a list into set ,sets automatically remove duplicates & they allow only unique elements 
print(unique_list)

""" Output 
[1, 2, 3, 4, 5, 6] """

#3.List comprehension to get squares of even numbers
num = [1,2,3,4,5,6]
even_square = [x**2 for x in num if x%2 == 0 ]
print(even_square)

""" Output 
[4, 16, 36] """