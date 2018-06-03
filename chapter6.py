#Chapter 6 Notes
#List = ['a', 'b', 'c'];
#Character at a certain index: List[0] = 'a';
#len(List) = 3;
#Count how often something appears in a list: List.count('a') = 1; List.count('d') = 0;
#Where an index occurs: List.index('b') = 1
#Checking if a character or string is in a list: 'd' in List = False
#Adding items to a list: x = []; x.append('one'); x.append('two'); x = ['one','two']
#Making a list longer: x1 = [1,2,3]; x2 = [4,5,6]; x1.extend(x2);
#Removing items from a list: numbers = [1,2,3,4,5,6]; numbers.remove(6); numbers = [1,2,3,4,5]
#Inserting items at specific indices: list = ['a','c','d']; list.insert(1,'b')
#Adding a list: a = [1,2,3]; b = [4,5,6]; a + b = [1,2,3,4,5,6]
#reverse() puts list in reverse order
#sort() puts numbers in numerical or alphabetical order

#Chapter 6 Exercise
stock = ['pepperoni', 'sausage', 'cheese', 'peppers']
x = raw_input("Please give me a topping: ")
toppings = [];
if x in stock:
    toppings.append(x)
    print "We have " + x + "!"
else:
    print "Sorry, we don't have " + x + "."

y = raw_input("Please give me one more topping: ")
if y in stock:
    toppings.append(y)
    print "We have " + y + "!"
else:
    print " Sorry, we don't have " + y + "."

print "Here are toppings: {}".format(toppings)
