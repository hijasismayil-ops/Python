def lemonadeChange(bills):
    five = 0
    ten = 0
    twenty = 0
    flag = True
    for bill in bills:
        if bill == 5:
            five += 1
        elif bill == 10:
            if five:
                five -= 1
                ten += 1
            else:
                flag = False
                break
        else:
            bill == 20
            if five >= 3:
                five -= 3
                twenty += 1
            elif ten >= 1 and five >= 1:
                ten -= 1
                five -= 1
                twenty += 1
            else:
                flag = False
                break
    if flag == True:
        print("True")
    else:
        print("False")


bills = [5, 5, 5, 10, 20]

lemonadeChange(bills)
