# functions

# structural programing
# functional programing
# modular programing
# object oriented programing
# procedural programing

# functions

# block of code which is executed whhen it is called
# reuseble

# def functionname():
#   code to be executed

# def hello():
#     print("hello my is hijas")


# hello() calling the function

# hello()

# arguments

# def hello(name):
#     print(name)


# hello("Hijas")

# 2 types
# positional arguments


# def add(a, b):
#     print(a + b)


# add(5, 5)

# keyword arguments


# def mul(x, y, z):
#     pass


# mul(y=1, x=5, z=3)

# factorial of number using function?


# def factorial(num):
#     fact = 1
#     for i in range(1, num+1):
#         fact *= i
#     print(fact)


# factorial(4)

# a = a + 1 -- # a += 1 both are same


# write a function to check if a string is unique or not?

# 1
# def is_unique(str):
#     uniq = True
#     for i in range(0, len(str)):
#         for k in range(i + 1, len(str)):
#             if str[i] == str[k]:
#                 uniq = False
#                 break
#     if uniq:
#         print("True")
#     else:
#         print("False")


# is_unique("mohan")

# def add(a, b):
#     return a + b


# print(add(5, 8))

# def add(a, b):
#     return 30, 40, 50, 60


# print(add(5, 8))

# the functions return multiple values -- tuple

# simple calculator using function?

# num1 = float(input("Enter a number:- "))
# num2 = float(input("Enter a number:- "))
# opr = str(input("Enter operator(+,-,*,/): "))


# def add(a, b):
#     return a + b


# def sub(a, b):
#     return a - b


# def div(a, b):
#     return a / b


# def mul(a, b):
#     return a * b


# if opr == "+":
#     print(add(num1, num2))
# elif opr == "-":
#     print(sub(num1, num2))
# elif opr == "*":
#     print(mul(num1, num2))
# elif opr == "/":
#     print(div(num1, num2))
# else:
#     print("Enter a valid operator!!")

# lambda function

# lambda arguments : expression
# def sumz(a, b):
#     return a + b


# print(sumz(5, 6))
# b = lambda x,y : x + y

# print(b(7,8))

# product of 3 number?

# prd = lambda a, b, c : a * b * c
# print(prd(2,4,5))

# are of a triangle?

# area = lambda a, b: 1/2 * a * b

# print(area(8, 6))

# perimeter of a circle?

# rad = lambda c : 2 * 3.14 * c
# print(rad(5))

# full name of a person?

# fname = str(input("Enter first name: "))
# mname = str(input("Enter middle name: "))
# lname = str(input("Enter last name: "))

# fullname = lambda a,b,c : f"{a}{b}{c}"

# print(fullname(fname,mname,lname))

# square root of a number?

# num = int(input("Enter a Number: "))
# sqrt = lambda a : a ** .5
# print(sqrt(num))

# avarage of 5 numbers?
# avrg = lambda n1,n2,n3,n4,n5 : (n1 + n2 + n3 + n4 + n5) / 5
# print(avrg(5,5,55,5,5))

# check if a person is eligible to vote or not?

# vote = lambda age : "Eligible" if age >= 18  else "Not eligible"
# print(vote(21))

# recurtion

# def counttozero(n):
#     print(n)
#     if n == 0:
#         return 0
#     return counttozero(n - 1)


# counttozero(10)

# sum
# def counttozero(n):

#     if n == 0:
#         return 0
#     return n + counttozero(n - 1)


# print(counttozero(10))

# factorial


# def counttozero(n):
#     if n == 1:
#         return 1
#     return n * counttozero(n - 1)


# print(counttozero(5))

# check if a number is amstrong or not?
# 153

# 1 ** 3 + 5 ** 3 + 3 ** 3 == 153

# leet code 13th question -- home work

# scope

# area in which it is recognised

# name = "hijas"  # globally declared


# def myname():
#     # name = "ijx"
#     # print(name)

#     def nickname():  # local scope
#         # name = "santhy"
#         print(name)
#     nickname()


# myname()

# 1. local
# 2. enclose
# 3. global
# 4. build in

# x = 10


# def twotimes():
#     global x
#     x = x * 2
#     print(x)


# twotimes()
# print(x)

# args and kwargs

# def add(*args):  # recives as a tuple
#     sum = 0
#     for i in args:
#         sum += i
#     print(sum)


# add(4, 5, 6, 23, 3, 3, 4, 4, 4)

# def fullname(*args, **kwargs):  # receives as a dic
#     full = ""
#     for i in kwargs:
#         full = full + kwargs[i] + " "
#     print(full)


# fullname(fname="ijx", mname="hijas", lname="jobi", fifthname="satheesh")

# modules

# matrix addition

# a = [[2, 3],
#      [4, 5]]
# b = [[2, 1],
#      [3, 2]]

# c = [[0, 0],
#      [0, 0]]

# for i in range(len(a)):
#     for j in range(len(a)):
#         c[i][j] = a[i][j] + b[i][j]
# print(c)

# a = [[2, 3],
#      [4, 5]]
# b = [[2, 1],
#      [3, 2]]

# c = [[0, 0],
#      [0, 0]]

# for i in range(len(a)):
#     for j in range(len(a)):
