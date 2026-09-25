# check if a number is prime or not?

# 1.
num = int(input("Enter a number:"))
is_prime = True
if num == 1:
    print("not prime")
else:
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
if is_prime == True:
    print("prime")
else:
    print("not prime")

# 2. 
num = int(input("Enter a number:"))
is_prime = True
if num == 1:
    print("not prime")
else:
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            print("not prime")
            break
    else:
        print("prime")