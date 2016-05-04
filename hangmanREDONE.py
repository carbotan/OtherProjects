import random
import re
import requests
from hangmanPics import HANGMANPICS

#Get request to random word API
def apiWord():
    word = requests.get("http://randomword.setgetgo.com/get.php?len=7")
    return word.text.lower()

#Display Board function: Will take: secretWord.  Will return: Nothing
def displayBoard(word, usedLetters, wrongGuessCounter):
    #Will one day display ASCII
    print(HANGMANPICS[wrongGuessCounter])
    #Displays 'hashed' secretWord
    print("")
    print("SECRET WORD -->     ", end="")
    for letter in word:
        if letter in usedLetters:
            print(letter, end=" ")
        else:
            print("*", end="")
    print("     <-- SECRET WORD")
    #Display letters that have been used
    print("Your guessed letters:",end=" ")
    for x in sorted(usedLetters):
        print(x.upper(),end=" ")
    

#checkInput function:  Make sure input is single letter.  Append correct input to usedLetters
def checkInput(usedLetters):
    while True:
        print("")
        playerGuess = input("Guess a letter.").lower()
        if not re.match("[a-zA-Z]", playerGuess):
            print("Error: Only single letters allowed")
            continue
        elif len(playerGuess) != 1:
            print("Error: Only single letters allowed")
            continue
        elif playerGuess in usedLetters:
            print("Error: The letter '{}' has already been used.  Please guess again.".format(playerGuess.upper()))
            continue
        else:
            usedLetters.append(playerGuess)
            return playerGuess

#isInWord function: Checks if user input is in the secretWord (after checkInput)
#Will take: guess.  Will return: nothing  If guess is not in secret word, increase wrongGuessCounter by 1
def isInWord(guess, secretWord, wrongGuessCounter):
    if guess in secretWord:
        print("YES!  The letter '{}' is in the Secret Word!\n".format(guess.upper()))
    else: 
        print("The letter '{}' is not in the Secret Word.\n".format(guess.upper()))
        wrongGuessCounter += 1
    return wrongGuessCounter
        

#Check if player has won with last input (function)
#If they win, display win message and call playAgain. If not, continue
def win(secretWord, usedLetters):
    foundAllLetters = True
    for letters in secretWord:
        if letters not in usedLetters:
            foundAllLetters = False
            break
    if foundAllLetters == True: 
        print("You win!  The secret word was {}.  It took you {} guesses to find it!".format(secretWord.upper(), len(usedLetters)))
        playAgain()

#playAgain function:  Asks the user if they want to play agian.  Starts over if they do.  Exits if not
def playAgain():
    startOver = False
    
    startOver = input("Would you like to play again?").lower() in ["yes", "y"]
    if startOver == True:
        main()
    else: 
        print("Have a nice day!")
        exit()
    
#main body:  Non-function.  Nest within while loop - calls all of the above functions as necessary

def main():
    print("Welcome to Hangman! Try to guess the Secret Word. If you guess wrong five \
times the game is over.")

    wrongGuessCounter = 0
    usedLetters = []
    secretWord = apiWord()
    
    #Calls all functions while players hasn't reached max number of wrong guesses
    while wrongGuessCounter < 5:
        print(secretWord)
        displayBoard(secretWord, usedLetters, wrongGuessCounter)
        guess = checkInput(usedLetters)
        wrongGuessCounter = isInWord(guess, secretWord, wrongGuessCounter)
        win(secretWord, usedLetters)
        
    #Check if player has lost by running out of turns (non-function)
    #If they lost, display lose message and call playAgain
    else:
        print(HANGMANPICS[wrongGuessCounter])
        print("You are out of guesses.  The word was {}.".format(secretWord.upper()))
        playAgain()
        
if __name__ == "__main__":
    main()