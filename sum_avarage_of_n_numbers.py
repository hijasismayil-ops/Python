# sum and average of n numbers?

count = int(input("Enter count:"))
sum = 0
for i in range(0, count):
    num = int(input("Enter a number:"))
    sum = sum + num

print("Tottal sum:",sum)
print("Avarage:",sum/count)