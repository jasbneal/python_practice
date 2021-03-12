# 10 March 2021
# Starting Out With Python Programming Exercise 1
# Write an Employee class that keeps data attributes for the following pieces of information:
# Employee name
# Employee number
# Next, write a class named ProductionWorker that is a subclass of the Employee class. The 
# ProductionWorker class should keep data attributes for the following information:
# Shift number (an integer, such as 1, 2, or 3)
# Hourly pay rate
# The workday is divided into two shifts: day and night. The shift attribute will hold an
# integer value representing the shift that the employee works. The day shift is 1 and the night
# shift is 2. Write the appropriate accessor and mutator methods for each class.
# Once you have written the classes, write a program that creates an object of the ProductionWorker
# class and prompts the user to enter data for each of the object's data attributes. Store the data
# in the object and then use the object's accessor methods to retrieve it and display it on the screen.

# Employee class stores the employee's name and employee number.
class Employee():
    def __init__(self, name, num):
        self.__name = name
        self.__num = num
    
    def set_name(self, name):
        self.__name = name

    def set_num(self, num):
        self.__num = num

    def get_name(self):
        return self.__name

    def get_num(self):
        return self.__num

# ProductionWorker class is an Employee subclass and stores the employee shift and pay.
class ProductionWorker(Employee):
    def __init__(self, name, num, shift, pay):
        Employee.__init__(self, name, num)
        self.__shift = shift
        self.__pay = pay

    def set_shift(self, shift):
        self.__shift = shift

    def set_pay(self, pay):
        self.__pay = pay

    def get_shift(self):
        return self.__shift

    def get_pay(self):
        return self.__pay

    # Returns the employee's name, employee number, shift and pay.
    def __str__(self):
        return '\nName: ' + self.get_name() + \
            '\nEmployee Number: ' + str(self.get_num()) + \
            '\nShift: ' + str(self.__shift) + \
            '\nPay: $' + str(format(self.__pay, ',.2f'))

# Gets the employee name, employee number, shift and pay from the user.
name = input("Enter the production worker's first and last name: ")
num = int(input("Enter the production worker's employee number: "))
shift = int(input("Enter the production worker's shift (day shift = 1 and night shift = 2): "))
# Loop prompting the user to enter a valid shift number if input < 1 or > 2.
while shift < 1 or shift > 2:
    print('ERROR: You must enter either 1 or 2')
    shift = int(input("Try Again. Enter the production worker's shift (day shift = 1 and night shift = 2): "))
pay = float(input("Enter the production worker's hourly pay rate: "))

# Print employee info V1 by calling the object's str method. 
worker = ProductionWorker(name, num, shift, pay)
print()
print("This is the information you've entered:")
print(worker)

# Print employee info V2 by calling the accessor methods for the object.
print()
print("This is the information you've entered:")
print('Name:', worker.get_name())
print('Employee Number:', worker.get_num())
print('Shift:', worker.get_shift())
print('Pay: $', format(worker.get_pay(), ',.2f'), sep='')

# 11 March 2021
# Starting Out With Python Exercise 2
# In a particular factory, a shift supervisor is a salaried employee who supervises a shift. In
# addition to a salary, the shift supervisor earns a yearly bonus when his or her shift meets
# production goals. Write a ShiftSupervisor class that is a subclass of the Employee class you
# created in Programming Exercise 1. The ShiftSupervisor class should keep a data attribute for 
# the annual salary and a data attribute for the annual production bonus that a shift supervisor
# has earned. Demonstrate the class by writing a program that uses a ShiftSupervisor object.

# Employee class stores the employee's name and employee number.
class Employee():
    def __init__(self, name, num):
        self.__name = name
        self.__num = num
    
    def set_name(self, name):
        self.__name = name

    def set_num(self, num):
        self.__num = num

    def get_name(self):
        return self.__name

    def get_num(self):
        return self.__num

# ShiftSupervisor is a subclass of the Employee superclass and stores a shift supervisor's
# name, num, salary, and bonus.
class ShiftSupervisor(Employee):
    def __init__(self, name, num, salary, bonus):
        Employee.__init__(self, name, num)
        self.__salary = salary
        self.__bonus = bonus

    def set_salary(self, salary):
        self.__salary = salary

    def set_bonus(self, bonus):
        self.__bonus = bonus

    def get_salary(self):
        return self.__salary

    def get_bonus(self):
        return self.__bonus

    # The total_pay method = salary + bonus.
    def total_pay(self):
        return (self.__salary + self.__bonus)

    # Returns the emoloyee's name, employee number, salary bonus and annual pay.
    def __str__(self):
        return '\nName: ' + self.get_name() + \
            '\nEmployee Number: ' + str(self.get_num()) + \
            '\nSalary: $' + str(format(self.__salary, ',.2f')) + \
            '\nBonus: $' + str(format(self.__bonus, ',.2f')) + \
            '\nTotal Annual Pay: $' + str(format(self.total_pay(), ',.2f'))

# Gathers the name, employee number and salary from the user.
name = input("Enter the shift supervisor's first and last name: ")
num = int(input("Enter the shift supervisor's employee number: "))
salary = int(input("Enter the shift supervisor's salary: "))

# Gathers the annual production goal and the actual amount of units produced.
production_goal = int(input("Enter the annual production goal (in units): "))
production_actual = int(input("Enter the actual amount of units produced for the year: "))

# Compares the production goal with the actual amount of units sold. If actual >= goal, gathers the 
# annual bonus and calls the class's str method. If actual < goal, bonus = 0 and calls the class's str method.
if production_goal <= production_actual:
    production_goal_met = True
    bonus = int(input("Enter the shift supervisor's annual production bonus: "))
else:
    production_goal_met = False
    bonus = 0
    print('The supervisor did not meet the production goal and will not earn a production bonus.')
supervisor = ShiftSupervisor(name, num, salary, bonus)
print(supervisor)

# 12 March 2021
# Starting Out With Python Exercise 3
# Write a class named Person with data attributes for a person's name, address, and 
# telephone number. Next, write a class name Customer that is a subclass of the Person
# class. The Customer class should have a data attribute for a customer and a Boolean
# data attribute indicating whether the customer wishes to be on a mailing list. Demonstrate
# an instance of the Customer class in a simple program.

# Person class stores the user's name, address and telephone number.
class Person():

    def __init__(self, name, address, tel):
        self.__name = name
        self.__address = address
        self.__tel = tel

    def set_name(self, name):
        self.__name = name

    def set_address(self, address):
        self.__address = address

    def set_tel(self, tel):
        self.__tel = tel

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_tel(self):
        return self.__tel

# Customer is a sublcass of the Person super class and stores whether the users
# wants to be added to the mailing list. 
class Customer(Person):

    def __init__(self, name, address, tel):
        Person.__init__(self, name, address, tel)
        self.__mailing_list = False

    def yes_mailing_list(self):
        self.__mailing_list = True
        return self.__mailing_list

    def no_mailing_list(self):
        self.__mailing_list = False
        return self.__mailing_list

mailing_list_dct = {}

# Gather the name, address and telephone number of the user.
name = input("Enter your full name: ")
address = input("Enter your address (street, city, state, zip code): ")
tel = int(input("Enter your telephone number with no spaces, parentheses or dashes: "))

# Gather whether the user wants to be added to the mailing list. While loop to ensure the input is 
# either y or n.
mailing_list = input('Would you like to be added to the mailing list? (Enter y for yes or n for no.): ' )
while mailing_list.lower() != 'y' and mailing_list.lower() != 'n':
    print('ERROR: You must enter either y or no. Try Again')
    mailing_list = input('Would you like to be added to the mailing list? (Enter y for yes or n for no.):' )

# Creates a customer object, sets the mailing_list method to True and adds the user name and address to 
# the mailing_list_dct if the response is y and sets the mailing_list method to False if the response is n.
user = Customer(name, address, tel)
if mailing_list.lower() == 'y':
    user.yes_mailing_list()
    mailing_list_dct[name] = user.get_address()
    print('You have been added to the mailing list.')
else:
    user.no_mailing_list()
    print('You have not been added to the mailing list.')
