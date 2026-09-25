# find the largest and smallest number in this list?

a = [10, -1, 1000, -999, 0, 89, 67, 32, 3278]
lg = 0
sm = 0

for i in a:
    if i > lg:
        lg = i
    if i < sm:
        sm = i
print(lg)
print(sm)
