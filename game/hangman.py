from random import randrange
import datetime
import logging
from time import sleep
from util import Util

def show_welcome_message(good_guess, initial_attempts):
    print("*********************************************")
    print("| Welcome to hangman game! Fruits Version !!|")
    print("*********************************************")
    logging.info(Util.info(f"starting {good_guess=} with {initial_attempts} attempts!!"))


def load_seeds(seed_file="hangman_seed.dat", start_line=0):
    possible_secret_words = []
    # hangman_seed = open(seed_file, "r", encoding="utf-8")
    with open(seed_file, "r", encoding="utf-8") as hangman_seed:
        for seed in hangman_seed:
            possible_secret_words.append(seed.strip().upper())
    # hangman_seed.close()

    secret_word = possible_secret_words[randrange(start_line, len(possible_secret_words))].upper()

    return secret_word


def initialize_good_guess(secret_word):
    return ["?" for _ in secret_word]


def ask_guess():
    sleep(1)
    guess = input("Choose a letter: ")
    return guess.strip().upper()


def guess_mark_as_correct(good_guess, guess, secret_word):
    for index, letter in enumerate(secret_word):
        if guess == letter:
            # FIXME good_guess was not returned. Why the program still works?!
            good_guess[index] = guess


def log_game(attempts, bad_guess, bad_word, good_guess, initial_attempts, secret_word, status):
    with open(f"../logs/hangman.log", "a", encoding="utf-8") as file_log:
        file_log.write(f"timestamp for this log: **{datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S')}**\n")
        file_log.write(f"good guesses: **{good_guess}**\n")
        file_log.write(f"bad guesses: **{bad_guess}**\n")
        file_log.write(f"bad word guessed: **{bad_word}**\n")
        file_log.write(
            f"Game result was **{status.upper()}** with **{attempts}** attempts remains of **{initial_attempts}**\n")
        file_log.write(f"The secret word was **{secret_word}**\n")
        file_log.write("-------------------------------------------------------------------------------\n")
    # file_log.close()


def guess_full_word():
    guess_word = input("Would you try to guess the full word? ")
    guess_word = guess_word.strip().upper()
    return guess_word


def print_status(status, secret_word):
    print(f"End of hangman game. You {status}!! The secret word was {secret_word}")

    if status == "lose":
        print("You been hanged!")
        print("    _______________         ")
        print("   /               \       ")
        print("  /                 \      ")
        print("//                   \/\  ")
        print("\|   XXXX     XXXX   | /   ")
        print(" |   XXXX     XXXX   |/     ")
        print(" |   XXX       XXX   |      ")
        print(" |                   |      ")
        print(" \__      XXX      __/     ")
        print("   |\     XXX     /|       ")
        print("   | |           | |        ")
        print("   | I I I I I I I |        ")
        print("   |  I I I I I I  |        ")
        print("   \_             _/       ")
        print("     \_         _/         ")
        print("       \_______/           ")
    else:
        print("Congratulations! You are the winner!")
        print("       ___________      ")
        print("      '._==_==_=_.'     ")
        print("      .-\\:      /-.    ")
        print("     | (|:.     |) |    ")
        print("      '-|:.     |-'     ")
        print("        \\::.    /      ")
        print("         '::. .'        ")
        print("           ) (          ")
        print("         _.' '._        ")
        print("        '-------'       ")


def draw_gibbet(attempts, initial_attempts):
    print(f"You already started with {initial_attempts} and now you have {attempts}!")

    print("  _______     ")
    print(" |/      |    ")

    if attempts == 6:
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if attempts == 5:
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if attempts == 4:
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if attempts == 3:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if attempts == 2:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if attempts == 1:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if attempts == 0:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def play():
    secret_word = load_seeds()
    attempts = randrange(1, 8)
    initial_attempts = attempts
    bingo = False
    bad_guess = []
    bad_word = []
    good_guess = initialize_good_guess(secret_word)
    logging.basicConfig(level=logging.INFO, format=Util.LOG_FORMAT_SIMPLE)

    show_welcome_message(good_guess, initial_attempts)

    while not bingo and not attempts == 0:
        guess = ask_guess()
        if guess in secret_word:
            guess_mark_as_correct(good_guess, guess, secret_word)

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

        guess_word = guess_full_word()
        if guess_word == secret_word:
            bingo = True
            print(f"Good! You found the secret word! {guess_word=} == {secret_word=}")
        else:
            bingo = False  # FIXME need it!?
            bad_word.extend([guess_word])
            print(f"Oh boy! Not this time! You have {attempts} attempts.")
            print(f"{bad_word=}")

        draw_gibbet(attempts, initial_attempts)
        print("--------------------------------------------------")

    if not bingo and attempts == 0:
        status = "lose"
    else:
        status = "win"

    log_game(attempts, bad_guess, bad_word, good_guess, initial_attempts, secret_word, status)
    print_status(status, secret_word)


if __name__ == "__main__":
    play()
