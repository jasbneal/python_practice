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

# 3 February 2021
# Starting Out With Python Exercise 5
# Write a program that reads the contents of the charge_accounts.txt file into a
# list. The program should then ask the user to enter a charge account number.
# The program should determine whether the number is valid by searching for it
# in the list. If the number is in the list, the program will display a message
# indicating the number is valid. If the number is not in the list, the program
# should display a message indicating the number is invalid.

charge_accounts_list = []

infile = open('charge_accounts.txt', 'r')

search = int(input('Enter a charge account number: '))

line = infile.readline()

while line != '':
    line = int(line.rstrip('\n'))
    charge_accounts_list.append(line)
    line = infile.readline()

infile.close()

if search in charge_accounts_list:
    print('The number is valid.')
else:
    print('The number is invalid.')

# 3 February 2021
# Starting Out With Python Exercise 6
# In a program, write a function that accepts two arguments: a list, and a number
# n. Assume that the list contains numbers. The function should display all of
# the numbers in the list that are greater than the number n.

def main():
    # Gets the value of n and creates a number list
    n = int(input('Enter a number: '))

    number_list = [1, 20, 300, 4000, 50000, 600000, 7000000]

    print('Numbers Greater Than', n)
    print('--------------------------')

    greater_than(number_list, n)

def greater_than(list_name, n):
    # Function to display all numbers greater than n from the given list
    for i in list_name:
        if i > n:
            print(i)

main()

# 3 February 2021
# Starting Out With Python Exercise 7
# The local driver's license office has asked you to create an application that grades
# the written portion of the driver's license exam. The exam has 20 multiple-choice
# questions. Here are the correct answers: 1.A, 2.C, 3.A, 4.A, 5.D, 6.B, 7.C, 8.A,
# 9.C, 10.B, 11.A, 12.D, 13.C, 14.A, 15.D, 16.C, 17.B, 18.B, 19.D, 20.A
# Your progarm should store these correct answers in a list and read the student's
# answers for each of the 20 questions from a text file store the answers in another
# list. After the student's answers have been read from the file, the program should
# display a message indicating whether the student passed or failed the exam (15+/20 to
# pass). It should then display the total number of correctly answers questions,
# the total number of incorrectly answered questions and a list showing the question
# numbers of the incorrectly answered questions.

answer_sheet = ['A', 'C', 'A', 'A', 'D', 'B', 'C', 'A', 'C', 'B', 'A', 'D', 'C', 'A', 'D', 'C','B', 'B', 'D', 'A']

# Read contents of student_answers file and adds them to student_answers list.
infile = open('student_answers.txt', 'r')

student_answers = []

for line in infile:
    answer = line.rstrip('\n')
    student_answers.append(answer)

infile.close()

index = 0
total_correct = 0
total_incorrect = 0

incorrect_answer_numbers = []

# Loop evaluates the correct answers and adds the incorrect question numbers to a list.
for i in range(20):
    if answer_sheet[index] == student_answers[index]:
        total_correct += 1
    else:
        total_incorrect += 1
        incorrect_answer_numbers.append(index + 1)
    index += 1

# Determine if the student passed or failed
if total_correct >= 15:
    print('PASSED')
else:
    print('FAILED')

print('Correctly Answered Questions:', total_correct)
print('Incorrectly Answered Questions:', total_incorrect)
print()

print('Incorrectly Answered Question Numbers:')
for i in incorrect_answer_numbers:
    print(i)

# 3 February 2021
# Starting Out With Python Exercise 8
# Write a program that reads the contents of the GirlNames.txt and BoyNames.txt
# files into two separate lists. The user should be able to enter a boy's name,
# a girl's name, or both, and the application will display messages indicating
# whether the names were among the most popular.

girls_names = []
boys_names = []

infile_girls = open('GirlNames.txt', 'r')

for line in infile_girls:
    name = line.rstrip('\n')
    girls_names.append(name)

infile_girls.close()

infile_boys = open('BoyNames.txt', 'r')

for line in infile_boys:
    name = line.rstrip('\n')
    boys_names.append(name)

infile_boys.close()

search = input('Enter a name: ')

if search in girls_names:
    print(search, 'is among the most popular girl names.')

if search in boys_names:
    print(search, 'is amoung the most popular boy names.')

if search not in girls_names and search not in boys_names:
    print(search, 'is not a popular name for boys or girls.')

# 4 February 2021
# Starting Out With Python Exercise 9
# Write a program that reads the USPopulation.txt file's contents into a list. The first
# number is for the year 1950. The program should display the following data:
# average annual change in population during that time period, year with the
# greatest increase in population during the time period, year with the smallest
# increase in population during the time period.

US_population = []
population_increase = []

# Opens the USPopulation.txt file and writes the contents into the US_population list.
infile = open('USPopulation.txt', 'r')

for line in infile:
    population = int(line.rstrip('\n'))
    US_population.append(population)

infile.close()

# Calculates the population difference for each year range, puts the difference into
# the population_increase list and adds them to the total accumulator. 
index = 0
total = 0
for i in range(len(US_population) - 1):
    population_change = US_population[index + 1] - US_population[index]
    total += population_change
    population_increase.append(population_change)
    index += 1

# Calculates the average change in population
average_change = total / len(population_increase)
print('Average Annual Change in Population:', format(average_change, ',.2f'))

# Calculates the year range with the lowest increase in population
min_index = population_increase.index(min(population_increase))
min_Year1 = min_index + 1950
print('Years with the lowest increase in population:', min_Year1, '-', min_Year1 + 1)

# Calculates the year range with the highest increase in population
max_index = population_increase.index(max(population_increase))
max_Year1 = max_index + 1950
print('Years with the highest increase in population:', max_Year1, '-', max_Year1 + 1)

# 4 February 2021
# Starting Out With Python Exercise 10
# The WorldSeriesWinners.txt file contains a hronological list of the World Series
# winning teams from 1903 through 2009. (The first line in the file is the name of the
# team that won in 1903, and the last line is the name of the team that won in 2009.
# Note that the World Series was not played in 1904 or 1994. Write a program that lets
# the user enter the name a team and then display the number of times that team has won
# the World Series in the time period from 1903 through 2009.

WorldSeriesWinners = []

# Reads the contents of the WorldSeriesWinner file and puts it into the
# WorldSeriesWinners list
infile = open('WorldSeriesWinners.txt', 'r')

for line in infile:
    team = line.rstrip('\n')
    WorldSeriesWinners.append(team)

infile.close()

# Gets the name from the user and uses a loop to calculate how often the name
# appears in the WorldSeries list
search = input('Enter the name of a team: ')

total_wins = 0
for name in WorldSeriesWinners:
    if name == search:
        total_wins += 1

print(search, 'Wins:', total_wins)

# 4 February 2021
# Starting Out With Python Exercise 11
# The Lo Shu Magic Square is a grid with 3 rows and 3 columns. The Lo Shu Magic Square has
# the following properties: the grid contains the numbers 1 through 9 exactly, the sum
# of each row, each column and each diagonal all add up to the same number. In a program
# you can simulate a magic square using a two-dimensional list. Write a function that
# accepts a two-dimensional list as an argument and determines whether the list is a Lo
# Shu Magic Square. Test the function in a program.
        
def main():
    # Creates a lo_shu list and gathers the numbers via loop from the user to create a magic square
    lo_shu = [[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]

    for r in range(3):
        for c in range(3):
            lo_shu[r][c] = int(input('Enter a number: '))

    determine_lo_shu(lo_shu)

def determine_lo_shu(list_name):
    # Calculates the different sum options for rows, columns and diagonals
    sum1 = list_name[0][0] + list_name[0][1] + list_name[0][2]
    sum2 = list_name[1][0] + list_name[1][1] + list_name[1][2]
    sum3 = list_name[2][0] + list_name[2][1] + list_name[2][2]
    sum4 = list_name[0][0] + list_name[1][0] + list_name[2][0]
    sum5 = list_name[0][1] + list_name[1][1] + list_name[2][1]
    sum6 = list_name[0][2] + list_name[1][2] + list_name[2][2]
    sum7 = list_name[0][0] + list_name[1][1] + list_name[2][2]
    sum8 = list_name[2][0] + list_name[1][1] + list_name[0][2]

    if sum1 == 15 and sum2 == 15 and sum3 == 15 and sum4 == 15 and sum5 == 15 and sum6 == 15 and sum7 == 15 and sum8 == 15:
        print('Congratulations! This is a Lo Shu Magic Square!')
    else:
        print('This is not a Lo Shu Magic Square.')

main()
