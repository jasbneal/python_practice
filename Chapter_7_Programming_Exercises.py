# 26 January 2021
# Given an array of integers, return how many of them are even numbers.

import random

# Global Variable to determine list size and test efficiency. 
LIST_LENGTH = 20

numbers = [0] * LIST_LENGTH

index = 0

# Assigns each element in the list a random number)
while index < len(numbers):
    for i in range(len(numbers)):
        numbers[index] = random.randint(1, 999999)
        index += 1

print(numbers)

even_num_total = 0

# Determines if each number in the list is even and adds 1 to the
# even_num_total accumulator
for num in numbers:
    if num % 2 == 0:
        even_num_total += 1

print('Even numbers in this list:', even_num_total)
        
# 27 January 2021
# Given an array of integers, return how many of them are even number of digits.

import random

# Global Variable to determine list size and test efficiency. 
LIST_LENGTH = 500

numbers = [0] * LIST_LENGTH

index = 0

# Assigns each element in the list a random number)
while index < len(numbers):
    for i in range(len(numbers)):
        numbers[index] = random.randint(1, 999999)
        index += 1

print(numbers)

even_num_total = 0

# Determines if each number in the list has an even amount of numbers and
# adds 1 to the even_num_total accumulator

for num in numbers:
    if num >= 10 and num <= 99:
        even_num_total += 1
    elif num >= 1000 and num <= 9999:
        even_num_total += 1
    elif num >= 100000 and num <= 999999:
        even_num_total += 1
    else:
        even_num_total += 0

print('Even numbers in this list:', even_num_total)

# 2 February 2021
# Starting Out With Python Exercise 1
# Design a program that asks the user to enter a store's sales for each day of the week.
# The amounts should be stored in a list. Use a loop to calculate the total sales for
# the week and display the result.

# Global variable to control the items in the sales_list
DAYS = 7

sales_list = [0] * DAYS

index = 0
total_sales = 0

# Loop to receive the store's sales for each day.
for i in range(DAYS):
    sales_list[index] = int(input('Enter store sales: '))
    index += 1

# Loop to calculate the week's total sales. 
for i in sales_list:
    total_sales += i

print('Total Sales for the Week = $', format(total_sales, ',.2f'), sep='')
        
# 2 February 2021
# Starting Out With Python Exercise 2
# Design a program that generates a seven-digit lottery number. Thie program should
# generate seven random numbers, each in the range of 0 through 9, and assign each
# number to a list element. Then write another loop that displays the contents
# of the list.

import random

numbers = [0] * 7

index = 0

for i in numbers:
    numbers[index] = random.randint(0, 10)
    index += 1

for i in numbers:
    print(i)

# 2 February 2021
# Starting Out With Python Exercise 3
# Design a program that lets the user enter the total rainfall for each of 12 months into
# a list. The program should calculate and display the total rainfall for the year, the
# average monthly rainfall, and the months with the highest and lowest amounts.

def main():
    rainfall_list = get_rainfall()
    total_rainfall = calculate_total_rainfall(rainfall_list)
    print('Total Rainfall:', total_rainfall)
    average_rainfall = calculate_average_rainfall(total_rainfall)
    print('Average Rainfall Per Month:', average_rainfall)
    lowest_rainfall = calculate_lowest_rainfall(rainfall_list)
    print('Lowest Monthly Rainfall:', lowest_rainfall)
    highest_rainfall = calculate_highest_rainfall(rainfall_list)
    print('Highest Monthly Rainfall:', highest_rainfall)

def get_rainfall():
    # Gets each month's rainfall and stores it in the rainfall list
    rainfall_list = [0] * 12
    index = 0
    for i in range(12):
        rainfall_list[index] = int(input("Enter a month's total rainfall: "))
        index += 1
    return rainfall_list

def calculate_total_rainfall(list):
    # Calculates the total rainfall
    total = 0
    for i in list:
        total += i
    return total

def calculate_average_rainfall(total):
    # Calculates the average rainfall
    average = total / 12
    return average

def calculate_lowest_rainfall(list):
    # Displays the lowest monthly rainfall
    return min(list)

def calculate_highest_rainfall(list):
    # Displays the highest monthly rainfall
    return max(list)
    
main()

# 2 February 2021
# Starting Out With Python Exercise 4
# Design a program that asks the user to enter a series of 20 numbers. The program should
# store the numbers in a list and then display the following data: lowest number in
# the list, highest number in the list, total of the numbers in the list, average
# of the numbers in the list

LIST_LENGTH = 20

def main():
    numbers = numbers_list()
    print('Lowest Number in the List:', min(numbers))
    print('Highest Number in the List:', max(numbers))
    numbers_total = calculate_list_total(numbers)
    print('Total of the Numbers in the List:', numbers_total)
    print('Average of the Numbers in the List:', numbers_total / LIST_LENGTH)

def numbers_list():
    # Gets a series of 20 numbers from the user
    numbers_list = [0] * LIST_LENGTH
    index = 0
    for i in range(LIST_LENGTH):
        numbers_list[index] = int(input("Enter a number: "))
        index += 1
    return numbers_list

def calculate_list_total(list):
    # Calculates the total of the numbers in a list
    total = 0
    for i in list:
        total += i
    return total
    
main() 
