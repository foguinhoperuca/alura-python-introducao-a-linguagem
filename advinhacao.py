print("********************************")
print("|| Try to Guess the number !! ||")
print("********************************")

secret_number = 42

guess = input("Try some number: ")
print("You say:", guess)
bingo = int(guess) == secret_number
bigger = int(guess) > secret_number
lesser = int(guess) < secret_number

while not bingo:
    if (bingo):
        print("Nice! Your guess was good!!")
    else:
        print("Nay! Better lucky next time. The number was: ", "hahaha - you think that I will show it to you...")
        #if (int(guess) < secret_number):
        if (bigger):
            print("But guess what: your number is higher than the secret number!!")
        elif (lesser):
            print("But guess what: your number is lower than the secret number!!")

        print("-----------------------------------------------")
        guess = input("Try some number: ")
        print("You say:", guess)
        bingo = int(guess) == secret_number
        bigger = int(guess) > secret_number
        lesser = int(guess) < secret_number

print("Finishing class 02 - python-introducao-a-linguagem!")