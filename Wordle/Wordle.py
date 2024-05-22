import urllib.request
import random


def stringtochar(word):
    charList = list(word)
    return charList


def wordmatching(word,input):
    wordlist = []
    for i in range(len(word)):
        if word[i] == input [i]:
            wordlist.append(word[i])
        else:
            wordlist.append("_")
    return wordlist


word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
response = urllib.request.urlopen(word_site)
long_txt = response.read().decode()
wordslist = long_txt.splitlines()

print(wordslist)
mainmenu = True
while mainmenu:
    print("-----------------")
    print("Welcome to wordle!")
    print("-----------------")
    print("1. Start Game")
    print("2. Instruction")
    print("3. Stop Playing")
    print("-----------------")
    choice = input()
    if choice == "1":
        mainmenu = False
        gameOn = True
        gameWin = False
        wordlol = random.choice(wordslist)
        stringlist = stringtochar(wordlol)
        print(wordlol)
        guessingList = []
        counter = 0
        for i in stringlist:
            guessingList.append("_")
    if choice == "2":
        print("Guess the word")
        print("")
        print("")
        print("enter to go back")
        input()
    if choice == "3":
        break

    while gameOn:
        print(guessingList)
        print("Current attempt" ,counter)
        guessedword = input("Guess the word!\n")
        guessedwordlist = list(guessedword)


        if len(guessedwordlist) == len(stringlist):
            guessingList = wordmatching(stringlist, guessedwordlist)
            print(guessingList)
            if guessingList == stringlist:
                gameOn = False
                print("-----------------")
                print("Congratulations! You have won the game")
                print("You took a number of", counter , "attempts")
                print("Would you like to return to main menu or quit the game?")
                print("-----------------")
                print("1. return to main menu")
                print("2. quit")
                print("-----------------")
                choice = input()
                if choice == "1":
                    mainmenu = True
                    break
                if choice == "2":
                    break

            if counter > 5:
                gameOn = False
                print("-----------------")
                print("Sorry, you have reached the maximum number of tries")
                print("Would you like to return to main menu or quit the game?")
                print("-----------------")
                print("1. return to main menu")
                print("2. quit")
                print("-----------------")
                choice = input()
                if choice == "1":
                    mainmenu = True
                    break
                if choice == "2":
                    break

            print("-----------------")
            print("Unfortunately you haven't guess the word yet. Please Try Again")
            print("-----------------")
            counter += 1
        elif len(guessedwordlist) < len(stringlist) or len(guessedwordlist) > len(stringlist):
            print("Please input the correct amount of characters for the word")
