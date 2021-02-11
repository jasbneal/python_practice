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
