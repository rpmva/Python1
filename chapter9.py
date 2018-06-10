#Chapter 9 notes
#1
#states = {} <- dictionary
#states = {"Virginia": "Richmond", "Maryland": "Annapolis", "New York": "Albany"}
#print states . . . {'Maryland': 'Annapolis', 'New York': 'Albany', 'Virginia': 'Richmond'}
#states['Oregon'] = 'Salem' <- adding something to the dictionary
#states.pop(Oregon) = Salem; States = line 4 original list

#2
#user_emails = {'15363': 'doughnut.lover@gmail.com'}
#user_emails['15363'] = "rpmva@udel.edu"
#user_emails
#result --> {'15363': 'rpmva@udel.edu'}

#3 Getting Information About a Dictionary
#isbns = {'1234': 'Easy Math', '1357': "Things are odd', '2468': Let\'s break even"}
#isbns['2468'] = "Let's Break Even"
#isbns.has_key('1111') = False; <- check if a key is in a dictionary
#isbns.has_key('1234') = True;
#isbns.keys() = ['1234', '2468', '1357'] <- get keys
#isbns.values() = ['Easy Math', "Let's Break Even", 'Things are odd'] <- get values

#4
#d = {'one': 1, 'two': 2}
#'one' in d -> True
#'four' in d -> False

#5, Comparing Dictionaries
#a = {1: 'one', 2: 'two', 3: 'three'}
#b = {1: 'one', 2: 'two', 3: 'three'}
# c = {2: 'two', 3: 'three', 4: 'four'}
# a == b -> True
# b == c -> False 
