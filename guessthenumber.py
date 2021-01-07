import random

number = random.randint(1, 20)
game_end = False

while game_end == False:
    answer_guessed = int(input("Guess between 1 and 20: "))
    if number == answer_guessed:
        print("\nYou guessed the answer, Good Job!")
        game_end = True
    elif answer_guessed > number:
        print("\nYou guess is too high, Guess again!")
    elif answer_guessed < number:
        print("\n Your guess is too low, Guess again!")