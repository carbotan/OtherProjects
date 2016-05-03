import random
import string
import re


wordList = ['cat', 'sun', 'cup', 'ghost', 'flower', 'pie', 'cow', 'banana', 
'snowflake', 'bug', 'book', 'jar', 'snake', 'light', 'tree', 'lips', 'apple']

# Rename guess counter to show that it only increases with wrong guesses
wrongGuessCounter = 0
secretWord = random.choice(wordList)
usedLetters = []


def start():
    global wrongGuessCounter
    print("Here are the letters that have already been guessed:")
    print(sorted(usedLetters))
    print("")
    print("Number of incorrect guesses you have left: {} \n".format(5 - wrongGuessCounter))
    guess = input("Guess a letter.  Type 'solve' to guess the word.\n")
    if guess.lower() == "solve" or guess == "'solve'":
        solve()
        return None
    else:
        checkInput(guess)
        return guess
        
        
def solve():
    solution = input("What is the Secret Word?\n")
    if solution == secretWord:
        print("Congratulations!  You win!")
        exit()
    else:
        print("No.  That is not the Secret Word.")
        #guessCounter += 1
    
def checkInput(guess):
    global wrongGuessCounter
    if not re.match("[a-zA-Z]", guess):
        print("Error: Only single letters allowed")
        wrongGuessCounter -= 1
    elif len(guess) > 1:
        print("Error: Only single letters allowed")
        wrongGuessCounter -= 1
    elif guess in usedLetters:
        print("Error: The letter '{}' has already been used.  Please guess again.".format(guess))
        wrongGuessCounter -= 1
    else:
        usedLetters.append(guess)

def main():
    global wrongGuessCounter
    print("Welcome to Hangman! Try to guess the Secret Word. If you guess wrong five\
    times the game is over. The Secret Word has {} letters. \n".format(len(secretWord)))
    print(secretWord)
    while wrongGuessCounter < 6:
        guess = start()
        if guess is None:
            wrongGuessCounter += 1
            continue
        print("")
        print("SECRET WORD -->     ", end="")
        for letter in secretWord:
            if letter in usedLetters:
                print(letter, end="")
            else:
                print("*", end="")
        print("     <-- SECRET WORD")
        if guess.lower() in secretWord:
            print("YES!  The letter '{}' is in the Secret Word!\n".format(guess))
        else: 
            print("The letter '{}' is not in the Secret Word.\n".format(guess))
            wrongGuessCounter += 1
        #If all letters guessed, player wins
        for letters in secretWord:
            if letters in usedLetters:
                print("You win!")
    else: 
        print("You have no guesses left, you lose!")
    
        
    
if __name__ == "__main__":
    main()



