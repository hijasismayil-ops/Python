# find the duplicate and remove it print non-duplicate numbers from the given list?

data = [1, 2, 3, 4, 5, 3, 4, 1, 2, 3, 6, 5, 4, 2, 7, 8, 3, 2, 1]
op = []
for i in data:
    if i not in op:
        op.append(i)
print(op)
