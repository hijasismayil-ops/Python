# # given a sentence, create a dictionary containing the frequency of eatch words.

# # input: "python is easy and python is powerful"

# # expected:
# # {
# #     "python": 2,
# #     "is": 2,
# #     "easy": 1,
# #     "and": 1,
# #     "powerful": 1
# # }

# 1.

# str = "python is easy and python is powerful"
# temp = ""
# words = []
# dict = {}

# for i in str:
#     if i != " ":
#         temp = temp + i
#     else:
#         words.append(temp)
#         # dict[temp] += 1
#         temp = ""

# words.append(temp)
# # dict[temp] += 1

# # print(words)

# for i in words:
#     if i in dict:
#         dict[i] += 1
#     else:
#         dict[i] = 1

# print(dict)

# 2.

# str = "python is easy and python is powerful"
# dict = {}
# words = str.split()


# for i in words:
#     if i in dict:
#         dict[i] += 1
#     else:
#         dict[i] = 1

# print(dict)
