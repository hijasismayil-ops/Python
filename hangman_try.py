from movie_list import movies
import random


# selected_movie = random.choice(movies)
selected_movie = "AVATAR"
hidden_movie = ""
upd_movie = ""
player_guess = ""
chances = 5

for i in selected_movie:
    if i == " ":
        hidden_movie = hidden_movie + " "
    else:
        hidden_movie = hidden_movie + "_ "

print(selected_movie)
print(hidden_movie)

while upd_movie != selected_movie:
    player_guess = input("Guess a character or the movie name: ").upper()
    if player_guess in selected_movie.upper():
        for i in selected_movie:
            if player_guess == i:
                upd_movie = upd_movie + i
            else:
                if i == " ":
                    upd_movie = upd_movie + " "
                else:
                    upd_movie = upd_movie + "_ "
        print(upd_movie)
    else:
        print("Wrong guss!!")
