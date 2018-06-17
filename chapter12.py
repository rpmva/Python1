#Chapter 12 Notes
# class Test(object):
# 	def __init__(self):
# 		self.one = 1

#t = Test()
#print
#s = Test()
#t == s -> False

#Equality
# class Test(object):
# 	def __init__(self):
# 		self.num = 5
#
#
# a = Test()
# b = Test()
# a == b -> False

#Using __eq__
#class Test(object):
# 	def __init__(self, num):
# 		self.num = num
# 	def __eq__(self, other):
# 		if self.num == other.num:
# 		   return True
# 		else:
# 		   return False
#
#
# a = Test(5)
# b = Test(5)
# c = Test(7)
# a == b -> True
# a == c -> False

#Using __ne__
# class Test(object):
# 	def __init__(self, num):
# 		self.num = num
# 	def __eq__(self, other):
# 		if self.num == other.num:
# 		   return True
# 		else:
# 		   return False
# 	def __ne__(self, other):
# 		if self.num != other.num:
# 			return True
# 		else:
# 			return False
#
#
# a = Test(5)
# b = Test(5)
# c = Test(7)
# a != b -> False
# a !=c -> True

#__gt__() -> greater than
#__lt__() -> less than
#__gte__() -> greater than or equal to
#__lte__() -> less than or equal to

#Working with print
# class Test(object):
# 	def __init__(self, text, num):
# 		self.text = text
# 		self.num = num
#
#
# a = Test(text="Hello", num=10)
# print a
# <__main__.Test object at 0x10daf2710>

#__str__
# class Test(object):
# 	def __init__(self, text, num):
# 		self.text = text
# 		self.num = num
# 	def __str__(self):
# 		return self.text
#
#
# a = Test(text="Hello", num=10)
# print a -> Hello

#printing out all attributes
# class Test(object):
# 	def __init__(self, word, num):
# 		self.word = word
# 		self.num = num
# 	def __str__(self):
# 		return "Values in this object:\
# 		word = {word}, num = {num}".format(word=self.word, num =self.num)
#
#
# a = Test(word = "Hello", num=5)
# print a
# Values in this object:word = Hello, num = 5

#InventoryItem
class InventoryItem(object):
    def __init__(self, title, description, price, store_id):
        self.title = title
        self.description = description
        self.price = price
        self.store_id = store_id

    def __str__(self):
        return self.title

    def __eq__(self, other):
        if self.store_id == other.title:
            return True
        else:
            return False

    def change_description(self, description=""):
        if not description:
            description = raw_input("Please give me a description: ")
        self.description = description

    def change_price(self, price=-1):
        while price < 0:
            price = raw_input("Please give me the new price [x.xx]: ")
            try:
                price = float(price)
                break
            except:
                print "I'm sorry, but {} isn't valid.".format(price)
        self.price = price

    def change_title(self, title=""):
        if not title:
            title = raw_input("Please give me a new title: ")
        self.title = title

#Subclassing a class
class Book(InventoryItem):
    def __init__(self, title, description, price, format, author, store_id):
        super(Book, self).__init__(title=title, description=description, price=price, store_id=store_id)
        self.format = format
        self.author = author

    def __str__(self):
        book_line = "{title} by {author}".format(title=self.title, author=self.author)
        return book_line

    def __eq__(self, other):
        if self.title == other.title and self.author == other.author:
            return True
        else:
            return False

    def change_format(self, format):
        if not format:
            format = raw_input("Please give me the new format: ")
        self.format = format

    def change_author(self, author):
        if not author:
            author = raw_input("Please give me the new author: ")
        self.author = author

#Software class
class Software(InventoryItem):
    def __init__(self, title, description, price, os, rating, store_id):
        super(Software, self).__init__(title=title, description=description, price=price, store_id=store_id)
        self.os = os
        self.rating = rating

    def __str__(self):
        about_software = "{title} for {os} operating systems and had a rating of {rating}".format(title=self.title, os=self.os, rating=self.rating)
        return about_software

    def __eq__(self, other):
        if self.title == other.title and self.rating == other.rating:
            return True
        else:
            return False

    def change_os(self, os):
        if not os:
            os = raw_input("Please give me the new operating system: ")
        self.os = os

    def change_rating(self, rating):
        if not rating:
            rating = raw_input("Please give me the new rating: ")
        self.rating = rating
        
#Using the class
hamlet = Book(title="Hamlet",description="A Dane has a bad time.", price = 5.99, format = "paperback", store_id="29382918", author="William Shakespeare")
hamlet_hardback = Book(title="Hamlet", description="A Dane has a bad time.", price = 10.99, format="hardback", store_id="3894083920",author="William Shakespeare")
macbeth = Book(title="Macbeth", description="Don't listen to strange ladies on the side of the road.", price=4.99, format="paperback", store_id="23928932", author="William Shakespeare")
