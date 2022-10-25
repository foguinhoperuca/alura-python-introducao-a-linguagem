import guess_number
import hangman

def choose_game():
    chosen = False

    while not chosen:
        game = int(input("Choose your game [0] Guess the Number [1] Hangman: "))

        if game == 0:
            print("Go to guess the number game")
            guess_number.play()
            chosen = True
        elif game == 1:
            print("Go to hangman game")
            hangman.play()
            chosen = True
        else:
            print("Incorrect option! Choose wisely [0 guess | 1 hangman] !")

    print("Thanks for the fun! Bye!!")


if __name__ == "__main__":
    choose_game()