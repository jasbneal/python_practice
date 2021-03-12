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

    def __str__(self):
        return '\nName: ' + self.get_name() + \
            '\nNumber: ' + str(self.get_num()) + \
            '\nShift: ' + str(self.__shift) + \
            '\nPay: $' + str(format(self.__pay, ',.2f'))

name = input("Enter the production worker's first and last name: ")
num = int(input("Enter the production worker's employee number: "))
shift = int(input("Enter the production worker's shift (day shift = 1 and night shift = 2): "))
pay = float(input("Enter the production worker's hourly pay rate: "))

worker = ProductionWorker(name, num, shift, pay)
print()
print("This is the information you've entered:")
print(worker)