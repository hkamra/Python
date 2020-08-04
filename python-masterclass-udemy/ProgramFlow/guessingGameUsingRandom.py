import random

highest = 10
answer = random.randint(1, highest)  # this is inclusive
print(answer)  # TODO: Remove after testing

print("Please guess number between 1 and {}: ".format(highest))
guess = int(input())

correct_guess = False
guess_in_first_time = True

while not correct_guess:
    if guess == 0:
        print("Game is Over")
        break
    if guess == answer and guess_in_first_time:
        print("You got it first time")
        correct_guess = True
    else:
        if guess == answer:
            print("Well done, you guessed it")
            correct_guess = True
        else:
            if guess < answer:
                print("Please guess higher")
            else:
                print("Please guess lower")
            guess = int(input())
            guess_in_first_time = False
