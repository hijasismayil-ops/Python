# reverse the keys and values of a dictionary?

# input : {1: "a", "b" : 2, "c": 3}

# output : {"a": 1, 2: "b", 3: "c"}

dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {}

for i in dict1:
    dict2[dict1[i]] = i

print(dict2)
