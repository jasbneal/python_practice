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

# 24 February 2021
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

# 24 February 2021
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

# 25 February 2021
# Starting Out With Python Programming Exercise 5 (Info Pre-Entered Version)
# Write a class named RetailItem that holds data about an item in a retail store.
# The class should store the following data in attributes: item, description, units
# in inventory, and price. Once you have written the class, write a program that 
# creates three RetailItem objects and stores the following data in them:

#                   Description         Units in Inventory              Price
#   Item #1         Jacket                      12                      $59.95
#   Item #2         Designer Jeans              40                      $34.95
#   Item #3         Shirt                       20                      $24.95

class RetailItem():
# Class that stores a retail item's description, number of units in 
# inventory and price.

    def __init__(self, descr, units, price):
        self.__descr = descr 
        self.__units = units 
        self.__price = price 

    def set_descr(self, descr):
        self.__descr = descr
    
    def set_units(self, units):
        self.__units = units

    def set_price(self, price):
        self.__price = price

    def get_descr(self):
        return self.__descr

    def get_units(self):
        return self.__units

    def get_price(self):
        return self.__price

    def __str__(self):
        return '\nDescription: ' + self.__descr + \
        '\nUnits: ' + str(self.__units) + \
        '\nPrice: $' + str(self.__price)

# Creates three objects that store the given description, units and price.
descr = 'Jacket'
units = 12
price = 59.95

item_1 = RetailItem(descr, units, price)

descr = 'Designer Jeans'
units = 40
price = 34.95

item_2 = RetailItem(descr, units, price)

descr = 'Shirt'
units = 20
price = 24.95

item_3 = RetailItem(descr, units, price)

# 25 February 2021
# Starting Out With Python Programming Exercise 5 (Info Entered By User Version)
# Write a class named RetailItem that holds data about an item in a retail store.
# The class should store the following data in attributes: item, description, units
# in inventory, and price. Once you have written the class, write a program that 
# creates three RetailItem objects and stores the following data in them:

#                   Description         Units in Inventory              Price
#   Item #1         Jacket                      12                      $59.95
#   Item #2         Designer Jeans              40                      $34.95
#   Item #3         Shirt                       20                      $24.95

class RetailItem():
# Class that stores a retail item's description, number of units in 
# inventory and price.

    def __init__(self, descr, units, price):
        self.__descr = descr 
        self.__units = units 
        self.__price = price 

    def set_descr(self, descr):
        self.__descr = descr
    
    def set_units(self, units):
        self.__units = units

    def set_price(self, price):
        self.__price = price

    def get_descr(self):
        return self.__descr

    def get_units(self):
        return self.__units

    def get_price(self):
        return self.__price

    def __str__(self):
        return '\nDescription: ' + self.__descr + \
        '\nUnits: ' + str(self.__units) + \
        '\nPrice: $' + str(self.__price)

# Creates three objects that store the given description, units and price by 
# calling the name, descr, inv_units and price functions.

def main():
    descr = create_descr()
    units = create_inv_units()
    price = create_price()
    item_1 = RetailItem(descr, units, price)

    descr = create_descr()
    units = create_inv_units()
    price = create_price()
    item_2 = RetailItem(descr, units, price)

    descr = create_descr()
    units = create_inv_units()
    price = create_price()
    item_3 = RetailItem(descr, units, price)

def create_descr():
    descr = input("Enter the item's description: ")
    return descr

def create_inv_units():
    units = int(input("Enter the amount of units on hand of this item: "))
    return units

def create_price():
    price = float(input('Enter the price of the item: '))
    return price

main()

# 25-28 February 2021
# Starting Out With Python Programming Exercise 6
# Create a program that stores Employee objects in a dictionary. Use the employee
# ID number as the key. The program should present a menu that lets the user perform
# the following: look up an employee in the dictionary, add a new employee to the 
# dictionary, change an existing employee's name, department, and job title in the
# dictionary, delete an employee from the dictionary, quit the program.
# When the program ends, it should pickle the dictionary and save it to a file. Each
# time the program starts, it should try to load the pickled dictionary from the file.
# If the file does not exist, the program should start with an empty dictionary.

# Come back to the import pickle/load dictionary contents, in the process of making functions for the
# menu options. Look up how to add objects as values to menus, does there need to be another choice
# input by the user at the end of the while loop or does it automatically repeat? 

import Employee_Class
import pickle

# MENU
LOOK_UP = 1
ADD_NEW_EMPLOYEE = 2
CHANGE_EXISTING_EMPLOYEE_INFO = 3
DELETE_EMPLOYEE = 4
QUIT = 5

def main():
# Opens the pickled employee_directory.dat file, unpickles its contents and saves it to employee_dct.
# If the file doesn't exist, a new employee_dct dictionary is created. 
# Loop allows the user to select their desired option as long the option != quit.
    try:
        input_file = open('employee_directory.dat', 'rb')
        employee_dct = pickle.load(input_file)
        input_file.close()
    except FileNotFoundError:
        employee_dct = {}
    finally:
        choice = 0
        print(employee_dct)

        while choice != 5:
            print()
            print('MENU')
            print('------------------')
            print('Look up an employee in the directory: 1')
            print('Add a new employee to the directory: 2')
            print("Change an existing employee's information: 3")
            print('Delete an employee from the directory: 4')
            print('Quit: 5')

            choice = int(input("Enter the action you'd like to make: "))

            if choice < 1 or choice > 5:
                print("You've entered an invalid selection.")
                choice = int(input("Enter a valid selection: "))

            if choice == 1:
                look_up_emp(employee_dct)

            if choice == 2:
                add_new_employee(employee_dct)

            if choice == 3:
                change_employee_info(employee_dct)

            if choice == 4:
                delete_employee(employee_dct)

        print(employee_dct)

    output_file = open('employee_directory.dat', 'wb')
    pickle.dump(employee_dct, output_file)
    output_file.close()
    
def look_up_emp(dct):
# Function: Look-up employee info by ID number & ValueError exception handled. 
    try: 
        ID_number = int(input("Enter the employee's ID number: "))
    except ValueError:
        print('You must only enter numbers to represent the employee ID.')
        ID_number = int(input("Enter the employee's ID number: "))
    if ID_number in dct:
        print(dct[ID_number])
    else:
        print('The employee ID number cannot be found.')

def add_new_employee(dct):
# Function: Add new employee & ValueError exception handled.
    try: 
        ID_number = int(input("Enter the employee's ID number: "))
    except ValueError:
        print('You must only enter numbers to represent the employee ID.')
        ID_number = int(input("Enter the employee's ID number: ")) 
    if ID_number not in dct:
        name = input("Enter the employee's name: ")
        dept = input("Enter the employee's department: ")
        title = input("Enter the employee's job title: ")
        emp_ID = Employee_Class.Employee(name, ID_number, dept, title)
        dct[ID_number] = emp_ID
    else:
        print('This employee already exists within the directory.')

def change_employee_info(dct):
# Function: Change employee info (name, dept, title) & ValueError exception handled.
    try: 
        ID_number = int(input("Enter the employee's ID number: "))
    except ValueError:
        print('You must only enter numbers to represent the employee ID.')
        ID_number = int(input("Enter the employee's ID number: "))
    if ID_number in dct:
        name = input("Update the employee's name: ")
        dept = input("Update the employee's department: ")
        title = input("Update the employee's job title: ")
        emp_ID = Employee_Class.Employee(name, ID_number, dept, title)
        dct[ID_number] = emp_ID

def delete_employee(dct):
# Function: Delete an eployee via the ID number & ValueError exception handled.
    try: 
        ID_number = int(input("Enter the employee's ID number: "))
    except ValueError:
        print('You must only enter numbers to represent the employee ID.')
        ID_number = int(input("Enter the employee's ID number: "))
    if ID_number in dct:
        del dct[ID_number]
        print("This employee's information has been deleted from the directory.")
    else:
        print('This employee is not in the directory') 

main()

# 4 March 2021
# Starting Out With Python Programming Exercise 7
# Assuming you have created the RetailItem class for Programming Exercise 5, create
# a CashRegister class that can be used with the RetailItem class. The CashRegister
# class should be able to internally keep a list of RetailItem objects and have the
# following methods: 
# A method named purchase_item that accepts a RetailItem object as an argument. Each
# time the purchase_item method is called, the RetailItem object that is passed as an
# argument should be added to the list.
# A method named get_total that returns the total price of all the RetailItem objects
# stored in the CashRegister object's internal list.
# A method named show_items that displays data about the RetailItem objects stored in
# the CashRegister object's internal list.
# A method named clear that should clear the CashRegister object's internal list.

# Demonstrate the CashRegister class in a program that allows the user to select several
# items for purchase. When the user is ready to check out, the program should display
# a list of all the items he/she has selected for purchase, as well as the total price.

import RetailItem
import CashRegister
import pickle

# MENU
ADD_ITEM_TO_INV = 1
UPDATE_ITEM_UNITS = 2
DELTE_ITEM_FROM_INVENTORY = 3
PURCHASE = 4

def main():
    
    try:
        input_file = open('item_inv.dat', 'rb')
        inv_dct = pickle.load(input_file)
        input_file.close()
    except FileNotFoundError:
        inv_dct = {}

    choice = print_menu()

    while choice != PURCHASE:
    # Loop allowing the user to add an itemt to the inventory list, 
    # update the units of an item or delete an item. When the user selects
    # PURCHASE, the loop ends.

        if choice < 1 or choice > 4:
            print("You've entered an invalid option, try again.")
            choice = int(input('Enter a new choice: '))

        if choice == ADD_ITEM_TO_INV:
        # Gathers the description, units and price of an item, creates a 
        # RetailItem oject and adds it to the inv_dct dictionary (key = descr, value = obj)
            try:
                descr = create_descr()
            except ValueError:
                print("Invalid Entry. Please try again.")
                descr = create_descr()
            if descr not in inv_dct:
                units = create_inv_units()
                price = create_price()
                obj = RetailItem.RetailItem(descr, units, price)
                inv_dct[descr] = obj
            else:
                print('This item is already in the inventory.')

        if choice == UPDATE_ITEM_UNITS:
        # Gets the description for the item and calls the set_units method to update
        # the number of units in inventory
            try:
                descr = input("Enter the description of the item you'd like to update: ")
            except ValueError:
                print("Invalid Entry. Please try again.")
                descr = input("Enter the description of the item you'd like to update: ")
            if descr in inv_dct:
                units = int(input("Enter the new amount of units in inventory for this item: "))
                obj = inv_dct[descr]
                obj.set_units(units)
                print('The units in inventory have been updated.')
            else:
                print('This item is not in inventory.')

        if choice == DELTE_ITEM_FROM_INVENTORY:
        # Deletes an item from the inventory list.
            try:
                descr = input("Enter the description of the item you'd like to delete: ")
            except ValueError:
                print("Invalid Entry. Please try again.")
                descr = input("Enter the description of the item you'd like to delete: ")
            if descr in inv_dct:
                del inv_dct[descr]
                print('This item has been deleted from inventory.')
            else:
                print("The item you entered doesn't exist in inventory.")

        choice = print_menu()

    # Display all the items in stock for the user. If units in inventory > 0,
    # the item is printed. 
    print()
    print('Items In Stock')
    print('--------------')

    for key in inv_dct:
        obj = inv_dct[key]
        if obj.get_units() > 0:
            print(key)

    register = CashRegister.CashRegister()

    # Loop promptingg the user to enter the descr of the item they'd like to purhcase,
    # passes the item's value (RetailItem object) as an argument to the CashRegister
    # purchase_item method (adds the item to an internal list and adds its price to a 
    # total accumulator). -1 from units attribute to update the inventory level.
    another_item = 'y'
    while another_item.lower() == 'y':
        item = input("Enter the name of the item you'd like to purchase: ")
        if item in inv_dct:
            obj = inv_dct[item]
            if obj.get_units() > 0:
                selection = inv_dct[item]
                register.purchase_item(selection)
                units = obj.get_units()
                new_units = units - 1
                obj.set_units(new_units)
                
            else:
                print('This item is out of stock. Please select another one.')
        else:
            print('ERROR: This item is not available to purchase.')
        another_item = input("Would you like to purchase another item (Enter y for yes)? ")

    # Prints the items in the register object's internal list.
    print()
    print('Items You Have Selected:')
    print('------------------------')
    register.show_items()

    # Calls the get_total function for the register object for the total amount of 
    # all chosen items. 
    print()
    print('Purchase Total: $', format(register.get_total(), ',.2f'), sep='')

    output_file = open('item_inv.dat', 'wb')
    pickle.dump(inv_dct, output_file)
    output_file.close()

    # Clears the register object's internal list.
    register.clear()

def create_descr():
    descr = input("Enter the item's description: ")
    return descr

def create_inv_units():
    units = int(input("Enter the amount of units on hand of this item: "))
    return units

def create_price():
    price = float(input('Enter the price of the item: '))
    return price

def print_menu():
    print('MENU')
    print('----------')
    print('Add a new item to inventory: 1')
    print('Update the units in inventory of an existing item: 2')
    print('Delete an item from inventory: 3')
    print('Purchase an item/items: 4')
    choice = int(input('Enter your selection from the menu: '))
    return choice

main()

# 7 March 2021
# Starting Out With Python Programming Exercise 8
# In this programming exercise you will create a simple trivia game for two players.
# The program will work like this:
# Starting with player 1, each player gets a turn at answering 5 trivia questions. (There
# should be a total of 10 questions.) When a question is displayed, 4 possible answers are
# also displayed. Only one of the answers is correct, and if the player selects the correct
# answer, he or she earns a point.
# After answers have been selected for all the questions, the program displays the number
# of points earned by each player and declares the player with the highest number of points
# the winner.

# To create this program, write a Question class to hold the data for a trivia question. The
# Question class should have attributes for the following data:
# a trivia question, possible answer 1, possible answer 2, possible answer 3, possible answer 4,
# the number of correct answer (1, 2, 3, or 4)

# The Question class also should have an appropriate __init__ method, accessors, and mutators. 
# The program should have a list or a dictionary containing 10 Question objects, one for each
# trivia question. Make up your own trivia questions on the subject or subjects of your choice
# for the objects.

import Question_Class
import pickle
import random

def main():
    # Attempts to open the question_bank file or creates a new set of 10 questions and 
    # adds them to the question_dct dictionary.
    try:
        input_file = open('question_bank.dat', 'rb')
        question_dct = pickle.load(input_file)
        input_file.close()
    except FileNotFoundError:
        question_dct = {}
        for i in range(10):
            quest = input("Enter the question you'd like to add to the question bank: ")
            A = input('Enter the first possible answer (Option A): ')
            B = input('Enter the second possible answer (Option B): ')
            C = input('Enter the third possible answer (Option C): ')
            D = input('Enter the fourth possible answer (Option D): ')
            correct_ans = input('Enter whether the correct answer is A, B, C or D: ')
            if correct_ans != 'A' and correct_ans != 'B' and correct_ans != 'C' and correct_ans != 'D':
                correct_ans = input("You've entered an invalid response. Please enter either A, B, C, or D: ")
            obj = Question_Class.Question(quest, A, B, C, D, correct_ans)
            question_dct[i] = obj

    # Creates a list of the question_dct. (This allows the program to randomly choose a number and delete
    # the number from the list when displaying the questions.)
    quest_bank = list(question_dct)

    print('Player 1 will answer 5 trivia questions.')

    # Asks player 1 five questions. Adds +1 to the p1_total if the correct answer is given. Removes
    # the number from the quest_bank list.
    p1_total = 0
    for i in range(5):
        num = random.choice(quest_bank)
        p1_total += answer_question(num, question_dct)
        quest_bank.remove(num)
    
    # Asks player 2 five questions. Adds +1 to the p2_total if the correct answer is given. Removes
    # the number from the quest_bank list.
    print()
    print('Player 2 will answer 5 trivia questions.')
    p2_total = 0
    for i in range(5):
        num = random.choice(quest_bank)
        p2_total += answer_question(num, question_dct)
        quest_bank.remove(num)

    # Displays the total correctly answered questions and determines the winner. 
    print()
    print('Player 1 Correctly Answered Questions:', p1_total)
    print('Player 2 Correctly Answered Questions:', p2_total)

    if p1_total > p2_total:
        print('Player 1 Wins!')
    elif p2_total > p1_total:
        print('Player 2 Wins!')
    else:
        print("It's a tie!")

    output_file = open('question_bank.dat', 'wb')
    pickle.dump(question_dct, output_file)
    output_file.close()

def answer_question(num, dct):
# Using the number given, prints the question and possible answers of the respective
# object. Returns 1 if the correct_ans == response and returns 0 if the correct_ans != response.
    obj = dct[num]
    print(obj)
    response = input('Enter your answer: ')
    while response != 'A' and response != 'B' and response != 'C' and response != 'D':
        print('ERROR: You must enter either A, B, C, or D.')
        response = input('Enter your answer: ')
    if obj.get_correct_ans() == response:
        print('Correct!')
        return 1
    else:
        print("That's incorrect.")
        return 0

main()

# The Question class holds data for a triva question: question, possible answers
# (A, B, C, or D), and the correct answer.

class Question:

    def __init__(self, quest, A, B, C, D, correct_ans):
        self.__quest = quest
        self.__A = A
        self.__B = B
        self.__C = C
        self.__D = D
        self.__correct_ans = correct_ans

    def set_quest(self, quest):
        self.__quest = quest

    def set_As(elf, A):
        self.__A = A

    def set_B(self, B):
        self.__B = B

    def set_C(self, C):
        self.__C = C
    
    def set_D(self, D):
        self.__D = D

    def set_correct_ans(self, correct_ans):
        self.__correct_ans = correct_ans

    def get_quest(self):
        return self.__quest

    def get_ans_1(self):
        return self.__A
    
    def get_B(self):
        return self.__B

    def get_C(self):
        return self.__C

    def get_D(self):
        return self.__D

    def get_correct_ans(self):
        return self.__correct_ans

    def __str__(self):
    # Displays the question and possible answers. 
        return '\nQuestion: ' + self.__quest + \
        '\nA: ' + self.__A +  \
        '\nB: ' + self.__B + \
        '\nC: ' + self.__C + \
        '\nD: ' + self.__D