#Chapter 5 notes
#input() asks for input
#raw_input() asks for input and saves the user's input as a string
#float() converts string integers to a float
#int() converts floats to integers
#Getting a password:
from getpass import getpass
password = getpass(prompt="Password: ")
if password == "Ryan":
    print "That's clean you're in!"
else:
    print "Swing and a miss!"

#formatting output: use format() to replace words with variables {};
