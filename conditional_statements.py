# if

# age = int(input("Enter younr age:"))

# if age > 18 :
#     print("eligible to vote")
# else:
#     print("not eligible")

# elif
# smark = 30
# if smark > 90:
#     print("A")
# elif smark > 80:
#     print("B")
# elif smark > 70:
#     print("C")
# elif smark > 60:
#     print("D")
# else:
#     print("fail")


# logical operators

# or
# and
# not

# or
# a = 18
# b = 1
# if (a > 10) or (b == 5) or (b % 2 == 0):
#     print("ok")

# and
# a = 7
# if a == 7 and a % 2 == 0:
#     print("yes")

# not
# a = 17
# if not a > 15:
#     print("yes")

# control statements -- loops

# while
# for

# while condition
# code to be executed

# i = 1

# while i < 10:
#     print(i)
#     i = i + 1

# sum

# i = 1
# sum = 0

# while i <= 10:
#     sum = sum + i
#     i = i + 1
# print(sum)


# num = 15432
# sum = 0

# while num > 0:
#     sum = sum + (num % 10)
#     num = num // 10

# print(sum)


# for loop

# for i in range(start,stop,step)

# for i in range(1,10,2):
#     print(i)

# sum of first 10 numbers

# sum = 0

# for i in range(1,11,1):
#     print(i)
#     sum = sum + i

# print(sum)

# break
# pass
# continue

# break

# for i in range(10):
#     if i == 5:
#         break
#     print(i)

# pass

# if 1< 0:
#     pass

# print("hii")

# continue

# for i in range(1,10):
#     if i == 1:
#         continue
#     print(i)
# print("mohan")

# nested loop

# pattern printing

# 1.

# *
# **
# ***
# ****
# *****

# for i in range(1,6):
#     for k in range(1,i+1):
#         print("*",end="")
#     print()

# 2.

# *****
# ****
# ***
# **
# *

# for i in range(5,0,-1):
#     for k in range(1,i+1):
#        print("*",end="")
#     print()

# 3.

#      *
#     * *
#    * * *
#   * * * *
#  * * * * *

# for i in range(1,6):
#     for j in range(6-i):
#         print(" ",end="")
#     for k in range(1,i+1):
#         print("* ",end="")
#     print()

# 4.

# W B W B W B W B
# B W B W B W B W
# W B W B W B W B
# B W B W B W B W
# W B W B W B W B
# B W B W B W B W
# W B W B W B W B
# B W B W B W B W

# for i in range(1,9):
#     for k in range(1,9):
#         if (i + k) % 2 == 0:
#             print("W ",end="")
#         else:
#             print("B ",end="")
#     print()

# for i in range(1,6):
#     for j in range(6-i):
#         print(" ",end="")
#     for k in range(1,i+1):
#         print("A ",end="")
#     print()

# list

# collection of data
# a = []
# numbers = [1,2,3,4,5,6,7,8,9,10]
# print(numbers)
# print(type(numbers))
# 1. any data of any type

# a = [1,2,3,4,1,1,1,2,"mohan",True,[11,12,13]]

# 2. orderd

# a = [1,2,3]
# b = [3,2,1]

# 2. indexed

# start at 0

# a = [11,12,13,14,15,16]
# print(a[2])
# list of index 2
# print(a[3])
# print(a[3:6])
# print(a[:6])
# print(a[::3])
# print(a[::-1])

# a = "mohandasgandhiji"
# [start:stop:step]

# print(a[1:14:2])
# print(a[::-1])

# mutable -- changable

# a = [11,12,13,14,15]
# a[0] = "mohan"
# print(a)
# string is not mutable
# a = "mohan"
# a[0] = "1"
# print(a)

# dynamic

# add --> grow
# remove --> shrink

# a = [11,12,13,14,15,16,17,18,19,20]
# a[2:3] = ["k","hi","heyyy"]

# print(a)

# inbuild methods

# add

# append

# a = [11,12,13,14,15]
# a.append(300)

# print(a)

# extend(indexed iterable)

# a = [1,2,3,4,5]
# a.extend("mohan")

# print(a)

# insert(index,value)

# a = [11,12,13,14,15]

# a.insert(0,2026)

# print(a)

# remove(element)
# .pop()
# pop(index)
# a = [11,12,13,14,15]
# a.clear()
# a.remove()
# a.pop()
# a.pop(0)
# print(a)

# tuple
# collection of data
# t1 = [11,12,13,14,15]
# t1[0] = "mohan"

# any elements any size
# orderd
# indexed
# immutable

# name = "mohan"
# a = [11,12,13,14,15]
# b = (11,12,13,14,15)

# for i in name:
#     print(i)

# for i in b:
#     print(i)

# list of index

# len(name)

# for i in range(len(name)):
#     print(i,name[i])

# a = [11,12,13,14,15]
# len(a)

# for i in range(len(a)):
#     print(i,a[i])

# in membership operator
# a = "hijas"
# if "h" in a:
#     print("yes")

# string formatting
# name = "mohan"
# age = 26
# rating = 4.5
# z = f"my name is {name} and my age is {age} and my rating is {rating}"
# print(z)

# input a string print vowels and their index

# string = input("Enter a string: ")
# for i in range(len(string)):
#     if string[i] == 'a' or string[i] == 'e' or string[i] == 'i' or string[i] == 'o' or string[i] == 'u':
#         print(f"Vowel: {string[i]} at index: {i}")

# string = input("Enter a string: ")
# vowels = "aeiouAEIOU"
# for index in range(len(string)):
#     if string[index] in vowels:
#         print(f"Vowel: {string[index]} at index: {index}")

# create a list of first 100 numbers?
# li = []

# for i in range(1, 101):
#     li.append(i)
# print(li)

# create a list of even numbers and odd numbers from 1 to 100?
# oli = []
# eli = []

# for i in range (1,101):
#     if i % 2 == 0:
#         eli.append(i)
#     else:
#         oli.append(i)
# print("Even numbers:",eli)
# print("Odd numbers:",oli)

# check if the numbers are postive or negative or zero from given list?
# z = [0,-2,-82,1,4,5,-199,-6]

# for i in z:
#     if i>0:
#         print(i,"is positive")
#     elif i<0:
#         print(i,"is negative")
#     else:
#         print(i,"is zero")

# find the duplicate and remove it print non-duplicate numbers from the given list?
# data = [1,2,3,4,5,3,4,1,2,3,6,5,4,2,7,8,3,2,1]
# op = []
# for i in data:
#     if i not in op:
#         op.append(i)
# print(op)

# find the largest and smallest number in this list?
# a = [10,-1,1000,-999,0,89,67,32,3278]
# lg = 0
# sm = 0

# for i in a:
#     if i > lg:
#         lg = i
#     if i < sm:
#         sm = i
# print(lg)
# print(sm)

# # sort this list to ascending order?
# a = [10,-1,1000,-999,0,89,67,32,3278]


# for i in range(len(a)):
#     for j in range(len(a)):
#         if a[i] < a[j]:
#             a[i],a[j] = a[j],a[i]

# print(a)
