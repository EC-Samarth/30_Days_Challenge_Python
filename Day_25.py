#Day_25<Comprehensions Deep Dive >

#1.Nested List Compreshension
"""A list comprehension inside another list comprehension, typically used for matrices, 
flattening lists, or multi-dimensional data."""

#Flatten 2D list
matrix = [[1, 2], [3, 4], [5, 6]]              # for row in matrix loops over sublists
flat = [item for row in matrix for item in row]#for item in row gets each number
print(flat)  # Output: [1, 2, 3, 4, 5, 6]

#Crate a multiplication table(2D Matrix)
table = [[i * j for j in range(1, 6)] for i in range(1, 6)]
print(table)


#2.Dictionat Comprehension with Conditions

#Square numbers,but only if numbers is even
squares = {x: x**2 for x in range(10) if x % 2 == 0}
print(squares)  # Output: {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

#Invert a dictionary ,but skip some values 
grades = {'A': 90, 'B': 80, 'C': 70, 'D': 60}
inverted = {v: k for k, v in grades.items() if v >= 70}
print(inverted)  # Output: {90: 'A', 80: 'B', 70: 'C'}
