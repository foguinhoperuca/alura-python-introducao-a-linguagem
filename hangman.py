from random import random, randrange

def play():
    print("*********************************************")
    print("| Welcome to hangman game! Fruits Version !!|")
    print("*********************************************")

    possible_secret_words = (
        "banana",
        "maçã",
        "laranja",
        "limão",
        "pera",
        "uva",
        "mamão",
        "melancia"
    )
    secret_word = possible_secret_words[randrange(0, 8)].upper()
    attempts = randrange(1, 11)
    bingo = False
    bad_guess = []
    bad_word = []
    good_guess = ["?" for letter in secret_word]
    # for index, letter in enumerate(secret_word):
    #     good_guess.insert(index, "?")

    print(f"starting {good_guess=} with {attempts} attempts!!")

    while (not bingo and not attempts == 0):
        guess = input("Choose a letter: ")
        guess = guess.strip().upper()
        if guess in secret_word:
            for index, letter in enumerate(secret_word):
                # if secret_word.find(guess) != -1:
                if guess.upper() == letter.upper():
                    # print(f"Your {guess=} found at {index=}")
                    good_guess[index] = guess

            print(f"Your {guess=} is right!")
        else:
            print(f"Nay! No good {guess=}! Try another one!")
            bad_guess.extend([guess])
            attempts -= 1

        print("*** Here the status: ***")
        print(f"{good_guess} - missing {good_guess.count('?')} letter(s)")
        print(f"{sorted(bad_guess)=}: {len(bad_guess)} error(s)")

        if "?" not in good_guess:
            bingo = True
            break

        guess_word = input("Would you try to guess the full word? ")
        guess_word = guess_word.strip().upper()
        if guess_word == secret_word:
            bingo = True
            print(f"Good! You found the secret word! {guess_word=} == {secret_word=}")
        else:
            bingo = False  # FIXME need it!?
            bad_word.extend([guess_word])
            print(f"Oh boy! Not this time! You have {attempts} attempts.")
            print(f"{bad_word=}")

        print("--------------------------------------------------")

    if not bingo and attempts == 0:
        status = "lose"
    else:
        status = "win"

    print(f"End of hangman game. You {status}!! The secret word was {secret_word}")

if __name__ == "__main__":
    play()