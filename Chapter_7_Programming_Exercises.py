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
        
