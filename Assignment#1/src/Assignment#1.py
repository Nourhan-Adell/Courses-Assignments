list = [1, 2, 3, 4, 5, 6]
while (True):
    try:
        v = int(input("guess a number or enter q to quit\n"))

        if v in list:
            print("successfully guessed a number in the list\n")
        else:
            print("not successfully guessed a number in the list\n")
    except ValueError:
        break
