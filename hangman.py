def overprint():
    print(7*"\n")

alphabet = "abcdefghijklmnopqrstuvwxyz"
def printwordfunc(wordtoprint):
    if len(wordtoprint) > 21:
        lastspace = 0
        for charnum in range(21):
            if wordtoprint[charnum] in [" ","/"]:
                lastspace = charnum
        if lastspace == 0 or len(wordtoprint) - lastspace > 21:
            newword = ""
            for char in wordtoprint:
                newword += char
                if len(newword) == 21:
                    newword += "\n"
        else:
            newword = ""
            for char in wordtoprint:
                newword += char
                if len(newword) == lastspace+1:
                    newword += "\n"
        print(newword)
    else:
        print(wordtoprint)
while True:
    overprint()
    wordtoguess = ""
    wordinvalid = True
    while wordinvalid:
        print("Enter word to guess:")
        wordtoguess = input()
        overprint()
        if len(wordtoguess) <= 42:
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
        printwordfunc(printword)
        printguessed = "Used: "
        for char in lettersguessed:
            printguessed += str(char)
            if len(printguessed) == 21:
                printguessed += "\n"
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
                    print("You solved the word!\nThe word was:")
                    printwordfunc(wordtoguess)
        elif len(guess) > 1:
            if guess == wordtoguess:
                solved = True
                print("You solved the word!\nThe word was:")
                printwordfunc(wordtoguess)
            elif len(guess) != len(wordtoguess):
                print("Invalid guess.")
            else:
                print("Not the word.")
                wrongnum += 1
    if wrongnum > 9:
        print("You did not solve it.\nThe word was:")
        printwordfunc(wordtoguess)
    input()
