# 21 February 2021
# Starting Out With Python Algorithm Workbench Exercise 1
# Write a class definition named Book. The Book class should have data attributes
# for a book's title, the author's name, and the publisher's name. The class should
# also have the following:
# a. An __init__ method for the class that should accept an argument for each of the 
# data attributes.
# b. Accessor and mutator methods for each data attribute.
# An __str__ method that returns a string indicating the state of the object.

# The class Book holds the title, author and publishing information. 
class Book:
    # Initializes the attributes
    def __init__(self, title, author, publisher):
        self.__title = title
        self.__author = author
        self.__publisher = publisher

    # Mutator method to set the title attribute
    def set_title(self, title):
        self.__title = title

    # Mutator method to set the author attribute
    def set_author(self, author):
        self.__author = author

    # Mutator method to set the publisher attribute
    def set_publisher(self, publisher):
        self.__publisher = publisher

    # Accessor method to return the title attribute
    def get_title(self):
        return self.__title

    # Accessor method to return the author attribute
    def get_author(Self):
        return self.__author

    # Accessor method to return the publisher attribute
    def get_publisher(self):
        return self.__publisher

    # __str__ method to return the object's state as a string
    def __str__(self):
        return 'Title: ' + self.__title + \
            '\nAuthor: ' + self.__author + \
            '\nPublisher: ' + self.__publisher

