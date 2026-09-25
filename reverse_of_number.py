# reverse of a number?

num = 154
rev = 0

while num > 0:
    b = num % 10
    num = num // 10
    rev = rev * 10 + b
    
print(rev)