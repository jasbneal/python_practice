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
