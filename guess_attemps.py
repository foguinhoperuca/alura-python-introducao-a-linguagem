print("********************************")
print("|| Try to Guess the number !! ||")
print("********************************")

secret_number = 42
attempts = 3
turn = 1

while (turn <= attempts):
    guess = input("Try some number: ")
    print("You say:", guess)
    bingo = int(guess) == secret_number
    bigger = int(guess) > secret_number
    lesser = int(guess) < secret_number

    if (bingo):
        print("Nice! Your guess was good!! Your attempt is: {} of {}".format(turn, attempts))
        break
    else:
        print("Nay! Better lucky next time. Your attempt is: {} of {}".format(turn, attempts))
        turn += 1
        if (bigger):
            print("But guess what: your number is higher than the secret number!!")
        elif (lesser):
            print("But guess what: your number is lower than the secret number!!")

print("Finishing class 02 - python-introducao-a-linguagem!")