# The ViewInv module holds the ViewInv class which allows the user to see all the 
# components in inventory based on the data in the dedicated inventory file.

import tkinter
import pickle
import InventoryLevels

class ViewInv:

    def __init__(self, FILE_NAME):
        self.main_window = tkinter.Toplevel()
        self.FILE_NAME = FILE_NAME

        try:
            input_file = open(self.FILE_NAME, 'rb')
            inv_dct = pickle.load(input_file)
            input_file.close()
        except FileNotFoundError:
            inv_dct = {}
        input_file.close()

        # The top frame holds grid formatted label widgets (3 columns= name, on_hand, min_need)
        # and the formatted data from the given inventory file.
        # The bottom frame holds the quit button which closes the main window.
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.top_frame.columnconfigure(0, weight=2)
        self.top_frame.columnconfigure(1, weight=1)
        self.top_frame.columnconfigure(2, weight=1)

        self.name_descr = tkinter.Label(self.top_frame, text='Item Name')
        self.name_descr.grid(column=0, row=0, padx=5, pady=5)

        self.item_on_hand_descr = tkinter.Label(self.top_frame, text='On-Hand Quantity')
        self.item_on_hand_descr.grid(column=1, row=0, padx=5, pady=5)

        self.min_need_descr = tkinter.Label(self.top_frame, text='Minimum Needed for Product Build')
        self.min_need_descr.grid(column=2, row=0, padx=5, pady=5)

        # Begins with the row beneath the title row. Puts the name in c=0, on_hand in c=1 and the min_need
        # in c=2. +1 to r to move the next item in the dct to the next row and repeats.
        r = 1
        c = 0
        for name in inv_dct:
            name = inv_dct[name].get_name()
            on_hand = inv_dct[name].get_on_hand()
            min_need = inv_dct[name].get_min_need()
            tkinter.Label(self.top_frame, text=name).grid(row=r, \
                column=c)
            tkinter.Label(self.top_frame, text=on_hand).grid(row=r, \
                column=c+1)
            tkinter.Label(self.top_frame, text=min_need).grid(row=r, \
                column=c+2)
            r += 1

        self.quit_button = tkinter.Button(self.bottom_frame, text='Quit', \
            command=self.main_window.destroy)
        self.quit_button.pack(side='right')

        self.top_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()