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

# 22 February 2021
# Starting Out With Python Programming Exercise 1
# Write a class named Pet which should have the following data attributes: __name,
# __animal_type, __age. The Pet class should have an __init__method and accessor and
# mutator methods for each data attribute. 
# Once you've written the class, write a program that creates an object of the class and
# prompts the user to enter the name, type and age of his/her pet. This data should be 
# stored as the object's attributes. Use the object's accessor methods to retrieve the
# pet's name, type, and age and display this data on the screen.

class Pet:
# Pet class gets and stores the name, animal type and of a pet.

    def __init__(self, name, animal_type, age):
    # Initializes the name, animal type and age of the pet.
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age

    def set_name(self, name):
    # Mutator method to set the pet name
        self.__name = name

    def set_animal_type(self, animal_type):
    # Mutator method to set the animal type
        self.__animal_type = animal_type

    def set_age(self, age):
    # Mutator method to set the pet age
        self.__age = age

    def get_name(self):
    # Accessor method to get the pet name
        return self.__name

    def get_animal_type(self):
    # Accessor method to get the animal type
        return self.__animal_type

    def get_age(self):
    # Accessor method to get the pet age
        return self.__age

# Program that gets the name, animal type and age of a pet. Creates an object of the Pet class with 
# this info and displaying the name, animal type and age through the class's accessor methods. 
name = input('Enter the name of your pet: ')
animal_type = input('Enter the type of animal of your pet (ex. Dog, Cat, Bird, Fish etc.): ')
age = int(input('Enter the age of your pet: '))

pet_info = Pet(name, animal_type, age)

print("Here are your pet's details:")
print('Name:', pet_info.get_name())
print('Animal Type:', pet_info.get_animal_type())
print('Age:', pet_info.get_age())

# 22 February 2021
# Starting Out With Python Programming Exercise 2
# Write a class named Car that has the following data attributes: __year_model,
# __make, and __speed. The Car class should have an __init__ method that accepts
# the car's year model and make as arguments. These values should be assigned to
# the object's __year_model, and __make data attributes. It should also assign 0 
# to the speed attribute. The class should have the following methods: accelerate: 
# add 5 to the speed data attribute each time it is called, brake: subtract 5 from
# the data attribute each time it is called, get_speed: return the current speed.
# Next design a program that creates a Car object and then calls the accelerate mehod
# five times. After each call to the accelerate method, get the current speed of the car
# and display it. Then call the brake method five times. After each call to the brake
# method, get the current speed of the car and display it.

class Car:
    
    def __init__(self, year_model, make):
    # Initializes the __year_model, __make, and __speed attributes.
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0
    
    def accelerate(self):
    # Adds 5 to the speed when called.
        self.__speed += 5
    
    def brake(self):
    # Subtracts 5 from the speed when called.
        self.__speed -= 5

    def get_speed(self):
    # Accessor method to return the __speed attribute
        return self.__speed

# Gets the year_model and make and passes them as arguments to create an object of the
# Car class
year_model = input("Enter the car year's model: ")
make = input('Enter the make of the car: ')

Tesla = Car(year_model, make)

# Calls the accelrate method 5 times and displays the speed level.
print('Acceleration')
print('------------')
print('Speed:', Tesla.get_speed())
for i in range(5):
    Tesla.accelerate()
    print('Speed:', Tesla.get_speed())

print()

# Calls the brake method 5 times and displays the speed level.
print('Brake')
print('-----------')
for i in range(5):
    Tesla.brake()
    print('Speed:', Tesla.get_speed())
