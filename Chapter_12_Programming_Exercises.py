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
