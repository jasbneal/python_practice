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
