def overprint():
    print("\n\n\n\n\n\n\n\n")

alphabet = "abcdefghijklmnopqrstuvwxyz"

while True:
    overprint()
    wordtoguess = "oooooooooooooooooooooooooooo"
    wordinvalid = True
    while wordinvalid:
        wordtoguess = input("Word: ")
        overprint()
        if len(wordtoguess) <= 18:
            if len(wordtoguess) > 1:
                guessed = []
                wordinvalid = False
                for blank in range(len(wordtoguess)):
                    if wordtoguess[blank] == " ":
                        guessed.append("/")
                    elif wordtoguess[blank] in alphabet:
                        guessed.append("_")
                    else:
                        wordinvalid = True
                if wordinvalid:
                    print("Only letters allowed.")
            else:
                print("Too short word.")
        else:
            print("Too long word.")
    solved = False
    lettersguessed = []
    wrongnum = 0
    while solved == False and wrongnum < 10:
        printword = ""
        for blank in guessed:
            printword += str(blank)
        print(printword)
        printguessed = "Used: "
        for char in lettersguessed:
            printguessed += str(char)
        print(printguessed)
        print("Mistakes: " + str(wrongnum))
        guess = input("Guess: ").lower()
        overprint()
        if len(guess) == 1:
            if guess in lettersguessed:
                print("Letter already used.")
            elif guess not in alphabet:
                print("That is not a letter.")
            else:
                lettersguessed.append(guess)
                inword = False
                for index in range(len(wordtoguess)):
                    if wordtoguess[index] == guess:
                        guessed[index] = guess
                        inword = True
                if inword == False:
                    wrongnum += 1
                elif "_" not in guessed:
                    solved = True
                    print("You solved the word! \nThe word was: \n'" + wordtoguess + "'")             
        elif len(guess) > 1:
            if guess == wordtoguess:
                solved = True
                print("You solved the word! \nThe word was: \n'" + wordtoguess + "'")
            else:
                print("Not the word.")
                wrongnum += 1
    if wrongnum > 9:
        print("You did not solve it. \nThe word was: \n'" + wordtoguess + "'")
    input()
