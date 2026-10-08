# number gussing game
# computer generates a random number
# player gets 5-7 attemts
# give hints: too high / too low
# track score
import random

rand = random.randint(1, 100)
score = 0

print(rand)

for i in range(1, 8):
    guss = int(input("Guss a number:"))
    if rand == guss:
        if i == 1:
            score = 70
            print(
                f"Computer chose {rand} It's correct, You Win, your score is {score} yeeeeeeei!!!!")
            break
        else:
            score = 70 - (i * 10)
            print(
                f"Computer chose {rand} It's correct, You Win, your score is {score} yeeeeeeei!!!!")
            break

    elif rand > guss:
        print("hint: Your guss is too low")
    else:
        print("hint: Your guss is too high")

    if i == 7:
        print(
            f"You lose, attempt completed. The correct number is {rand}, your score is {score}")
