import random


def hangman(word):
    wrong = 0

    stages = ["",
              "_____________              ",
              "|              |           ",
              "|              0           ",
              "|              |           ",
              "|            / | \\         ",
              "|           /     \\        ",
              "|                          "]

    remaining_letters = list(word)
    board = ["__"] * len(word)
    win = False
    print("Welcom to Hangman!")

    while (wrong < len(stages) and win == False):
        char = input("Guss the letter! \n")
        if char in remaining_letters:
            char_index = remaining_letters.index(char)
            board[char_index] = char
            remaining_letters[char_index] = "$"
            if "__" not in board:
                print("You win!")
                print(" ".join(board))
                win = True
        else:
            wrong += 1

    # print((" ".join(board)))
    # print("\n".join(stages[0:wrong + 1]))

    if not win:
        print("\n".join(stages[0:wrong]))
        print("You lose! It was {}.".format(word))


x = random.choice(["Nourhan", "Mirna", "Esraa", "Rowan", "Amany"])
hangman(str(x))
