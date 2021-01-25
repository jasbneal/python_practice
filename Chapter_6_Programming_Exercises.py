# 18 January 2021
# Create a function that returns the factorial of any number you give it.

def main():
    
    number = int(input('Enter a number between 1 and 1000: '))
    print(number, '! = ', determine_factorial(number), sep='')


def determine_factorial(number):
    # Determines the factorial of a number and keeps a running total
    total = 1.0
    for number in range(number, 0, -1):
        total = total * number
    return total

main()

# 24 January 2021
# Starting Out With Python Algorithm Workbench #1
# Write a program that opens an output file with the filename my_name.txt,
# writes your name to the file, and then close the file.

name_file = open('my_name.txt', 'w')

name = input('Enter your name: ')

name_file.write(name + '\n')

name_file.close()

print('The name', name, 'has been saved to the my_name file.')

# 24 January 2021
# Starting Out With Python Algorithm Workbench #2
# Write a program that opens the my_name.txt files that was created in question #1,
# reads your name from the file, displays the name ont he screen, and then
# closes the file. 

name_file = open('my_name.txt', 'r')

name = name_file.read()
name = name.rstrip('\n')

print(name)

name_file.close()

# 24 January 2021
# Starting Out With Python Workbench #3
# Write code that does the following: opens an output file with the filename
# number_list.txt, uses a loop to write the numbers 1 through 100 to the file, and
# then closes the file.

numbers_file = open('number_list.txt', 'w')

for num in range(1, 101):
    numbers_file.write(str(num) +'\n')

numbers_file.close()

print('Numbers 1-100 have been written to the number_list file.')

# 24 January 2021
# Starting Out With Python Workbench #4
# Write code that does the following: opens the number_list.txt file that was
# created by the code you wrote in question 3, reads all the numbers from the file
# and displays them, and then closes the file.

numbers_file = open('number_list.txt', 'r')

for line in numbers_file:
    num = float(line)
    print(format(num, '.0f'))

numbers_file.close()

# 24 January 2021
# Starting Out With Python Workbench #5
# Modify the code that you wrote in question #4 so it adds all of the numbers
# read from the file and displays their total.

numbers_file = open('number_list.txt', 'r')

total = 0.0

for line in numbers_file:
    num = float(line)
    total += num

print('The total of the numbers in the number_list file is', format(total, ',.0f'))

numbers_file.close()

# 24 January 2021
# Starting Out With Python Exercise 1
# Assume that a file containing a series of integers is named numbers.txt and
# exists on the computer's disk. Write a program that displays all of the numbers
# in the file.

numbers_file = open('numbers.txt', 'r')
contents = numbers_file.read()
print(contents)
numbers_file.close()

# 24 January 2021
# Starting Out With Python Exercise 2
# Write a program that asks the user for the name of the file. The program should display
# only the first five lines of the file's contents. If the file contains less than
# five lines, it should display the file's entire contents

file_name = input('Enter the name of the file: ')

infile = open(file_name + '.txt', 'r')

line = infile.readline()

for i in range(1, 6):
    if line != '':
        line = line.rstrip('\n')
        print(line)
    line = infile.readline()

infile.close()

# 24 January 2021
# Starting Out With Python Exercise 3
# Write a program that asks the user for the name of a file. The program should display
# the contents of the file with each line preceded with a line number followed by a
# colon. The line numbering should start at 1.

read_position = 0

file_name = input('Enter the name of the file: ')

infile = open(file_name + '.txt', 'r')

line = infile.readline()

while line != '':
    line = (line.rstrip('\n'))
    read_position += 1
    print(read_position, ':', sep='', end='')
    print(' ', line)
    line = infile.readline()

infile.close() 

# 24 January 2021
# Starting Out With Python Exercise 4
# Assume that a file containing a series of names (as strings) is named names.txt
# and exists on the computer's disk. Write a program that displays the number of
# names that are stored in the file. (Hint: Open the file and read every string
# stored in it. Use a variable to keep a count of the number of items that are
# read from the file.)

infile = open('names.txt', 'r')

read_position = 0.0

line = infile.readline()

while line != '':
    line = line.rstrip('\n')
    read_position += 1
    line = infile.readline()

infile.close()

print('Number of names stored in this file:', read_position)

# 24 January 2021
# Starting Out With Python Exercise 5
# Assume that a file containing a series of integers is named numbers.txt and
# exists on the computer's disk. Write a program that reads all of the numbers
# stored in the file and calculates their total.

total = 0.0

infile = open('numbers.txt', 'r')

for line in infile:
    amount = float(line)
    total += amount

print('The total of the numbers in this file is', format(total, ',.1f'))

infile.close()

# 24 January 2021
# Starting Out With Python Exercise 6
# Assume that a file containing a series of integers is named numbers.txt and
# exists on the computer's disk. Write a program that calculates the average of
# all the numbers stored in the file.

read_position = 0

num_total = 0

infile = open('numbers.txt', 'r')

for line in infile:
    num = float(line)
    read_position += 1
    num_total += num

average = num_total / read_position

print('The average of the numbers stored in this file is', format(average, ',.1f'))

infile.close()

# 24 January 2021
# Starting Out With Python Exercise 7
# Write a program that writes a series of random numbers to a file. Each random
# number should be in the range of 1 through 500. The applications should let
# the user specify how many random numbers the file will hold. 

import random

outfile = open('random.txt', 'w')

total_num = int(input("Enter the total amount of random numbers you'd like" + \
                        "write to file random.txt: "))

for i in range(1, total_num + 1):
    num = random.randint(1, 501)
    outfile.write(str(num) + '\n')

print(total_num, 'numbers have been written to the random.txt file.')

outfile.close()

# 24 January 2021
# Starting Out With Python Exercise 8
# Assuming you have completed exercise 7, write a program that reads the random
# numbers from the file, displays the numbers and then displays the total of
# the numbers and the number of random numbers read from the file.

read_position = 0

total = 0

infile = open('random.txt', 'r')

for line in infile:
    line = line.rstrip('\n')
    num = int(line)
    print(line)
    total += num
    read_position += 1

print()
print('Total of the Numbers:', format(total, ',.1f'))
print('Number of Random Numbers in the File:', format(read_position, ',.0f'))

infile.close()

# 24 January 2021
# Starting Out With Python Exercise 9
# Modify the program that you wrote for exercise 6 so it handles the following
# exceptions: It should handle any IOError exceptions that are raised when the
# file is opened and data is read from it. It should handle any ValueError
# exceptions that are raised when the items that are read from the file are
# converted to a number.

try:
    
    read_position = 0

    num_total = 0

    infile = open('numbers.txt', 'r')

    for line in infile:
        num = float(line)
        read_position += 1
        num_total += num

    average = num_total / read_position

    print('The average of the numbers stored in this file is', format(average, ',.1f'))

    infile.close()

except IOError as msg:
    print(msg)

except ValueError as msg:
    print(msg)

# 25 January 2021
# Starting Out With Python Exercise 10
# The Springfork Amateur Golf Club has a tournament every weekend. The club president
# has asked you to write two programs:
# 1. A program that will read each player's name and golf score as keyboard input,
#    and then save these records in a file named golf.txt. (Each record will have
#    a field for the player's name and a field for the player's score.)
# 2. A program that reads the records from the golf.txt file and displays them.

def write_golf_data():

    keep_going = 'y'

    golf_file = open('golf.txt', 'w')

    while keep_going == 'y':
        name = input("Enter the player's name: ")
        score = float(input("Enter the player's score: "))
        golf_file.write(name + '\n')
        golf_file.write(str(score) + '\n')
        keep_going = input('Would you like to write another score to the file (enter y ' + \
                       'for yes)? ')

    print('The data has been written to the golf.txt file.')

    golf_file.close()

def read_golf_data():

    golf_file = open('golf.txt', 'r')

    name = golf_file.readline()

    while name != '':
        score = golf_file.readline()
        score = float(score.rstrip('\n'))
        name = name.rstrip('\n')
        print(name)
        print(score)
        name = golf_file.readline()

    golf_file.close()
