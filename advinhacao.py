print("********************************")
print("|| Try to Guess the number !! ||")
print("********************************")

secret_number = 42

guess = input("Try some number: ")
print("You say:", guess)

if (int(guess) == secret_number):
    print("Nice! Your guess was good!!")
else:
    print("Nay! Better lucky next time. The number was: ", secret_number)

print("Finishing class 02 - python-introducao-a-linguagem!")