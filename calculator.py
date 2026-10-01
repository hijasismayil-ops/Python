# # simple calculator using function?

# 1
# num1 = float(input("Enter a number"))
# num2 = float(input("Enter a number"))
# opr = str(input("Enter operator(+,-,*,/)"))


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

# 2
def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def div(a, b):
    return a / b


def mul(a, b):
    return a * b


def main():
    print("Welcome to simple calculator!!!")
    while True:
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter a number: "))
        opr = int(input("Enter operator\n1.Add\n2.Sub\n3.Mul\n4.Div\n5.Exit\n"))
        if opr == 1:
            print(add(num1, num2))
        elif opr == 2:
            print(sub(num1, num2))
        elif opr == 3:
            print(mul(num1, num2))
        elif opr == 4:
            print(div(num1, num2))
        elif opr == 5:
            break
        else:
            print("Invalid Choice")


main()
