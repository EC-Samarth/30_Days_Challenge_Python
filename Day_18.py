#Day_18<Class and static method>
"""Class Methods vs Static Methods
Class Methods
- Definition: A method that belongs to a class rather than an instance.
- Decorator: @classmethod
- First parameter: cls (a reference to the class)
- Use case: When you need to access or modify class attributes, or create alternative constructors.

Static Methods
- Definition: A method that belongs to a class, but doesn't depend on the class or instance state.
- Decorator: @staticmethod
- No implicit first parameter: No self or cls parameter
- Use case: When you need a utility function that belongs to the class, but doesn't depend on the class or instance state."""

#1.- Implement both in a class with examples

class Student:
    school_name = "ABC High School"

    def __init__ (self,name,age):
        self.name = name
        self.age = age 

    @classmethod
    def get_school_name(cls):
        return cls.school_name
        
    @staticmethod
    def is_valid_age(age):
        return age >= 18

#Example usage 

print(Student.get_school_name()) # Output : ABC High School

print(Student.is_valid_age(20))  # Output: True
print(Student.is_valid_age(15))  # Output: False

#2.Use @classmethod and @staticmethod
class MathOperations:
    @classmethod
    def add(cls, a, b):
        print(f"Using class {cls.__name__}")
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b

# Example usage:
print(MathOperations.add(2, 3))
# Output: Using class MathOperations, 5

print(MathOperations.multiply(4, 5))
# Output: 20

        