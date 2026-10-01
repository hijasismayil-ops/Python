# # check if a number is amstrong or not?
# # 153
# # 1 ** 3 + 5 ** 3 + 3 ** 3 == 153

# 1

# num = 153
# org = num
# total = 0
# count = 0

# temp = num

# while temp > 0:
#     temp = temp // 10
#     count += 1

# # print(count)

# while num > 0:
#     digit = num % 10
#     # print(digit)
#     total = total + (digit ** count)
#     num = num // 10

# if total == org:
#     print("Armstrong number")
# else:
#     print("Not an Armstrong number")

# 2


# def count(num):
#     count = 0
#     while num > 0:
#         count += 1
#         num = num // 10
#     return count


# def amstrong(num):
#     actual_no = num
#     sum = 0
#     while num > 0:
#         b = num % 10
#         c = count(actual_no)
#         sum = sum + (b ** c)
#         num = num // 10
#     if actual_no == sum:
#         print("True")
#     else:
#         print("False")


# amstrong(153)
