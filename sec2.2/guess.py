# This is a simple guess the number game

#import random module required for random function
import random

#Program asks user for his/her name
print('Hi what is your name?')
name = input()

#Program tells user it is thinking of a number between 1 and 20
print('Well ' + name + ', I am thinking of a number between 1 and 20')
secretNumber = random.randint(1, 20)

#Allows user to guess six times
for guessesTaken in range(1, 7): 
    print('take a guess.')
    guess = int(input())
    
    if guess < secretNumber:
        print ('your guess is too low')
    elif guess > secretNumber:
        print('your guess is too high')
    else:
        break # This condition is for the correct guess

if guess == secretNumber:
    print('good job ' + name + ', you guessed my number in ' + str(guessesTaken) + ' guesses.')
else:
    print('nope. the number i was thinking of was ' + str(secretNumber))

