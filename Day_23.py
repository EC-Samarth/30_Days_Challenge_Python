#Day_23 <Decorators>

#1.Basic Decorator

def greet_decorator(func):
    def wrapper():
        print("Hello")
        func()
        print("Good Bye")
    return wrapper()

@greet_decorator
def say_name():
    print("My name is Sam")

say_name

""" Output 
Hello
My name is Sam
Good Bye """

#2.Create a logging decorator
import functools

def logger(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOG] Called {func.__name__} with args={args} kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"[LOG] {func.__name__} returned {result}")
        return result
    return wrapper

@logger
def greet(name):
    return f"Hello, {name}!"


#3.Timer decorator to measure execution time
import time
import functools

def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"[TIMER] {func.__name__} took {(end - start):.6f} seconds")
        return result
    return wrapper

@timer
def slow_task():
    time.sleep(2)
    return "Finished!"
