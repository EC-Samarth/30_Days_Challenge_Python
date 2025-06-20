#Day_20 < Encapsulation >

#1.Use private variables in a class

class Student:
    def __init__(self,name,marks):
        self.__name = name   #private attribute 
        self.__marks = marks #private attribute

    def set_name(self,name):
        self.__name = name 

    def get_name(self):
        return self.__name

    def set_marks(self,marks):
        self.__marks = marks

    def get_marks(self):
        return self.__marks
    
#Using the class 

s = Student("Samarth",88)
print("Name :",s.get_name())
print("Marks :",s.get_marks())

""" Output 
Name : Samarth
Marks : 88 """

s.set_name("Gopal")
s.set_marks(95)
print("Updated Name :",s.get_name())
print("Updated Marks:",s.get_marks())

""" Output 
Updated Name : Gopal
Updated Marks: 95 """

#2.- Provide getters and setters
class Car:
    def __init__(self):
        self.__speed = 0
        self.__fuel = 100

    def set_speed(self,speed):
        if 0 <= speed <= 200:
            self.__speed = speed
        else:
            print("Invalid Speed ")

    def set_fuel(self,fuel):
        if 0 <= fuel <= 100:
            self.__fuel = fuel
        else:
            print("Invlaid Speed")

    def get_speed(self):
        return self.__speed
    
    def get_fuel(self):
        return self.__fuel
    
#Example Usage 
c = Car()
c.set_speed(150)
c.set_fuel(80)
print("Speed :",c.get_speed())
print("Fuel :", c.get_fuel())

""" Output 
Speed : 150
Fuel : 80 """

#3.Bank account 
import datetime

class BankAccount:
    def __init__(self, account_holder, account_number, initial_balance=0):
        self.__account_holder = account_holder
        self.__account_number = account_number
        self.__balance = initial_balance
        self.__transaction_history = []

    def __record_transaction(self, transaction_type, amount):
        # Internal helper method (encapsulated)
        time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.__transaction_history.append({
            "type": transaction_type,
            "amount": amount,
            "time": time,
            "balance_after": self.__balance
        })

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.__record_transaction("Deposit", amount)
            print(f"₹{amount} deposited successfully.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            self.__record_transaction("Withdraw", amount)
            print(f"₹{amount} withdrawn successfully.")
        else:
            print("Insufficient balance or invalid amount.")

    def get_balance(self):
        return self.__balance

    def get_account_info(self):
        return {
            "Account Holder": self.__account_holder,
            "Account Number": self.__account_number,
            "Current Balance": self.__balance
        }

    def get_transaction_history(self):
        return self.__transaction_history

    def change_account_holder(self, new_name):
        if new_name:
            self.__account_holder = new_name
            print("Account holder name updated.")
        else:
            print("Invalid name.")

# -----------------------------------------------------
# 🌟 Example Usage:

acc = BankAccount("Aman Verma", "AC123456789", 1000)

acc.deposit(2000)
acc.withdraw(500)
acc.change_account_holder("Amit Verma")

print("\n--- Account Info ---")
for key, value in acc.get_account_info().items():
    print(f"{key}: {value}")

print("\n--- Transaction History ---")
for t in acc.get_transaction_history():
    print(f"{t['time']} - {t['type']} ₹{t['amount']} → Balance: ₹{t['balance_after']}")