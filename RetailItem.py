class RetailItem():
# Class that stores a retail item's description, number of units in 
# inventory and price.

    def __init__(self, descr, units, price):
        self.__descr = descr 
        self.__units = units 
        self.__price = price 

    def set_descr(self, descr):
        self.__descr = descr
    
    def set_units(self, units):
        self.__units = units

    def set_price(self, price):
        self.__price = price
    
    def get_descr(self):
        return self.__descr

    def get_units(self):
        return self.__units

    def get_price(self):
        return self.__price

    def __str__(self):
        return '\nDescription: ' + self.__descr + \
        '\nUnits: ' + str(self.__units) + \
        '\nPrice: $' + str(self.__price)
