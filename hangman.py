import random
import string
import re


wordList = ['cat', 'sun', 'cup', 'ghost', 'flower', 'pie', 'cow', 'banana', 
'snowflake', 'bug', 'book', 'jar', 'snake', 'light', 'tree', 'lips', 'apple']

guessCounter = 0
secretWord = random.choice(wordList)
usedLetters = []

'''
def solve(guess):
    pass

def checkInput():
    pass

def main():
    pass
'''

print("Welcome to Hangman! Try to guess the Secret Word. If you guess wrong five\
 times the game is over. The Secret Word has {} letters. \n".format(len(secretWord)))
print(secretWord)
while guessCounter < 8:
    print("Here are the letters that have already been guessed:")
    print(sorted(usedLetters))
    print("")
    print("This is guess number: {} \n".format(guessCounter + 1))
    guess = input("Guess a letter.  Type 'solve' to guess the word.\n")
    if guess.lower() == "solve" or guess == "'solve'":
        solve = input("What is the Secret Word?\n")
        if solve == secretWord:
            print("Congratulations!  You win!")
        else:
            print("No.  That is not the Secret Word.")
            guessCounter += 1
            continue
    elif not re.match("[a-zA-Z]", guess):
        print("Error: Only single letters allowed")
        continue
    elif len(guess) > 1:
        print("Error: Only single letters allowed")
        continue
    elif guess in usedLetters:
        print("Error: The letter '{}' has already been used.  Please guess again.".format(guess))
        continue
    usedLetters.append(guess)
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
        guessCounter += 1






