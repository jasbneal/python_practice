import RetailItem

class CashRegister():

    def __init__(self):
        self.__register_list = []
        self.__total = 0

    def purchase_item(self, obj):
    # Takes an RetailItem object as an argument ad adds it to the internal list
        self.__register_list.append(obj)

    def get_total(self):
    # Adds the price of each RetailItem object in the internal list to the
    # self.__total accumulator
        for item in self.__register_list:
            price = item.get_price()
            self.__total += price
        return self.__total

    def show_items(self):
    # Prints all the RetailItem objects in the list.
        for item in self.__register_list:
            print(item.get_descr())

    def clear(self):
        self.__register_list = []

