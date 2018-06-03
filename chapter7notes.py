#Chapter 7 notes
#range(7) = [0,1,2,3,4,5,6]; range(1,5) = [1,2,3,4]; range(-5,5) = [-5,-4,-3,-2,-1,0,1,2,3,4];
#Naming loop variable: for year in range(1997,2019):
                        #print "In {}, I live".format(year)
#Iterating through lists: letters = ['a','b','c']
                          #for letter in letters:
                            #print "{} is a letter of the alphabet".format(letter)
#Skipping to the next list item: numbers = [5, 2, 0, 20, 30]
                                 #for number in numbers:
                                    #if number == 0:
                                        #print "Ugh. You gave me a 0"
                                        #continue
                                    #new_number = 100.0/number
                                    #print "100/{} = {}".format(number, new_number)

#Breaking Out of a Loop: cart = [20.25, 30.04, 102.4, 50, 80]
                        #for item in cart:
                            #print item
                            #if item > 100:
                                #print "You are going to require insurance on this order."

#Using Break: cart = [50.25, 20.98, 99.99, 1.24, .84, 60.03]
            #for item in cart:
                #print item
                #if item > 100:
                    #print "You are going to require insurance on this order."
                    #break
                #else:
                    #print "No insurance will be required for this order."

#While Loops: age = raw_input("Please give me your age in years (eg. 30): ")
             #while not age.isdigit():
                #print "I'm sorry, but {} isn't valid.".format(age)
                #age = raw_input("Please give me your age in years (eg. 30): ")
            #print "Thanks! Your age is set to {} ".format(age)

#Infinite Loops: while True:
                    #text = raw_input("Give me some text, and I'll count the e's. Enter 'q' to quit: ")
                    #if text == 'q':
                        #break
                    #print text.count('e')

#Chapter 7 Exercise
#sum() to add a list
