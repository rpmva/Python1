#Chapter 4 Notes
#len() gets the length of a variable or a string
#upper() converts all letters to uppercase
#lower() converts all letters to lowercase
#capitalize() converts the first letter of a string to uppercase and the rest to lowercase
#title() converts the first letter of each word to uppercase and the rest to lowercase
#isdigit checks if a string or a variable only contains digits
#isalpha checks if a string or a variable only contains letters
#s = x; s * 5 = x x x x x
#\n goes to a new line
#\t tabs over a space
#strip() removes all whitespace or undesired characters; rstrip or lstrip
#count checks the amount of times a letter or a character occurs
#find() checks what character something occurs at in a sentence or paragraph. If find() finds nothing it returns -1
#replace() replaces one word with another

#Chapter 4 exercise
email = "In this biographical drama, Britain's King George VI struggles with an embarrassing stutter until he seeks help from speech therapist Lionel Logue."

if email.find("emergency") > 0:
    print "Do you want to make this email urgent?"
else:
    print "Do you want to set this email as non-urgent?"

#or

if email.find("emergency") == -1:
    print "Do you want to set this email as non-urgent?"
else:
    print "Do you want to make this email urgent?"
