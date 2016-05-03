import random
import re

#Global variables: wordList, wrongGuessCounter, usedLetters, secretWord
wordList = ['cat', 'sun', 'cup', 'ghost', 'flower', 'pie', 'cow', 'banana', 
'snowflake', 'bug', 'book', 'jar', 'snake', 'light', 'tree', 'lips', 'apple']

wrongGuessCounter = 0
secretWord = random.choice(wordList)
usedLetters = []

#Display Board function:
def displayBoard(word):
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
    #Will one day display ASCII

#checkInput function:  Make sure input is single letter.  Append correct input to usedLetters
def checkInput():
    while True:
        print("")
        playerGuess = input("Guess a letter.").lower()
        if not re.match("[a-zA-Z]", playerGuess):
            print("Error: Only single letters allowed")
            continue
        elif len(playerGuess) > 1:
            print("Error: Only single letters allowed")
            continue
        elif playerGuess in usedLetters:
            print("Error: The letter '{}' has already been used.  Please guess again.".format(playerGuess))
            continue
        else:
            usedLetters.append(playerGuess)
            return playerGuess

#isInWord function: Checks if user input is in the secretWord (after checkInput)
def isInWord(guess):
    global wrongGuessCounter
    if guess in secretWord:
        print("YES!  The letter '{}' is in the Secret Word!\n".format(guess.upper()))
    else: 
        print("The letter '{}' is not in the Secret Word.\n".format(guess.upper()))
        wrongGuessCounter += 1
        
def win():
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
    global wrongGuessCounter
    global usedLetters
    global secretWord
    
    startOver = False
    
    startOver = input("Would you like to play again?").lower() in ["yes", "y"]
    if startOver == True:
        wrongGuessCounter = 0
        usedLetters = []
        secretWord = random.choice(wordList)
    else: 
        print("Have a nice day!")
        exit()
    
#main body:  Non-function.  Nest within while loop - calls all of the above functions as necessary
print("Welcome to Hangman! Try to guess the Secret Word. If you guess wrong five\
times the game is over.")
    
while wrongGuessCounter < 6:
    print(secretWord)
    #Display Board function.  Will take: secretWord.  Will return: Nothing
    displayBoard(secretWord)

    #Receives input and checks to make sure it is single letter (function) 
    #Will return: guess (player input that is a single letter)
    guess = checkInput()
    
    #Check input to see if it is in secretWord (function).
        #Will take: guess
        #If guess is not in secret word, increase wrongGuessCounter by 1
        #Will return: nothing
    isInWord(guess)
        
    #Check if player has won with last input (function)
    #If they win, display win message and call playAgain. If not, continue
    win()
        
#Check if player has lost by running out of turns (non-function)
#If they lost, display lose message and call playAgain
else:
    print("You are out of guesses.  The word was {}.".format(secretWord.upper()))
    playAgain()
