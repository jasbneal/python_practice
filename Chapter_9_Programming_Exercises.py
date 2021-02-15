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