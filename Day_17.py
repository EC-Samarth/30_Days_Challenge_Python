#Day_17 < Polymorphism >
#1.Implement polymorphism using duck typing
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

class Human:
    def speak(self):
        return "Hello!"

# Polymorphic function using duck typing
def make_it_speak(entity):
    print(entity.speak())

# Create objects
dog = Dog()
cat = Cat()
person = Human()

# Call function with different types of objects
make_it_speak(dog)    # Output: Woof!
make_it_speak(cat)    # Output: Meow!
make_it_speak(person) # Output: Hello!

#2.operator Overloading
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Overloading the '+' operator
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    # For printing the object
    def __str__(self):
        return f"({self.x}, {self.y})"

# Create two Point objects
p1 = Point(2, 3)
p2 = Point(4, 1)

# Add them using overloaded '+' operator
p3 = p1 + p2

print(p3)  # Output: (6, 4)

