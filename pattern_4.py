# W B W B W B W B 
# B W B W B W B W 
# W B W B W B W B 
# B W B W B W B W 
# W B W B W B W B 
# B W B W B W B W 
# W B W B W B W B 
# B W B W B W B W 
    
for i in range(1,9):
    for k in range(1,9):
        if (i + k) % 2 == 0:
            print("W ",end="")
        else:
            print("B ",end="")
    print()