# modules
import random

# math
# random
# os
# sys
# time

# random

# randint
# choice

# print(random.randint(1, 10))
# fruits = ("apple", "orange", "mango", "grapes")

# print(random.choice(fruits))

# coin tos ?

# list = ["Heads", "Tails"]


# def coin():
#     guss = str(input("Take a guss (Heads or Tails):"))
#     tos = random.choice(list)
#     if guss == tos:
#         print(guss)
#         print("Your guss is correct")
#     else:
#         print("Wrong")


# coin()

# rock paper game

# ch = ["rock", "paper", "scissors"]
# guss = ""

# while guss not in ch:
#     guss = input("Chose one (rock,paper,scissors)").lower()

# com = random.choice(ch)

# if guss == com:
#     print("Tie")
# elif guss == "rock":
#     if com == "paper":
#         print(f'Computer chose {com} You Lose')
#     else:
#         print(f'Computer chose {com} You Win')
# elif guss == "paper":
#     if com == "scissors":
#         print(f'Computer chose {com} You Lose')
#     else:
#         print(f'Computer chose {com} You Win')

# elif guss == "scissors":
#     if com == "rock":
#         print(f'Computer chose {com} You Lose')
#     else:
#         print(f'Computer chose {com} You Win')

# file handeling
# exception handeling

# file1 = open("hello.txt", "r")
# print(file1.read())
# file1.close()

# file2 = open("bye.txt", "w")
# file2.write("i am hijas")
# file2.close()

# file3 = open("bye.txt", "a")
# for i in range(1, 100):
#     file3.write(f"i am hijas {i}\n")
# file3.close()

# with open("hello.txt", "r") as f:
#     print(f.read())

import os

# os.mkdir("django")
# os.rename("bye.txt", "byyeeee.txt")
# file_path = file's path
# os.remove(file's path)

# exceptions

# exceptions - events that affects the execution of our programs

# try:
#     a = int(input("Enter a number:"))
#     b = int(input("Enter a number:"))
#     print(a/b)
# except:
#     print("an error occured!!")

# print("mohan")

# multiple exception handeling

# try:
#     a = int(input("Enter a number"))
#     b = "5"
#     print(a/b)
# except ZeroDivisionError:
#     print("You can't divide a number by zero!!")
# except ValueError:
#     print("Check your value")
# except TypeError:
#     print("Check your type")
# finally:
#     print("This will always executed")


# raise

# class Age_error(Exception):
#     pass


# age = 14

# if age < 18:
#     raise Age_error("age should be greater than 18")

# time

import time

# print(time.time())

# print(time.ctime())  # epoch time

# start = time.time()
# for i in range(1, 6):
#     print(i)
#     time.sleep(1)  # for delaying the excution
# end = time.time()

# print("total time :", end - start)


def execution_time(fun):
    def wrapper(*args, **kwargs):
        start = time.time()
        fun(*args, **kwargs)
        end = time.time()
        print("total time :", end - start)
    return wrapper


@execution_time
def number(n):
    for i in range(1, n+1):
        print(i)
        time.sleep(1)


@execution_time
def add(a, b):
    a + b


add(5, 7)
number(10)
