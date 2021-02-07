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

# 6 February 2021
# Starting Out With Python Programming Exercise 5
# Write a program that asks the user to enter a 10-character telephone
# number in the format XXX-XX-XXX. The application should display the
# telephone number with any alphabetic characters that appeared in the
# original translated to their numeric equivalent. Ex. 555-GET-FOOD shoudl
# display 555-438-3663.

tel_num = input('Enter a 10-character telephone number in the XXX-XX-XXXX format: ')
numeric_tel_num = ''

# Determines whether the ch is a digit, letter, dash or other and
# adds the new character to the numeric_tel_num string
for ch in tel_num:
    if ch.isdigit():
        numeric_tel_num += ch
    if ch == '-':
        numeric_tel_num += '-'
    if ch.isalpha():
        if ch.upper() == 'A' or ch.upper() == 'B' or ch.upper() == 'C':
            numeric_tel_num += '2'
        elif ch.upper() == 'D' or ch.upper() == 'E' or ch.upper() == 'F':
            numeric_tel_num += '3'
        elif ch.upper() == 'G' or ch.upper() == 'H' or ch.upper() == 'I':
            numeric_tel_num += '4'
        elif ch.upper() == 'J' or ch.upper() == 'K' or ch.upper() == 'L':
            numeric_tel_num += '5'
        elif ch.upper() == 'M' or ch.upper() == 'N' or ch.upper() == 'O':
            numeric_tel_num += '6'
        elif ch.upper() == 'P' or ch.upper() == 'Q' or ch.upper() == 'R' or ch.upper() == 'S':
            numeric_tel_num += '7'
        elif ch.upper() == 'T' or ch.upper() == 'U' or ch.upper() == 'V':
            numeric_tel_num += '8'
        elif ch.upper() == 'W' or ch.upper() == 'X' or ch.upper() == 'Y' or ch.upper() == 'Z':
            numeric_tel_num += '9'
        else:
            print('ERROR: An invalid character has been entered.')
            
print('Phone Number:', numeric_tel_num)

# 7 February 2021
# Starting Out With Python Programming Exercise 6
# Write a program that reads the text.txt file's contents (stored as one sentence
# per line) and calculates the average number of words per sentence.

infile = open('text.txt', 'r')

line_total = 0
word_total = 0

# For loop assigns each line to the line variable, splits it using the space character
# assigns that the to the line_list. Len(line_list) added to the word_total
# accumulator and divided by the total lines to get the average words per
# sentence.
for line in infile:
    line_list = line.split(' ')
    word_total += len(line_list)
    line_total += 1
    
print('Average Words Per Sentence:', word_total / line_total)
    
infile.close()

# 7 February 2021
# Starting Out With Python Programming Exercise 7
# Write a program that read's the contents of the text.txt file and determines:
# the number of uppercase letters in the file, number of lowercase letters in the file,
# number of digits in the file, number of whitespace characters in the file.

infile = open('text.txt', 'r')

upper_total = 0
lower_total = 0
digit_total = 0
whitespace_ch_total = 0

for line in infile:
    for ch in line:
        if ch.isupper():
            upper_total += 1
        if ch.islower():
            lower_total += 1
        if ch.isdigit():
            digit_total += 1
        if ch.isspace():
            whitespace_ch_total +=1

print('Total Uppercase Letters:', format(upper_total, ','))
print('Total Lowercase Letters:', format(lower_total, ','))
print('Total Digits:', format(digit_total, ','))
print('Total Whitespace Characters:', format(whitespace_ch_total, ','))

infile.close()

# 7 February 2021
# Starting Out With Python Programming Exercise 9
# Write a program with a function that accepts a string as an argument and returns the
# number of vowels that the string contains. The application should have another function
# that accepts a string as an argument and returns the number of consonants that the string
# contains, The application should let the user enter a string and should display the
# number of vowels and the number of consonants it contains.

def main():

    string = input('Enter a sentence or sentences: ')
    print('Total Vowels:', count_vowels(string))
    print('Total Consonants:', count_consonants(string))

def count_vowels(string):
    # If the ch is equal to a vowel, +1 to the total_vowels accumulator.
    total_vowels = 0
    for ch in string:
        if ch.upper() == 'A' or ch.upper() == 'E' or ch.upper() == 'I' or ch.upper() == 'O' or ch.upper() == 'U':
            total_vowels += 1
    return total_vowels

def count_consonants(string):
    # Creates a consonants list. If the ch is in the consonants lis, +1 to the
    # total_consonants accumulator.
    total_consonants = 0
    consonants_list = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V','W', 'X', 'Y', 'Z']
    for ch in string:
        if ch.upper() in consonants_list:
            total_consonants += 1
    return total_consonants

main()
