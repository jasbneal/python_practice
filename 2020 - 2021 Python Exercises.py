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
