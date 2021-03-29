# The InventoryLevels class creates objects that has a name attribute
# (name of the component needed to build a single unit), on_hand attribute 
# (amount of that specific component on-hand in current inventory) and
# a min_need attribute (the minimum number of the component needed to build
# a full single unit)

class InventoryLevels:

    def __init__(self, name, on_hand, min_need):
        self.__name = name
        self.__on_hand = on_hand
        self.__min_need = min_need

    # Mutator method for the name attribute
    def set_name(self, name):
        self.__name = name
    
    # Mutator method for the on_hand attribute
    def set_on_hand(self, on_hand):
        self.__on_hand = on_hand

    # Mutator method for the min_need attribute
    def set_min_need(self, min_need):
        self.__min_need = min_need

    # Mutator method for the name attribute
    def get_name(self):
        return self.__name

    # Accessor method for the on_hand attribute
    def get_on_hand(self):
        return self.__on_hand

    # Accessor method for the min_need attribute
    def get_min_need(self):
        return self.__min_need
 