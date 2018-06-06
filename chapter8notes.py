#Chapter 8 Notes and Practice

#1
# def hello():
#     print "Hello! How are you?"
#
# hello()

#2
# def hello2(name):
#     print "Hello, {}".format(name)
#
# hello2("Ryan")

#3
# def print_total(customer_name, items):
#     print "Total for {}".format(customer_name)
#     total = 0
#     for item in items:
#         total = total + item
#     print "${}".format(total)
#
# print_total(items = [1.25,2.50,3.75], customer_name = "Ryan")

#4
# def print_welcome(first, last, middle = ''):
#     print "Welcome, {} {} {}!".format(first, middle, last)
#     print "Enjoy your stay!"
#
# print_welcome(first = "Ryan", middle = "Patrick", last = "McGovern")

#5, using return
# def get_total(items):
#     total = 0;
#     for item in items:
#         total = total + item
#     return total
#
# items = [2,5,7,8,2]
# items_total = get_total(items)
# print items_total

#6
# def get_square_and_cube(number):
#     square = number ** 2
#     cube = number ** 3
#     return square, cube
#
# result = get_square_and_cube(5)
# print result
#
# square, cube = get_square_and_cube(3)
# print square
# print cube

#7
# def check_year(year):
#     if len(year) != 4:
#         print "{} is invalid as a year".format(year)
#         return
#     print "Good, that seems to work as a year!"
#
# check_year("1990")

#8, parameters and scope
# def add_five(number):
#     number = number + 5
#     print number
#
# x = 5
# add_five(x)

#9, grouping functions within a function
# def main():
#     username = get_username()
#     password = get_password()
#     authenticated = authenticate(user=username, password=password)
#     if authenticated:
#         print_timesheet(username)
#         add_hours(username)
#
# if __name__ == "__main__":
#     main()

#name is a special variable that Python sets when it runs a file
#main means we ran the file directly

#10, Sending a varying number of parameters
#**kwargs extra items added to a list
# def test_args(item_one, item_two, **kwargs):
#     print item_one
#     print item_two
#     print kwargs
#
# test_args(item_one="Let's", item_two="Go", item_three="Caps", item_four="!!!!")

#11
#*args takes non-keyboard values and stores them in a tuple
# def test_args(first, second, *args):
#     print first
#     print second
#     print args
#
# test_args(1,2,3,4,5)
