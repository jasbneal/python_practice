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

# 8 January 2021
# Starting Out With Python Functions Exercise 8
# Write a program that receives the square feet of wall space to be painted and the price
# per paint per gallon. Calculate the number of gallons of paint required, hours of labor
# required, cost of the paint, labor charges and total cost of the paint job.
# For every 112 sqft = 1 gallon on paint, 8 hours of labor, $35/hr of labor

MIN_SQFT= 112

MIN_PAINT_GALLON = 1

MIN_LABOR_HOURS = 8

LABOR_HOURLY_RATE = 35

def main():
    sqft = int(input('Enter the square feet of wall space to be painted: '))

    while sqft < 112:
        print('ERROR: Please enter a minimum of 112 square feet of wall space.')
        sqft = int(input('Enter another total of square feet of wall space: '))
        
    gallon_price = float(input('Enter the price per gallon in USD: '))
    paint_gallons_total = calculate_paint(sqft)
    print('Gallons of Paint Required:', format(paint_gallons_total, '.2f'))

    labor_hours_total = labor_hours(sqft)
    print('Hours of Labor Required:', format(labor_hours_total, '.1f'))

    paint_cost = gallon_price * paint_gallons_total
    print('Cost of Paint: $', format(paint_cost, ',.2f'), sep='')
        
    labor_total = labor_charges(sqft)
    print('Labor Charges: $', format(labor_total, ',.2f'), sep='')
              
    grand_total = paint_cost + labor_total
    print('Total Cost of the Job: $', format(grand_total, ',.2f'), sep='')

def calculate_paint(sqft):
    gallons = sqft / MIN_SQFT
    return gallons

def labor_hours(sqft):
    hours = (sqft / MIN_SQFT) * 8
    return hours

def labor_charges(sqft):
    charges = (sqft / MIN_SQFT) * 8 * LABOR_HOURLY_RATE
    return charges

main()

# 8 January 2021
# Starting Out With Python Functions Exercise 9
# Get the sales for the month and display the amount of county, state and total sales tax.
# state tax rate = 5%
# county tax rate = 2.5%

#Global variables for the state and county tax percentages

STATE_TAX_RATE = .05

COUNTY_TAX_RATE = .025

def main():
    #Gets the month's sales and generates the state, county and total taxes for that month
    sales = float(input("Enter this month's sales: "))

    county_tax = calculate_county_tax(sales)
    print("County Sales Tax: $", format(county_tax, ',.2f'), sep='')

    state_tax = calculate_state_tax(sales)
    print("State Sales Tax: $", format(state_tax, ',.2f'), sep='')

    total_tax = county_tax + state_tax
    print("Total Sales Tax: $", format(total_tax, ',.2f'), sep='')

def calculate_county_tax(sales):
    county_tax = sales * COUNTY_TAX_RATE
    return county_tax

def calculate_state_tax(sales):
    state_tax = sales * STATE_TAX_RATE
    return state_tax

main()

# 8 January 2021
# Starting Out With Python Functions Exercise 10
# Write a function named feet_to_inches that accepts a number of feet as an argument and
# returns the number of inches in that many feet. Use the program in a function to convert
# and display feet to inches.

def main():
    #Gets the number of feet and converts it to inches
    feet = int(input('Enter a number of feet: '))
    inches = feet_to_inches(feet)
    print(feet, 'feet =', inches, 'inches')

def feet_to_inches(feet):
    inches = 12 * feet
    return inches

main()

# 8 January 2021
# Starting Out With Python Functions Exercise 11
# Display two random numbers and prompt the user to answer the sum of the number.
# If it's correct, a congratulations message should be displayed. If the answer is incorrect,
# the correct answer should be displayed.

import random

number_1 = random.randint(1, 500)

number_2 = random.randint(1, 500)

correct_total = number_1 + number_2 

print('   ', number_1)
print('+  ', number_2)

total = float(input('Enter the total of the two numbers: '))

if total == correct_total:
    print('CONGRATULATIONS! That is the correct answer!')
else:
    print('The correct answer is', correct_total)

# 9 January 2021
# Starting Out With Python Functions Exercise 12
# Write a function named max that accepts two ineger values as arguments and returns
# the value that is greater of the two. Use the function in a program that prompts
# the user to enter two ineger values and displays the value that is greater
# of the two.

def main():

    #Gets two integers and displays the greater integer of the two
    num1 = int(input('Enter an integer: '))
    num2 = int(input('Enter a different integer: '))
    max_num = max(num1, num2)
    print('The greater integer of the two is', max_num)

def max(num1, num2):

    #Accepts two integers are arguments and returns the value that is greater
    if num1 > num2:
        return num1
    else:
        return num2

main()

# 9 January 2021
# Starting Out With Python Functions Exercise 13
# Write a function named falling_distance that accepts an object's falling time
# in seconds as an argument and returns the distance the object has falled. Write
# a program that calls the function in a loop that passes the values 1-10 as
# arguments and displays the return value.
# distance = (1/2)g(t ** 2) where g=9.8

print('Seconds\t\tDistance (in meters)')
print('-------\t\t--------------------')

def main():
    for seconds in range(1, 11):
        distance = falling_distance(seconds)
        print(seconds, '\t\t', format(distance, ',.1f'))

def falling_distance(seconds):
    d = (1/2) * 9.8 * (seconds ** 2)
    return d

main()

# 9 January 2021
# Starting Out With Python Functions Exercise 14
# Write a function named kinetic_energy that accepts an object's mass and velocity
# as arguments. The function should return the KE of the object. Write a program
# that asks the user to enter values for mass and velocity, calls the kinetic_energy
# function and displays the object's KE.
# KE = (1/2) * mass * (velocity ** 2)

def main():
    #Gets the mass and velocity of an object to display it's KE
    mass = float(input('Enter the mass (in kilograms) of an object: '))
    velocity = float(input("Enter the object's velocity (in meters/second): "))
    KE = kinetic_energy(mass, velocity)
    print('KE =', format(KE, ',.1f'))

def kinetic_energy(mass, velocity):
    KE = (1/2) * mass * (velocity ** 2)
    return KE

main()

# 9 January 2021
# Starting Out With Python Functions Exercise 15
# Write a program that asks the user for five test scores and eisplays a letter
# grade for each test score and average test score. It should have a calc_average
# function and a determine_grade function.

#Global variable to determine total number of test scores
TOTAL_TESTS = 5

def main():
    score1 = int(input('Enter your first test score: '))
    score2 = int(input('Enter your second test score: '))
    score3 = int(input('Enter your third test score: '))
    score4 = int(input('Enter your fourth test score: '))
    score5 = int(input('Enter your fifth test score: '))

    print('\n')
    
    print('Test Score\tGrade')
    print('----------\t-------')

    for score in [score1, score2, score3, score4, score5]:
        grade = determine_grade(score)
        print(score, '\t\t', grade)

    average = calc_average(score1, score2, score3, score4, score5)
    print('\n')
    print('Your test score average: ', average)

def calc_average(score1, score2, score3, score4, score5):
    average = (score1 + score2 + score3 + score4 + score5) / TOTAL_TESTS
    return average

def determine_grade(score):
    if score >= 90 and score <= 100:
        grade = 'A'
    elif score >= 80 and score <= 89:
        grade = 'B'
    elif score >= 70 and score <= 79:
        grade = 'C'
    elif score >= 60 and score <= 69:
        grade = 'D'
    else:
        grade = 'F'
    return grade

main()

# 9 January 2021
# Starting Out With Python Functions Exercise 16
# Write a program that generates 100 random numbers and keeps a count of how many
# of those random numbers are even and how many of them are odd.

import random

even_total = 0.0
odd_total = 0.0

print('No.\tValue')
print('---\t-----')

for number in range(1, 101):
    value = random.randint(1, 10000)
    print(number, '\t', value)
    if (value % 2) == 0:
        even_total += 1
    else:
        odd_total += 1

print('\n')
print('Even Numbers in the List:', format(even_total, '.0f'))
print('Odd Numbers in the List:', format(odd_total, '.0f'))
