print "Welcome to the receipt program!"
total = [];
s = "*";

while True:
    cost = input("Enter the value for the seat. ['q' to quit]: ");
    if cost == 'q':
        print s * 5
        print "Total: ${}".format(sum(total));
        break
    elif type(cost) == float or type(cost) == int:
        total.append(cost);
    else:
        print "I'm sorry, but '{}' isn't valid. Please try again.".format(cost);
