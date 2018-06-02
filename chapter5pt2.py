#Chapter 5 exercise
Name = raw_input("Give me your name, please: ");
Amount = input("How many widgets are you buying?: ");
Cost = input("How much do they cost per item?: ");
Total = float(Amount * Cost);

print "Your Total is $ {}".format(Total);
print "Thanks for shopping with us today, {}!".format(Name)
