from movie_list import movies
import random

selected_movie = random.choice(movies).upper()
hidden_movie = ""
upd_movie = ""
player_guess = ""
chances = 5
guessed_chars = []
print(selected_movie)

for i in selected_movie:
    if i == " ":
        hidden_movie = hidden_movie + "  "
    else:
        hidden_movie = hidden_movie + "_ "

print(hidden_movie)

while chances > 0 and upd_movie != selected_movie:
    player_guess = input(
        "Guess a character or the movie name: ").upper().strip()
    # The strip() is from chatgpt.

    if player_guess == selected_movie:
        upd_movie = selected_movie
        print("Correct! You guessed the movie!")
        break

    elif len(player_guess) == 1:
        if player_guess in guessed_chars:
            print("You already guessed that character!")
            continue

        guessed_chars.append(player_guess)

        if player_guess in selected_movie:
            print("Correct character!")

            upd_movie = ""
            for i in selected_movie:
                if i == " ":
                    upd_movie = upd_movie + "  "
                elif i in guessed_chars:
                    upd_movie = upd_movie + i + " "
                else:
                    upd_movie = upd_movie + "_ "
        else:
            chances -= 1
            print("Wrong guess!")

    else:
        chances -= 1
        print("Wrong movie name!")

    print(upd_movie if upd_movie else hidden_movie)
    print(f"Chances left: {chances}")

if upd_movie == selected_movie:
    print("You win!")
else:
    print(f"Game over! The movie was {selected_movie}")
