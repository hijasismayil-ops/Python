# # sort this list to ascending order?

a = [10, -1, 1000, -999, 0, 89, 67, 32, 3278]


for i in range(len(a)):
    for j in range(len(a)):
        if a[i] < a[j]:
            a[i], a[j] = a[j], a[i]

print(a)
