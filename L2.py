##Lists
# 1 fruits = ["apple", "banana", "cherry"]
# print(fruits[1])

# 2 fruits = ["apple", "banana", "cherry"]
# fruits[0] = "kiwi"

# 3 fruits = ["apple", "banana", "cherry"]
# fruits.append("orange")

# 4 fruits = ["apple", "banana", "cherry"]
# c "lemon")

# 5 fruits = ["apple", "banana", "cherry"]
# fruits.remove("banana")

# 6 fruits = ["apple", "banana", "cherry"]
# print(fruits[-1])

# 7 fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(fruits[2:5])

# 8 fruits = ["apple", "banana", "cherry"]
# print(len(fruits))

## Tuples
# 1 fruits = ("apple", "banana", "cherry")
# print(fruits[0])

# 2 fruits = ("apple", "banana", "cherry")
# print(len(fruits))

# 3 fruits = ("apple", "banana", "cherry")
# print(fruits[-1])

# 4 fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(fruits[2:5])

## Sets

# 1 fruits = {"apple", "banana", "cherry"}
# if "apple" in fruits:
#   print("Yes, apple is a fruit!")

# 2 fruits = {"apple", "banana", "cherry"}
# fruits.add("orange")

# 3 fruits = {"apple", "banana", "cherry"}
# more_fruits = ["orange", "mango", "grapes"]
# fruits.update(more_fruits)

# 4 fruits = {"apple", "banana", "cherry"}
# fruits.remove("banana")

# 5 fruits = {"apple", "banana", "cherry"}
# fruits.discard("banana")

## Dictionaries

# 1 car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964}
# print(car.get("model"))

# 2 car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964 }
# car["year"] = 2020
# print(car)

# 3 car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964 }
# car["color"] = "red"
# print(car)

# 4 car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964 }
# car.pop("model")

# 5 car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964 }
# car.clear()

## Functions

# 1 def my_function():
#   print("Hello from a function")

# 2 def my_function():
#   print("Hello from a function")
# my_function()

# 3 def my_function(fname, lname):
#   print(fname)

# 4 def my_function(x):
#     return x + 5

# 5 def my_function(*kids):
#     print("The youngest child is " + kids[2])

# 6 def my_function(**kid):
#     print("His last name is " + kid["lname"])

## Lambda

# 1 x = lambda a : a

## Classes and Objects

# 1 class MyClass:
#     x = 5

# 2 class MyClass:
#     x = 5
# p1 = MyClass()

# 3 class MyClass:
#     x = 5
# p1 = MyClass()
# print(p1.x)

# 4 class Person:
#   def __init__ (self, name, age):
#     self.name = name
#     self.age = age

## Inheritance

# 1 class Student(Person):

# 2 class Person:
#     def __init__(self, fname):
#       self.firstname = fname

#     def printname(self):
#       print(self.firstname)

#     class Student(Person):
#       pass

# x = Student("Mike")
# x.printname()