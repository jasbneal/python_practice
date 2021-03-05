# 4 March 2021
# Starting Out With Python Programming Exercise 7
# Assuming you have created the RetailItem class for Programming Exercise 5, create
# a CashRegister class that can be used with the RetailItem class. The CashRegister
# class should be able to internally keep a list of RetailItem objects and have the
# following methods: 
# A method named purchase_item that accepts a RetailItem object as an argument. Each
# time the purchase_item method is called, the RetailItem object that is passed as an
# argument should be added to the list.
# A method named get_total that returns the total price of all the RetailItem objects
# stored in the CashRegister object's internal list.
# A method named show_items that displays data about the RetailItem objects stored in
# the CashRegister object's internal list.
# A method named clear that should clear the CashRegister object's internal list.

# Demonstrate the CashRegister class in a program that allows the user to select several
# items for purchase. When the user is ready to check out, the program should display
# a list of all the items he/she has selected for purchase, as well as the total price.

import RetailItem
import CashRegister
import pickle

# MENU
ADD_ITEM_TO_INV = 1
UPDATE_ITEM_UNITS = 2
DELTE_ITEM_FROM_INVENTORY = 3
PURCHASE = 4

def main():
    
    try:
        input_file = open('item_inv.dat', 'rb')
        inv_dct = pickle.load(input_file)
        input_file.close()
    except FileNotFoundError:
        inv_dct = {}

    choice = print_menu()

    while choice != PURCHASE:
    # Loop allowing the user to add an itemt to the inventory list, 
    # update the units of an item or delete an item. When the user selects
    # PURCHASE, the loop ends.

        if choice < 1 or choice > 4:
            print("You've entered an invalid option, try again.")
            choice = int(input('Enter a new choice: '))

        if choice == ADD_ITEM_TO_INV:
        # Gathers the description, units and price of an item, creates a 
        # RetailItem oject and adds it to the inv_dct dictionary (key = descr, value = obj)
            try:
                descr = create_descr()
            except ValueError:
                print("Invalid Entry. Please try again.")
                descr = create_descr()
            if descr not in inv_dct:
                units = create_inv_units()
                price = create_price()
                obj = RetailItem.RetailItem(descr, units, price)
                inv_dct[descr] = obj
            else:
                print('This item is already in the inventory.')

        if choice == UPDATE_ITEM_UNITS:
        # Gets the description for the item and calls the set_units method to update
        # the number of units in inventory
            try:
                descr = input("Enter the description of the item you'd like to update: ")
            except ValueError:
                print("Invalid Entry. Please try again.")
                descr = input("Enter the description of the item you'd like to update: ")
            if descr in inv_dct:
                units = int(input("Enter the new amount of units in inventory for this item: "))
                obj = inv_dct[descr]
                obj.set_units(units)
                print('The units in inventory have been updated.')
            else:
                print('This item is not in inventory.')

        if choice == DELTE_ITEM_FROM_INVENTORY:
        # Deletes an item from the inventory list.
            try:
                descr = input("Enter the description of the item you'd like to delete: ")
            except ValueError:
                print("Invalid Entry. Please try again.")
                descr = input("Enter the description of the item you'd like to delete: ")
            if descr in inv_dct:
                del inv_dct[descr]
                print('This item has been deleted from inventory.')
            else:
                print("The item you entered doesn't exist in inventory.")

        choice = print_menu()

    # Display all the items in stock for the user. If units in inventory > 0,
    # the item is printed. 
    print()
    print('Items In Stock')
    print('--------------')

    for key in inv_dct:
        obj = inv_dct[key]
        if obj.get_units() > 0:
            print(key)

    register = CashRegister.CashRegister()

    # Loop promptingg the user to enter the descr of the item they'd like to purhcase,
    # passes the item's value (RetailItem object) as an argument to the CashRegister
    # purchase_item method (adds the item to an internal list and adds its price to a 
    # total accumulator). -1 from units attribute to update the inventory level.
    another_item = 'y'
    while another_item.lower() == 'y':
        item = input("Enter the name of the item you'd like to purchase: ")
        if item in inv_dct:
            obj = inv_dct[item]
            if obj.get_units() > 0:
                selection = inv_dct[item]
                register.purchase_item(selection)
                units = obj.get_units()
                new_units = units - 1
                obj.set_units(new_units)
                
            else:
                print('This item is out of stock. Please select another one.')
        else:
            print('ERROR: This item is not available to purchase.')
        another_item = input("Would you like to purchase another item (Enter y for yes)? ")

    # Prints the items in the register object's internal list.
    print()
    print('Items You Have Selected:')
    print('------------------------')
    register.show_items()

    # Calls the get_total function for the register object for the total amount of 
    # all chosen items. 
    print()
    print('Purchase Total: $', format(register.get_total(), ',.2f'), sep='')

    output_file = open('item_inv.dat', 'wb')
    pickle.dump(inv_dct, output_file)
    output_file.close()

    # Clears the register object's internal list.
    register.clear()

def create_descr():
    descr = input("Enter the item's description: ")
    return descr

def create_inv_units():
    units = int(input("Enter the amount of units on hand of this item: "))
    return units

def create_price():
    price = float(input('Enter the price of the item: '))
    return price

def print_menu():
    print('MENU')
    print('----------')
    print('Add a new item to inventory: 1')
    print('Update the units in inventory of an existing item: 2')
    print('Delete an item from inventory: 3')
    print('Purchase an item/items: 4')
    choice = int(input('Enter your selection from the menu: '))
    return choice

main()