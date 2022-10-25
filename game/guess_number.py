from random import random, randrange


def play():
    print("********************************")
    print("|| Try to Guess the number !! ||")
    print("********************************")

    secret_number = randrange(1, 101)  # round(random() * 100)
    attempts = 0
    points = 1000

    print("Game prize is: ${:10.2f}. Wins who get the better score!".format(1000000.00))
    print("The price for game ticket is: EASY ({:d} points and {:d} attempts) ${:.2f}; NORMAL ({:d} points and {:d} attempts) ${:.2f}; HARD ({:d} points and {:d} attempts) ${:.2f}.".format(1000, 5, 100.00, 100, 3, 10.00, 10, 1, 0.99))

    level = int(input("Which level  you would like to play [1 - EASY | 2 - NORMAL | 3 - HARD]? "))
    if int(level) == 1:
        attempts = 5
        points = 1000
    elif int(level) == 2:
        attempts = 3
        points = 100
    elif int(level) == 3:
        attempts = 1
        points = 10
    else:
        print("Game level wasn't correct. Game is finished!!")
        exit(1)

    for turn in range(1, (attempts + 1)):
        guess = int(input("Try some number (1..100): "))
        print("You say:", guess)
        if (guess < 1 or guess > 100):
            print("Penalty! You *SHOULD* try numbers between 1 and 100!! You lost this turn: {0} of {1}!".format(turn,
                                                                                                                 attempts))
            print("------------------------------------")
            continue

        bingo = guess == secret_number
        bigger = guess > secret_number
        lesser = guess < secret_number

        if (bingo):
            print("Nice! Your guess was good!! Your attempt is: {} of {}".format(turn, attempts))
            points += 1000000
            break
        else:
            print("Nay! Better lucky next time. Your attempt is: {} of {}".format(turn, attempts))
            points -= abs(secret_number - guess)
            if (bigger):
                print("But guess what: your number is higher than the secret number!!")
            elif (lesser):
                print("But guess what: your number is lower than the secret number!!")
            print("------------------------------------")

    print(f"Finishing game! The random number was: {secret_number}; Your points was: {points}.")


if __name__ == "__main__":
    play()