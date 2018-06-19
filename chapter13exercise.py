Exercise 1
from random import random
x = 0
while (random != 0 and random != 1):
    print random()
    print "Test item number: {}".format(x)
    x = x + 1
    if random == 0 or random == 1:
        print "Test complete!"
        break

Exercise 2
from random import randint
print "Welcome to the number guessing game!"
print "I have my number..."

MyNum = randint(1,10);
MyGuess = ""

def check_guess(MyGuess,MyNum):

    if MyGuess > MyNum:
        print "That's too high. Try again!"
        return False
    elif MyGuess < MyNum:
        print "That's too low. Try again!"
        return False
    else:
        print "You got it! Thanks for playing!"
        return True

while MyGuess != MyNum:
    MyGuess = input("What is your guess [1-10]? ")

    check_guess(MyGuess,MyNum)
