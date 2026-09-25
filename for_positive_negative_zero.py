# check if the numbers are postive or negative or zero from given list?

z = [0, -2, -82, 1, 4, 5, -199, -6]

for i in z:
    if i > 0:
        print(i, "is positive")
    elif i < 0:
        print(i, "is negative")
    else:
        print(i, "is zero")
