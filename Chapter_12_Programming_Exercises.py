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
