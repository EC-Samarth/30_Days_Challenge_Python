#Day_19<: Magic/Dunder Methods>

#1.- Implement __str__, __repr__, __add__, __len__
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        # Used when you print the object
        return f"'{self.title}' by {self.author}"

    def __repr__(self):
        # Used for debugging or inspecting the object
        return f"Book(title={self.title!r}, author={self.author!r}, pages={self.pages})"

    def __add__(self, other):
        # Add pages of two Book objects
        if isinstance(other, Book):
            return self.pages + other.pages
        return NotImplemented

    def __len__(self):
        # Return number of pages
        return self.pages


# Creating book objects
book1 = Book("Harry Potter", "J.K. Rowling", 300)
book2 = Book("Percy Jackson", "Rick Riordan", 250)

# Demonstrating __str__
print(book1)  # Output: 'Harry Potter' by J.K. Rowling

# Demonstrating __repr__
print(repr(book2))  # Output: Book(title='Percy Jackson', author='Rick Riordan', pages=250)

# Demonstrating __add__
total_pages = book1 + book2
print("Total Pages:", total_pages)  # Output: Total Pages: 550

# Demonstrating __len__
print("Length of book1:", len(book1))  # Output: Length of book1: 300




#2.- Customize behavior of your class objects


#Let's create a Vector class and customize its behavior using special methods:
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        else:
            raise TypeError("Can only add Vector instances")

    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        else:
            raise TypeError("Can only subtract Vector instances")

    def __eq__(self, other):
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        else:
            return False

# Example usage:
v1 = Vector(2, 3)
v2 = Vector(4, 5)

print(v1)  # Output: (2, 3)
print(repr(v1))  # Output: Vector(2, 3)

v3 = v1 + v2
print(v3)  # Output: (6, 8)

v4 = v1 - v2
print(v4)  # Output: (-2, -2)

print(v1 == v2)  # Output: False
print(v1 == Vector(2, 3))  # Output: True
