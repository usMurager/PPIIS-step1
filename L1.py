## Intro
# print("Hello World")

## User Input
# username = input("Enter username: ")
# print("Username is: " + username)

## Comments and This is comment

## Variables
# x = 5
# y = "John"
# print(x)
# print(y)

# x = 4       # x is of type int
# x = "Sally" # x is now of type str
# print(x)

# x = str(3)
# y = int(3)
# z = float(3)

# print(x)
# print(y)
# print(z)

## Data types

# x = True
# print(type(x))

## NUmbers 
# x = 1
# y = 2.8
# z = 1j

# print(type(x))
# print(type(y))
# print(type(z))

## Casting
# x = int(1)   # x will be 1
# y = int(2.8) # y will be 2
# z = int("3") # z will be 3

# x = float(1)     # x will be 1.0
# y = float(2.8)   # y will be 2.8
# z = float("3")   # z will be 3.0
# w = float("4.2") # w will be 4.2

# x = str("s1") # x will be 's1'
# y = str(2)    # y will be '2'
# z = str(3.0)  # z will be '3.0'

# print(x)
# print(y)
# print(z)
# print(w)

## Strings
# print("Hello")
# print("Hello")

# a = "hello"
# print(a)
# a = """Lorem ipsum dolor sit amet,
# consectetur adipiscing elit,
# sed do eiusmod tempor incididunt
# ut labore et dolore magna aliqua."""
# print(a)

# a = "Hello, World!"
# print(a[2])

# for x in "banana":
#   print(x)

# a = "Hello, World!"
# print(len(a))

# txt = "The best things in life are free!"
# print("free" in txt)

# txt = "The best things in life are free!"
# if "free" in txt:
#   print("Yes, 'free' is present.")

# txt = "The best things in life are free!"
# if "expensive" not in txt:
#   print("Yes, 'expensive' is NOT present.")

## String formating 
# price = 49
# txt = "The price is {} dollars"
# print(txt.format(price))

# price = 49
# txt = "The price is {:.2f} dollars"
# print(txt.format(price))

# quantity = 3
# itemno = 567
# price = 49
# myorder = "I want {} pieces of item number {} for {:.2f} dollars."
# print(myorder.format(quantity, itemno, price))

# quantity = 3
# itemno = 567
# price = 49
# myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
# print(myorder.format(quantity, itemno, price))

# age = 36
# name = "John"
# txt = "His name is {1}. {1} is {0} years old."
# print(txt.format(age, name))

# myorder = "I have a {carname}, it is a {model}."
# print(myorder.format(carname = "Ford", model = "Mustang"))

## Booleans
# print(10 > 9)
# print(10 == 9)
# print(10 < 9)

# a = 200
# b = 300

# if b > a:
#   print("b is greater than a")
# else:
#   print("b is not greater than a")

# print(bool("Hello"))
# print(bool(15))

# x = "Hello"
# y = 15

# print(bool(x))
# print(bool(y))

# print(bool("abc"))
# print(bool(123))
# print(bool(["apple", "cherry", "banana"]))

## Operators
# print(10 + 5)

## If... Else

# a = 33
# b = 200
# if b > a:
#   print("b is greater than a")

# if a > b: print("a is greater than b")

# a = 2
# b = 330
# print("A") if a > b else print("B")

## While Loops
# i = 1
# while i <= 6:
#   print(i)
#   i += 1

# i = 1
# while i < 6:
#   print(i)
#   if i == 3:
#     break
#   i += 1

# i = 0
# while i < 6:
#   i += 1
#   if i == 3:
#     continue
#   print(i)

# i = 1
# while i < 6:
#   print(i)
#   i += 1
# else:
#   print("i is no longer less than 6")

## For Loops
# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   print(x)

# for x in "banana":
#   print(x)

# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   print(x)
#   if x == "banana":
#     break

# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   if x == "banana":
#     break
#   print(x)

# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   if x == "banana":
#     continue
#   print(x)

## Arrays

# cars = ["Ford", "Volvo", "BMW"]
# # x = cars[0]
# # x = len(cars)
# # cars[0] = "Toyota"
# # for x in cars:
# # cars.pop(1)
# # cars.append("Honda")
# cars.remove("Volvo")
# print(cars)


