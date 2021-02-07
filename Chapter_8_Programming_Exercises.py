# 6 February 2021
# Starting Out With Python Chapter 8 Algorithm Workbench Exercise 7
# Write a function that accepts a string as an argument and displays the string
# backwards. 

string = 'Carola Neal'

def create_backwards_string(string):
    backwards_string = ''
    for i in range(len(string), 0, -1):
        backwards = string[i - 1]
        backwards_string += backwards
    print(backwards_string)

create_backwards_string(string)

# 6 February 2021
# Starting Out With Python Programming Exercise 1
# Write a program that gets a string containing a person's first, middle, and
# last names, and then display their first, middle and last initials. For example,
# if the user enters John William Smith the program should display J. W. S.

full_name = input('Enter your first, middle and last name: ')

initials = ''

# For loop that adds the capital letters to the initials string. Assumes that a
# capital letter indicates a first, middle or last name. 
for ch in full_name:
    if ch.isupper():
        initials += (ch + '. ')

print(initials)

# 6 February 2021
# Starting Out With Python Programming Exercise 2
# Write a program that akss the user to enter a series of single-digit numbers with
# nothing separating them. The program should display the sum of all the single
# digit numbers in the string. For example, if the user enters 2514, the method
# should return 12, which is the sum of 2, 5, 1, and 4.

digit_series = input('Enter a series of single-digit numbers with nothing' + \
                     'separating them: ')

total = 0
for ch in digit_series:
    total += int(ch)
print('Sum of the Digits:', total)

# 6 February 2021
# Starting Out With Python Programming Exercise 3
# Write a program that reads a string from the user containing a date in the form
# mm/dd/yyyy. It should print the date in the form March 12, 2014.

date = input('Enter a date in the mm/dd/yyyy format: ')

# Creates a list of months that's referenced to display the month (index = int(user input for month) -1)
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
date_list = date.split('/')
month = int(date_list[0])

# Displays the date in the Month Day, Year format
print(months[month - 1], ' ', end='')
print(date_list[1], ',', sep='', end='')
print(' ', date_list[2])

# 6 February 2021
# Starting Out With Python Programming Exercise 4
# Morse code is a code where each letter of the English alphabet, each digit,
# and various punctuation characters are represented by a series of dots and dashes.
# Table 8-4 shows part of the code. Write a program that asks the user to enter
# a string, and then converts that string to Morse code.

string = input('Enter a string to be converted to Morse code: ')

# Assigns special characters to variables, numbers to a list and letters to a list.
space = ' '
comma = '--..--'
period = '.-.-.-'
question_mark = '..--..'
numbers_0_to_9 = ['-----', '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.']
A_to_Z = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z']
morse_A_to_Z = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.-', '--..']

# Determines the character. If it's a number, prints the index of the int(ch) from the numbers_0_to_9 list.
# If it's a letter, looks for the index of the character in the A_to_Z list and prints the index of that
# letter in the morse_A_to_Z list.
for ch in string:
    if ch == space:
        print(space)
    elif ch == comma:
        print(comma)
    elif ch == period:
        print(period)
    elif ch == question_mark:
        print(question_mark)
    elif ch.isdigit():
        digit = int(ch)
        print(numbers_0_to_9[digit])
    elif ch.isalpha():
        letter = ch.upper()
        index = A_to_Z.index(letter)
        print(morse_A_to_Z[index])
    else:
        print('An invalid character is in the string.')

