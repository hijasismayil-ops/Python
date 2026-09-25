# create a list of even numbers and odd numbers from 1 to 100?

oli = []
eli = []

for i in range (1,101):
    if i % 2 == 0:
        eli.append(i)
    else:
        oli.append(i)
print("Even numbers:",eli)
print("Odd numbers:",oli)