def play():
    print("****************************")
    print("| Welcome to hangman game! |")
    print("****************************")

    secret_word = "banana"
    attempts = 3
    bingo = False
    bad_guess = []
    bad_word = []
    good_guess = []

    for index, letter in enumerate(secret_word):
        good_guess.insert(index, "?")

    print(f"starting {good_guess=}")

    while (not bingo and not attempts == 0):
        guess = input("Choose a letter: ")
        found = False
        for index, letter in enumerate(secret_word):
            # if secret_word.find(guess) != -1:
            if guess == letter:
                found = True
                # print(f"Your {guess=} found at {index=}")
                good_guess[index] = guess

        if found:
            print(f"Your {guess=} is right!")
        else:
            print(f"Nay! No good {guess=}! Try another one!")
            bad_guess.extend([guess])
            attempts -= 1

        # TODO scape from game if secret word is correct!
        print("*** Here the status: ***")
        print(f"{good_guess}")
        print(f"{sorted(bad_guess)=}")
        guess_word = input("Would you try to guess the full word? ")
        if guess_word == secret_word:
            bingo = True
            print(f"Good! You found the secret word! {guess_word=} == {secret_word=}")
        else:
            bingo = False  # FIXME need it!?
            bad_word.extend([guess_word])
            print("Oh boy! Not this time! Try again")
            print(f"{bad_word=}")

        print("--------------------------------------------------")

    if not bingo and attempts == 0:
        status = "lose"
    else:
        status = "win"

    print(f"End of hangman game. You {status}!! The secret word was {secret_word}")

if __name__ == "__main__":
    play()