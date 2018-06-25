#Chapter 15 notes
#Writing comments in code

#Explaining code with docstrings
# class Test(object):
#     ''' This is just a test object.
#         It doesn't do much, really.
#     '''
#     def __init__(self):
#      ''' This sets up the Test object. Doesn't
#          take any parameters.
#      '''
#      self.num = 10

# from doc import Test
# t = Test()
# help(t)

class Book(object):
    ''' Class for the Book object.
    '''
     def __init__(self, title="", author=""):
         ''' Sets Up a Book. title and author should be strings, but are
             not required.
         '''
         self.title = title
         self.author = author

     def __str__(self):
         ''' Formatting for printing a book. Returns the following:

             {title} by {author}
             No further formatting is done, so if you want title style
             capitalization, do it yourself.
         '''
         return "{title} by {author}".format(title=self.title, author=self.author)

#README and Install
