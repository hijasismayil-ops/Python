import random

p1 = 0
p2 = 0

while True:
    op = ["head", "tail"]
    toss = random.choice(op)
    a = input("enter player one guess:")
    b = input("enter player two guess:")
    print(f"correct guess is {toss}")
    if a == toss:
        p1 += 1
        print("score of player 1:", p1)
        print("score of player 2:", p2)
    elif b == toss:
        p2 += 1
        print("score of player 1:", p1)
        print("score of player 2:", p2)
    if p1 == 5:
        print("player one  wins")
        break
    if p2 == 5:
        print("player one wins")
        break
