#Write a program which will find all such numbers which are divisible by 7
#but are not a multiple of 5, between 2000 and 3200 (both included).
#The numbers obtained should be printed in a comma-separated sequence on a single line.

for number in range(2000, 3201):
    if (number % 7) == 0 and (number % 5) != 0:
        print(number, ',', end='')

#Exercise 14 (Chpt. 4 Starting Out With Python)
#Loop that prints the following design:
##
# #
#  #
#   #
#    #
#     #

for row in range(6):
    print('#', end='')
    for column in range(row):
        print(' ', end='')
    print('#')

#28 November 2020
#Print the following pattern (without # signs):

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

#Version 1 using if-statement to determine how many times to print the number.

for row in range(5):
    for column in range(5):
        if column <= row: #Only prints the number in the column if less than or equal to the row
            print(column + 1, ' ', end='')
    print()

print()

#Version 2 using range() function to determine how many times to print the number.

for row in range(1, 6):
    for column in range(1, row + 1):
        print(column, ' ', end='')
    print()

# 28 November 2020
#Accept number from user and calculate the sum of all number between 1 and given number.

number_total = 0.0

number = int(input('Enter a number: '))

for i in range(1, number + 1):
    number_total += i

print('The total of all numbers between 1 and', number, 'is', number_total)

#28 November 2020
#Print the multiplication table of a given number

number = int(input('Enter a number: '))

print('\n')

print('Multiplier\tResult')
print('----------------------')

for i in range(1, 13):
    print(i, '\t\t', i * number)

#28 November 2020
#Print the following patter (without # signs):

#5 4 3 2 1
#4 3 2 1
#3 2 1
#2 1
#1

for row in range(1, 6):
    for column in range(6 - row, 0, -1):
        print(column, ' ', end='')
    print()

#28 November 2020
#Print the following pattern (w/o # sign):

# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * * 
# * 

for row in range(1, 6):
    for column in range(row):
        print('*', ' ', end='')
    print()

for row in range(1, 5):
    for column in range(5 - row):
        print('*', ' ', end='')
    print()

#28 November 2020
#Print the following pattern (w/o # sign):

# *

# * *

# * * *

# * * * *

# * * * * *

# * * * *

# * * *

# * *

# * 

for row in range(0, 5):
    for column in range(0, row + 1):
        print('*', ' ', end='')
    print('\n')

for row in range(5, 0, -1):
    for column in range(0, row - 1):
        print('*', ' ', end='')
    print('\n')

# 1 December 2020
# Create a loop that sums the numbers from 100 to 200.

total = 0.0

for i in range(100, 201):
    total += i

print('The sum of all numbers from 100 to 200 is', format(total, ',.0f'))

# 1 December 2020
# Create a loop that counts all even numbers to 10.

for i in range(0, 11, 2):
    print(i)

# 1 December 2020
# Practice Python Character Input Exercise
# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them which year they will
# turn 100 years old.

def main():
    age_100()

def age_100():
    first_name = input('Enter your first name: ')
    age = int(input('Enter your age: '))
    current_year = int(input('What year is it? '))
    age_100 = (100 - age) + current_year
    print(first_name, 'you will turn 100 in the year', age_100)

main()

# 5 January 2021
# Starting Out With Python Functions Exercise 1
# Write a program that asks the user to enter a distance in kilometers,
# and then converts that distance to miles. The conversion formula is as follows:
# Miles = Kilometers x 0.6214

def main():
    kilometers = float(input('Enter a distance in kilometers: '))
    print(miles_conversion(kilometers))

# miles_conversion function calculates miles based on the kilometers argument

def miles_conversion(kilometers):
    miles = kilometers * .6214
    return format(miles, ',.2f')

main()

# 5 January 2021
# Starting Out With Python Functions Exercise 2
# Write a program that will ask the user to enter the amount of a purchase. The program
# should then compute the state and county sales tax. Assume the state sales tax is 5 percent
# and the county sales tax is 2.5 percent. The program should display the amount of the
# purchase, the state sales tax, the county sales tax, the total sales tax, and the total
# of the sale (purchase amount + total sales tax)

STATE_SALES_TAX = .05

COUNTY_SALES_TAX = .025

# Takes the sales tax, county tax, total tax and sale total functions to display the total
# purchase data to the user

def main():
    purchase = int(input('Enter the amount of the purchase: '))
    print('Here are the details of your purchase: ')
    print('Purchase Amount: $', format(purchase, ',.2f'), sep='')
    print('State Sales Tax Amount $', format(sales_tax_calculation(purchase), ',.2f'), sep='')
    print('State County Tax Amount $', format(county_tax_calculation(purchase), ',.2f'), sep='')
    print('Total Tax Amount $', format(total_tax_calculation(purchase), ',.2f'), sep='') 
    print('Total of Sale $', format(sale_total(purchase), ',.2f'), sep='')

# sales_tax_calculation function alculates the sales tax using the
# STATE_SALES_TAX global variable

def sales_tax_calculation(purchase):
    return purchase * STATE_SALES_TAX

# county_tax_calculation function calculates the sales tax using the
# COUNTY_SALES_TAX global variable

def county_tax_calculation(purchase):
    return purchase * COUNTY_SALES_TAX

# total_tax_calculation function calculates the total sales tax using the
# COUNTY_SALES_TAX and STATE_SALES_TAX global variables

def total_tax_calculation(purchase):
    total = (purchase * STATE_SALES_TAX) + (purchase * COUNTY_SALES_TAX)
    return total

# sale_total function calculates the total of the sale using the
# total_tax_calculation function and purchase price

def sale_total(purchase):
    total = purchase + total_tax_calculation(purchase)
    return total
    
main()

# 5 January 2021
# Starting Out With Python Functions Exercise 3
# Many financial experts advise that property owners should insure their homes or buildings
# for at least 80% of the amount it would cost to replace the structure. Write a program
# that asks the user to enter the replacement cost of a building and then displays the
# minimum amount of insurance he or she should buy for the property

INSURANCE_MINIMUM = .80

def main():
    cost = float(input('Enter the replacement cost of the building: ')) 
    print('The minimum amount of insurance you should buy for the property is $', end='')
    print(format(insurance_amount(cost), ',.2f'))

# insurance_amount function calculates the minimum insurance using the INSURANCE_MINIMUM
# global variable 

def insurance_amount(cost):
    minimum = cost * INSURANCE_MINIMUM
    return minimum

main()

# 6 January 2021
# Starting Out With Python Functions Exercise 4
# Write a program that asks the user to enter the monthly costs for the following expenses incurred
# from operating his or her automobile: loan payment, insurance, gas, oil, tires, and
# maintenance. The program should then display the total monthly cost of these expenses, and the total
#annual cost of these expenses.

def main():
    # Get the monthly costs of all car expenses and adds them for a monthly and yearly total
    loan_payment = get_loan_payment()
    insurance = get_insurance()
    gas = get_gas()
    oil = get_oil()
    tires = get_tires()
    maintenance = get_maintenance()
    monthly_total = loan_payment + insurance + gas + oil + tires + maintenance
    annual_total = 12 * monthly_total
    print('The monthly cost of your car expenses is $', format(monthly_total, ',.2f'), sep='')
    print('The annual cost of your car expenses is $', format(annual_total, ',.2f'), sep='')

def get_loan_payment():
    loan = float(input('Enter the monthly cost of your car loan payment: '))
    return loan

def get_insurance():
    insurance = float(input('Enter the monthly cost of your car insurance: '))
    return insurance

def get_gas():
    gas = float(input('Enter the monthly cost of gas: '))
    return gas

def get_oil():
    oil = float(input('Enter the monthly cost of oil: '))
    return oil

def get_tires():
    tires = float(input('Enter the monthly cost of tires: '))
    return tires

def get_maintenance():
    maintenance = float(input('Enter the monthly cost of maintenance: '))
    return maintenance

main()
    
# 6 January 2021
# Starting Out With Python Functions Exercise 5
# Write a program that gets the actual value of a property and caclulates and displays it's
# assessment value (60% of actual value) and property tax ($0.72 of $100 of assessment value)

ASSESSMENT_PERCENTAGE = .6

PROPERTY_TAX_PERCENTAGE = .0072

def main():
    # gathers the actual value to calculate the assessment value and property tax of a property
    assessment = calculate_assessment_value()
    property_tax = assessment * PROPERTY_TAX_PERCENTAGE
    print('Assessment Value: $', format(assessment, ',.2f'), sep='')
    print('Property Tax: $', format(property_tax, ',.2f'), sep='')

def calculate_assessment_value():
    actual_val = float(input('Enter the actual value of the property: '))
    assessment_val = actual_val * ASSESSMENT_PERCENTAGE
    return assessment_val
 
main()

# 6 January 2021
# Starting Out With Python Functions Exercise 6
# Get the fat grams and carbs grams from the user, calculate the calories from fat and the calories
# from carbs and display the results.

def main():
    fat_calories = calculate_fat_calories()
    carb_calories = calculate_carbs_calories()
    total_calories = fat_calories + carb_calories
    print("Calories From Fat:", format(fat_calories, ',.2f'))
    print("Calories From Carbs:", format(carb_calories, ',.2f'))
    print("Total Calories:", format(total_calories, ',.2f'))

def calculate_fat_calories():
    fat = float(input("Enter the amount of fat grams you've consumed in a day: "))
    calories = fat * 9
    return calories

def calculate_carbs_calories():
    carbs = float(input("Enter the amount of carbs grams you've consumed in a day: "))
    calories = carbs * 4
    return calories

main()

# 7 January 2021
# Starting Out With Python Functions Exercise 7
# Collect the amount of tickets sold for Class A ($20), Class B ($15) and Class C (10)
# Display the total income generated from ticket sales

A_TICKET_COST = 20

B_TICKET_COST = 15

C_TICKET_COST = 10

def main():
    a_tickets = calculate_a_tickets()
    b_tickets = calculate_b_tickets()
    c_tickets = calculate_c_tickets()
    total_tickets = a_tickets + b_tickets + c_tickets
    print('The total revenue from ticket sales is $', format(total_tickets, ',.2f'), sep='')

def calculate_a_tickets():
    ticket = int(input('How many Class A tickets were sold? '))
    total = ticket * A_TICKET_COST
    return total

def calculate_b_tickets():
    ticket = int(input('How many Class B tickets were sold? '))
    total = ticket * B_TICKET_COST
    return total

def calculate_c_tickets():
    ticket = int(input('How many Class C tickets were sold? '))
    total = ticket * C_TICKET_COST
    return total

main()
