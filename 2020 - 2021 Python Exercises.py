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
