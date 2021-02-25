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

# 23 February 2021
# Starting Out With Python Programming Exercise 3
# Design a class that holds the following personal data: name, address, age, and
# phone number. Write appropriate accessor and mutator methods. Also, write a program
# that creates three instances of the class. One instance should hold your information,
# and the other two should hold your friends' or family members' information.

class Perso_Info:
# Class that holds the name, address, age and phone number of a person.

    def __init__(self, name, address, age, phone_number):
        self.__name = name
        self.__address = address
        self.__age = age
        self.__phone_number = phone_number

    def set_name(self, name):
        self.__name = name
    
    def set_address(self, address):
        self.__address = address
    
    def set_age(self, age):
        self.__age = age
    
    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number

    def get_name(self):
        return self.__name
    
    def get_address(self):
        return self.__address
    
    def get_age(self):
        return self.__age

    def get_phone_number(self):
        return self.__phone_number
    
    def __str__(self):
        return 'Name: ' + self.__name + \
            '\nAddress: ' + self.__address + \
            '\nAge: ' + str(self.__age) + \
            '\nPhone Number: ' + str(self.__phone_number)

# Gathers the information of the user and creates an instance from the Perso_Info class.
name = input('Enter your first and last name: ')
address = input('Enter your address (street, city, state, zip code): ')
age = int(input('Enter your age: '))
phone_number = int(input('Enter your phone number (no spaces, parentheses or dashes): '))

my_info = Perso_Info(name, address, age, phone_number)

print()
print('Your Information:')
print(my_info)
print()

# Gathers the user's best friend's information and creates an instance of the 
# Perso_Info class.
name = input("Enter your best friend's first and last name: ")
address = input("Enter your best friend's address: ")
age = int(input("Enter your best friend's age: "))
phone_number = int(input("Enter your best friend's phone number (no spaces, parentheses or dashes): "))

best_friend = Perso_Info(name, address, age, phone_number)

print()
print("Your Best Friend's Information:")
print(best_friend)
print()

# Gathers the user's mother's information and creates an instance of the Perso_Info class.
name = input("Enter your mother's first and last name: ")
address = input("Enter your mother's address: ")
age = int(input("Enter your mother's age: "))
phone_number = int(input("Enter your mother's phone number (no spaces, parentheses or dashes): "))

mother = Perso_Info(name, address, age, phone_number)

print()
print("You Mother's Information:")
print(mother)

# 25 February 2021
# Starting Out With Python Programming Exercise 4 (User Input & Functions Version)
# Write a class named Employee that holds the following data about an employee in 
# attributes: name, ID number, department, and job title. Once you have written the 
# class, write a program that creates three Employee objects to hold the following data:

# Name               ID Number          Department          Job Title
# Susan Meyer        47899              Accounting          Vice President
# Mark Jones         39119              IT                  Programmer
# Joy Rogers         81774              Manufacturing       Engineer

# The program should store this data in three objects and then display the data for each
# employee on the screen. 

class Employee:
# Employee class that stores the name, ID number, department and job title data attributes.

    def __init__(self, name, ID_number, dept, title):
        self.__name = name
        self.__ID_number = ID_number
        self.__dept = dept
        self.__title = title
    
    def set_name(self, name):
        self.__name = name

    def set_ID_number(self, ID_number):
        self.__ID_number = ID_number

    def set_dept(self, dept):
        self.__dept = dept
    
    def set_title(self, title):
        self.__title = title

    def get_name(self):
        return self.__name
    
    def get_ID_number(self):
        return self.__ID_number

    def get_dept(self):
        return self.__dept

    def get_title(self):
        return self.__title

    def __str__(self):
        return 'Employee Name: ' + self.__name + \
        '\nEmployee ID Number: ' + str(self.__ID_number) + \
        '\nEmployee Dept: ' + self.__dept + \
        '\nEmployee Title: ' + self.__title

def main():
# Gets the input for three different employees and creates three different instances of
# the Employee class.    

    name = get_employee_name()
    ID_number = get_employee_ID()
    dept = get_employee_dept()
    title = get_employee_job_title()
    
    employee_1 = Employee(name, ID_number, dept, title)
    print()
    print(employee_1)
    print()

    name = get_employee_name()
    ID_number = get_employee_ID()
    dept = get_employee_dept()
    title = get_employee_job_title()
    
    employee_2 = Employee(name, ID_number, dept, title)
    print()
    print(employee_2)
    print()

    name = get_employee_name()
    ID_number = get_employee_ID()
    dept = get_employee_dept()
    title = get_employee_job_title()
    
    employee_3 = Employee(name, ID_number, dept, title)
    print()
    print(employee_3)
    
def get_employee_name():
    name = input("Enter the employee's first and last name: ")
    return name 

def get_employee_ID():
    ID_number = int(input("Enter the employee's ID number: "))
    return ID_number

def get_employee_dept():
    dept = input("Enter the employee's department: ")
    return dept

def get_employee_job_title():
    title = input("Enter the employee's job title: ")
    return title

main()

# 25 February 2021
# Starting Out With Python Programming Exercise 4 (Info Pre-Entered Version)
# Write a class named Employee that holds the following data about an employee in 
# attributes: name, ID number, department, and job title. Once you have written the 
# class, write a program that creates three Employee objects to hold the following data:

# Name               ID Number          Department          Job Title
# Susan Meyer        47899              Accounting          Vice President
# Mark Jones         39119              IT                  Programmer
# Joy Rogers         81774              Manufacturing       Engineer

# The program should store this data in three objects and then display the data for each
# employee on the screen. 

class Employee:
# Employee class that stores the name, ID number, department and job title data attributes.

    def __init__(self, name, ID_number, dept, title):
        self.__name = name
        self.__ID_number = ID_number
        self.__dept = dept
        self.__title = title
    
    def set_name(self, name):
        self.__name = name

    def set_ID_number(self, ID_number):
        self.__ID_number = ID_number

    def set_dept(self, dept):
        self.__dept = dept
    
    def set_title(self, title):
        self.__title = title

    def get_name(self):
        return self.__name
    
    def get_ID_number(self):
        return self.__ID_number

    def get_dept(self):
        return self.__dept

    def get_title(self):
        return self.__title

    def __str__(self):
        return 'Employee Name: ' + self.__name + \
        '\nEmployee ID Number: ' + str(self.__ID_number) + \
        '\nEmployee Dept: ' + self.__dept + \
        '\nEmployee Title: ' + self.__title


# Creates three Employee objects identifiable by employee ID_number and without any input by the user.    

name = 'Susan Meyers'
ID_number = 47899
dept = 'Accounting'
title = 'Vice President'

employee_47899 = Employee(name, ID_number, dept, title)
print()
print(employee_1)
print()

name = 'Mark Jones'
ID_number = 39119
dept = 'IT'
title = 'Programmer'

employee_39119 = Employee(name, ID_number, dept, title)
print(employee_2)
print()

name = 'Joy Rogers'
ID_number = 81774
dept = 'Manufacturing'
title = 'Engineer'

employee_81774 = Employee(name, ID_number, dept, title)
print(employee_3)
print()
