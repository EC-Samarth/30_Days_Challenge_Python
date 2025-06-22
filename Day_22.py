#Day 22:<List vs Generator>

""" What is a Generator?
A generator is a special type of iterator that yields items one by one using the yield keyword.

It does not store all values in memory — only one value at a time is generated on the fly.

"""
#1.Create a generator function

#Generate a function to yeild th square of the n numbers
def generate_squares(n):
    for i in range(n):
        yield i * i

# Using the generator
gen = generate_squares(5)
for value in gen:
    print(value)



#2. Compare memory usage with list
import sys

# List comprehension
list_squares = [i * i for i in range(1000)]
print("List memory usage:", sys.getsizeof(list_squares), "bytes")

# Generator expression
gen_squares = (i * i for i in range(1000))
print("Generator memory usage:", sys.getsizeof(gen_squares), "bytes")


"""
0
1
4
9
16
List memory usage: 8856 bytes
Generator memory usage: 200 bytes
"""