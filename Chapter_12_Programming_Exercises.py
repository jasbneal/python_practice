# 16 March 2021
# Starting Out With Python Exercise #1
# Design a recursive function that accepts an integer argument n, and prints the
# numbers 1 up through n.

try:
    n = int(input("Enter any whole number: "))
except ValueError:
    print("ERROR: You must enter a whole number. Try again.")
    n = int(input("Enter any whole number: "))

def show_num(n):
    if n == 0:
        return 0
    if n >= 1:
        show_num(n-1)
        print(n)

show_num(n)

# 16 March 2021
# Starting Out With Python Exercise #2
# Design a recursive function that accepts two arguments into the parameters x and y.
# The function whould return the value of x times y. Remember, the multiplication can be
# performed as repeated additions as follows:
# 7 X 4 = 4 + 4 + 4 + 4 + 4 + 4 + 4
# (To keep the function simple, assume that x and y will always hold positive nonzero integers.)

try:
    x = int(input("Enter any positive nonzero integer for x: "))
    y = int(input("Enter any positive nonzero integer for y: "))
except ValueError:
    print("ERROR: You must enter a positive nonzero integer. Try again.")
    x = int(input("Enter any positive nonzero integer for x: "))
    y = int(input("Enter any positive nonzero integer for y: "))

def multiply_nums(x, y):
    if x == 1:
        return y
    if x > 1:
        return y + multiply_nums(x - 1, y)

total = multiply_nums(x, y)
print(total)

# 16 March 2021
# Starting Out With Python Exercise #3
# Write a recursive function that accepts an argument, n. The function should display n
# lines of asterisks on the screen, with the first line showing 1 asterisk, the second line
# showing 2 asterisks, up to the nth line which shows n asterisks.

try:
    n = int(input("Enter any whole number: "))
except ValueError:
    print("ERROR: You must enter a whole number. Try again.")
    n = int(input("Enter any whole number: "))

def asterisks(n):
    if n == 1:
        print('*')
    if n > 1:
        asterisks(n - 1) 
        print('*' * n)

asterisks(n)

# 17 March 2021
# Starting Out With Python Exercise #4
# Design a function that accepts a list as an argument and returns the largest value
# in the list. The function should use recursion to find the largest item.

list1 = []

keep_going = 'y'

while keep_going.lower() == 'y':
    num = float(input("Enter a item to add to the list: "))
    list1.append(num)
    keep_going = input("Would you like to keep going? Enter y for yes and n for no: ")

def largest_item(list):
    n = len(list)
    if n == 0:
        print('The list is empty.')
    elif n == 1:
        print(format(list[0], ',.2f'))
    elif n > 1:
        if list[n-1] > list[n-2]:
            del list[n-2]
        else:
            del list[n-1]
        largest_item(list)

print("The largest item in the list is ", end='')
largest_item(list1)

# 17 March 2021
# Starting Out With Python Exercise #5
# Design a function that accepts a list of numbers as an argument. The function
# should recursively calculate the sum of all the numbers in the list and
# return that value.

list1 = []

keep_going = 'y'

while keep_going.lower() == 'y':
    num = float(input("Enter a item to add to the list: "))
    list1.append(num)
    keep_going = input("Would you like to keep going? Enter y for yes and n for no: ")

def add_list_items(list):
    n = len(list)
    if n == 0:
        print('The list is empty.')
    elif n == 1:
        print(format(list[0], ',.2f'))
    elif n > 1:
        list[-1] = list[-1] + list[-2]
        del list[-2]
        add_list_items(list)

print("The total of the items in the list is ", end='')
add_list_items(list1)