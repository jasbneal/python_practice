# 10 February 2021
# w3resrouce Python Dictionary Exercise #2
# Write a Python script to add a key to a dictionary. Sample dictionary =
# {0:10, 1:20}. Expected result = {0:10, 1:20, 2:30}

dictionary = {0:10, 1:20}
dictionary[2] = 30
print(dictionary)

# 10 February 2021
# w3resrouce Python Dictionary Exercise #4
# Write a Python script to check whether a key already exists in a dictionary.

dictionary = {0:10, 1:20}
key = int(input("Enter a key you'd like to search for in the dictionary: "))

if key in dictionary:
    print('Key is found in the dictionary.')
else:
    print('This key is not found in the dictionary.')

# 11 February 2021
# w3resrouce Python Dictionary Exercise #5
# Write a Python script to iterate over dictionaries using for loops.

dictionary = {'Jasmine' : 'Python', 'Qumars' : 'Python', 'Bukola' : 'Python',
              'Kara' : 'JavaScript', 'Andrei' : 'JavaScript', 'Ilyas' : 'Swift'}

for key in dictionary:
    print(key, ':', dictionary[key])

# 11 February 2021
# w3resrouce Python Dictionary Exercise #6
# Write a Python script to generate and print a dictionary that contains
# a number (between 1 and n) in the form (x, x*x). 
# Sample Dictionary (n = 5) :
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

numbers = dict()
num = int(input('Enter a number: '))

for i in range(1, num + 1):
    numbers[i] = i*i

print(numbers)

# 11 February 2021
# w3resrouce Python Dictionary Exercise #7
# Write a Python script to print a dictionary where the keys are numbers
# between 1 and 15 (both included) and the values are square of keys.
# Sample Dictionary

numbers = dict()

for i in range(1, 16):
    numbers[i] = i**2

print(numbers)

# 12 February 2021
# w3resrouce Python Dictionary Exercise #10
# Write a Python program to sum all the items in a dictionary.

dictionary = {0:10, 1:-20, 2:30, 3:-40, 4:50, 5:-60, 6:70, 7:-80, 8:90, 9:-100}

# VERSION 1
total = 0
for key in dictionary:
    total += dictionary[key]

#VERSION 2
total = sum(dictionary.values())

# 14 February 2021
# Starting Out With Python Algorithm Workbench Exercise 1
# Write a statement that creates a dictionary containing the following key-value
# pairs:
# 'a':1
# 'b':2
# 'c':3

dct = {'a':1, 'b':2, 'c':3}

print(dct)

# 14 February 2021
# Starting Out With Python Programming Exercise 1
# Write a program that creates a dictionary containing course numbers and the room numbers
# where the courses meet. The program should also create a dictionary containing
# course numbers and the names of the instructors that teach each course. The program
# should also create a dictionary containing course numbers and the meeting times
# of each course. The program should let the user enter a course number, and then it
# should display the course's room number, instructor and meeting time.

room_num_dct = {'CS101':3004, 'CS102':4501, 'CS103':6755, 'NT110':1244, 'CM241':1411}

instructor_dct = {'CS101':'Haynes', 'CS102':'Alvarado', 'CS103':'Rich', 'NT110':'Burke', 'CM241':'Lee'}

mtg_time_dct = {'CS101':'8:00 a.m.', 'CS102':'9:00 a.m.', 'CS103':'10:00 a.m.', 'NT110':'11:00 a.m.', 'CM241':'1:00 p.m.'}

course = input('Enter your course number: ')

print('Course Number:', course)
print('Course Room Number:', room_num_dct[course])
print('Course Instructor:', instructor_dct[course])
print('Course Meeting Time:', mtg_time_dct[course])

# 15 February 2021
# Starting Out With Python Programming Exercise 2
# Write a program that creates a dictionary containing the U.S. states as keys and their capitals as
# values. The program should then randomly quiz the user by displaying the name of a state and asking
# the user to enter the state's capital. The program should keep a count of the number of correct
# and incorrect responses. 

import random

state_capital_dct = {'Alabama': 'Montgomery', 'Alaska':'Juneau', 'Arizona':'Phoenix', 'Arkansas':'Little Rock',
    'California':'Sacramento', 'Colorado':'Denver', 'Connecticut':'Hartford', 'Delaware':'Dover', 'Florida':'Tallahassee',
    'Georgia':'Atlanta', 'Hawaii':'Honolulu', 'Idaho':'Boise', 'Illinois':'Springfield', 'Indiana':'Indianapolis',
    'Iowa':'Des Moines', 'Kansas':'Topeka', 'Kentucky':'Frankfort', 'Louisiana':'Baton Rouge', 'Maine':'Augusta',
    'Maryland':'Annapolis', 'Massachusetts':'Boston', 'Michigan':'Lansing', 'Minnesota':'Saint Paul', 'Mississippi':'Jackson',
    'Missouri':'Jefferson City', 'Montana':'Helena', 'Nebraska':'Lincoln', 'Nevada':'Carson City', 'New Hampshire':'Concord',
    'New Jersey':'Trenton', 'New Mexico':'Santa Fe', 'New York':'Albany', 'North Carolina':'Raleigh', 'North Dakota':'Bismarck', 
    'Ohio':'Columbus', 'Oklahoma':'Oklahoma City', 'Oregon':'Salem', 'Pennsylvania':'Harrisburg', 'Rhode Island':'Providence',
    'South Carolina': 'Columbia', 'South Dakota':'Pierre', 'Tennessee':'Nashville', 'Texas':'Austin', 'Utah':'Salt Lake City',
    'Vermont':'Montpelier', 'Virginia':'Richmond', 'Washington':'Olympia', 'West Virginia':'Charleston', 'Wisconsin':'Madison',
    'Wyoming':'Cheyenne'}
    
keep_going = 'Y'
total_correct = 0
total_incorrect = 0

# For loop to determine if the game continues or ends.
while keep_going.upper() == 'Y':
    key = random.choice(list(state_capital_dct))
    print('Enter the capital of', key, end='')
    response = input(': ')
    if response == state_capital_dct[key]:
        print("That's correct!")
        total_correct += 1
    else:
        print("That's incorrect.")
        total_incorrect += 1
    keep_going = input('Would you like to keep going (y/n)? ')

print()
print('Total Correct Answers:', total_correct)
print('Total Incorrect Answers:', total_incorrect)

# 15 February 2021
# Starting Out With Python Programming Exercise 3
# Write a program that uses a dictionary to assign "codes" to each letter of the alphabet.
# Ex. codes = {'A': '%', 'a':'9', 'B':'@', 'b':'#', etc...}
# The prgroam should open a specified text file, read its contents, and then use the 
# dictionary to write an encrypted version of the file's contents to a second file. Each
# character in the second file should contain the code for the corresponding character in
# the first file. Write a second program that opens an encrypted file and displays its
# decrypted contents on the screen.

encrypt_key ={'A':'+', 'a':'3', 'B':'~', 'b':'7', 'C':'-', 'c':'z', 'D':'!', 'd':'a', 'E':')', 'e':'b', 
'F':'@', 'f':'y', 'G':'(', 'g':'c', 'H':'#', 'h':'x', 'I':'*', 'i':'d', 'J':'$', 'j':'v', 'K':'&', 'k':'e',
'L':'%', 'l':'w', 'M':'^', 'm':'f', 'N':'?', 'n':'<', 'O':'"', 'o':'u', 'P':'=', 'p':'g', 'Q':'1', 'q':'t',
'R':'6', 'r':'h', 'S': '9', 's':'s','T':'5', 't':'i', 'U':'4', 'u':'r', 'V':'>', 'v':'j', 'W':'2', 'w':'q',
'X':':', 'x':'k', 'Y':'8', 'y':'p','Z':'0', 'z':'l'}

infile = open('GirlNames.txt', 'r')
outfile = open('GirlNamesEncrypted.txt', 'w')

# Encrypts each character in each line and saves the results to the GirlNamesEncrypted.txt file
for line in infile:
    line = line.rstrip('\n')
    for ch in line:
        new_ch = encrypt_key[ch]
        outfile.write(new_ch)
    outfile.write('\n')

infile.close()
outfile.close()

infile = open('GirlNamesEncrypted.txt','r')

# Uses the k_and_v dictionary view to identify the key associated with the value, adds it to a new string and prints the string.
k_and_v = encrypt_key.items()
print(k_and_v)

for line in infile:
    line = line.rstrip('\n')
    new_line = ''
    for ch in line:
        for key, value in k_and_v:
            if ch == value:
                new_line += key
    print(new_line)

infile.close()

# 15 February 2021
# Starting Out With Python Programming Exercise 4
# Write a program that opens a specified text file and then displays a list of 
# all the unique words found in the file. (Hint: Store each word as an element
# of a set.)

words_set = set()

infile = open('WorldSeriesWinners.txt', 'r')

# For loop that removes the newline character and punctuation from each line, then splits the words
# based on spaces and adds the words to the words_set set.
for line in infile:
    line = line.rstrip('\n')
    new_line = ''
    discard = ''
    for ch in line:
        if ch == '.' or ch == '?' or ch == '!' or ch == '"' or ch == ',':
            discard += ch
        else:
            new_line += ch.lower()
    line_list = new_line.split(' ')
    words_set.update(tuple(line_list))

print('Unique Words in the File')
print('------------------------')
for element in words_set:
    print(element)
print()
print('Number of Unique Words in the File:', len(words_set))

infile.close()

# 15 February 2021
# Starting Out With Python Programming Exercise 5
# Write a program that reads the contents of a text file. The program should create
# a dictionary in which the keys are the individual words found in the file and
# the values are the number of times each word appears. Ex. if the word "the" appears
# 128 times, the dictionary would contain an element with 'the' as the key and 128
# as the value. The program should either display the frequency of each word or create
# a second file containing a list of each word and its frequency.

word_dct = {}

infile = open('text.txt', 'r')

# For loop that removes the newline character and punctuation from each line, then splits the words
# based on spaces and adds the words to the line_list.
for line in infile:
    line = line.rstrip('\n')
    new_line = ''
    discard = ''
    for ch in line:
        if ch == '.' or ch == '?' or ch == '!' or ch == '"' or ch == ',':
            discard += ch
        else:
            new_line += ch.lower()
    line_list = new_line.split(' ')

# For loop that determines if the word in the list is in the word_dct. If so, it +1 to value. If not,
# adds the element with a value of 1.
    for element in line_list:
        if element in word_dct:
            word_dct[element] += 1
        else:
            word_dct[element] = 1

for key in word_dct:
    print('Word:', key, 'Frequency:', word_dct[key])

infile.close()

# 16 February 2021
# Starting Out With Python Programming Exercise 6
# Write a program that reads the contents of two text files and compares them in
# the following ways: it should display a list of all the unique qwords contained
# in both files, it should display a list of the words that appear in both files,
# it should display a list of the words that appear in the first file but not the
# second, it should display a list of words that appear in the second file but not
# the first, it should display a list of words that appear in either the first or
# second file but not both.

words_set1 = set()
words_set2 = set()

infile1 = open('text.txt', 'r')
infile2 = open('WorldSeriesWinners.txt', 'r')

# For loop that removes the newline character and punctuation from each line, then splits the words
# based on spaces and adds the words to the words_set set. Same logic for the second file too.
for line in infile1:
    line = line.rstrip('\n')
    new_line = ''
    discard = ''
    for ch in line:
        if ch == '.' or ch == '?' or ch == '!' or ch == '"' or ch == ',':
            discard += ch
        else:
            new_line += ch.lower()
    line_list1 = new_line.split(' ')
    words_set1.update(tuple(line_list1))

for line in infile2:
    line = line.rstrip('\n')
    new_line = ''
    discard = ''
    for ch in line:
        if ch == '.' or ch == '?' or ch == '!' or ch == '"' or ch == ',':
            discard += ch
        else:
            new_line += ch.lower()
    line_list2 = new_line.split(' ')
    words_set2.update(tuple(line_list2))
  
print()
print('Unique Words in the first file:')
print(words_set1)
print()
print('Uniwue Words in the second file:')
print(words_set2)

# Intersection of both files
print()
words_set3 = words_set1 & words_set2 
print('Words that appear in both files:')
print(words_set3)

# Difference of the first file and the second file
print()
words_set4 = words_set1 - words_set2
print('Words that appear in the first file but not the second:')
print(words_set4)

# Difference of the second file and the first file
print()
words_set5 = words_set2 - words_set1
print('Words that appear in the second file but not the first:')
print(words_set5)

# Symmetric difference of the two files
print()
words_set6 = words_set1 ^ words_set2
print('Words that appear in either files but not both:')
print(words_set6)

infile1.close()
infile2.close()

# 16 February 2021
# Starting Out With Python Programming Exercise 7
# Write a program that reads the WorldSeriesWinners.txt file and creates a 
# dictionary in which the keys are the names of the teams and each key's
# associated value is the number of times the team has won the World Series.
# The program should also create a dictionary in which the keys are the year
# and each key's associated value is the name of the team that won that year.
# The program should prompt the user for a year in the range of 1903 and 2008.
# It should then display the name of the team that won the World Series that
# year and the number of times that team has won the World Series. 

WorldSeriesWinnersCount_dct = {}
WorldSeriesWinnersYears_dct = {}

infile = open('WorldSeriesWinners.txt', 'r')

starting_year = 1903

# For each line (team) in the file, if it's in the WSWC_dct, +1 to value. If it's not,
# adds it. Using starting_year accumulator, adds staring year and line (team) to WSWY_dct,
# skipping years 1904 and 1994.
for line in infile:
    line = line.rstrip('\n')
    if line in WorldSeriesWinnersCount_dct:
        WorldSeriesWinnersCount_dct[line] += 1
    else:
        WorldSeriesWinnersCount_dct[line] = 1
    if starting_year == 1904 or starting_year == 1994:
        starting_year += 1
        WorldSeriesWinnersYears_dct[starting_year] = line
    else:
        WorldSeriesWinnersYears_dct[starting_year] = line
    starting_year += 1


year = int(input('Enter a year in the range of 1903 and 2008: '))

if year in WorldSeriesWinnersYears_dct:
    winner = WorldSeriesWinnersYears_dct.get(year)
    print('The winner of the World Series in', year, 'was the', winner)
    print('The', winner, 'won', WorldSeriesWinnersCount_dct[winner], 'time(s) between 1903 and 2008.')
else:
    year = print('ERROR: You have entered an invalid year.')

infile.close()

