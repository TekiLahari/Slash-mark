import random
import time

def introduction():
    print("May I ask you for your name?")
    player_name = input()
    print(player_name + ", we are going to play a game. I am thinking of a number between 1 and 200")
    time.sleep(.5)
    print("Go ahead. Guess!")
    return player_name

def choose_number(player_name):
    chosen_number = random.randint(1, 200)
    guesses_taken = 0
    while guesses_taken < 6:
        try:
            guess = int(input("Guess: "))
            if 1 <= guess <= 200:
                guesses_taken += 1
                if guess < chosen_number:
                    print("The guess is too low.")
                elif guess > chosen_number:
                    print("The guess is too high.")
                else:
                    print('Good job, ' + player_name + '! You guessed my number in ' + str(guesses_taken) + ' guesses!')
                    return
            else:
                print("Please enter a number between 1 and 200.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    print('Nope. The number I was thinking of was ' + str(chosen_number))

play_again = "yes"
while play_again.lower() in ["yes", "y"]:
    player_name = introduction()
    choose_number(player_name)
    play_again = input("Do you want to play again? (yes/no): ")
