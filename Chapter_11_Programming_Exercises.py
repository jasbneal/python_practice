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
