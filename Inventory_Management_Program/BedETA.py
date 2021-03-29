# The BedETA module holds the BedETA class which allows the user to see the estimated
# time from order to delivery. 3 weeks is the standard time, and a delay of 1 week is
# added if any needed components are not in stock. 

import tkinter
import pickle
import InventoryLevels

class BedETA:

    def __init__(self, FILE_NAME):
        self.main_window = tkinter.Toplevel()
        self.FILE_NAME = FILE_NAME

        # The top frame holds the label widget that displays the eta. # The bottom
        # frame holds the quit button.
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        try:
            input_file = open(self.FILE_NAME, 'rb')
            inv_dct = pickle.load(input_file)
            input_file.close()
        except FileNotFoundError:
            inv_dct = {}
        input_file.close()

        # Create a StringVar obj that displys the response of the action (eta).
        self.bed_eta_var = tkinter.StringVar()
        self.bed_eta_show = tkinter.Label(self.top_frame, textvariable=self.bed_eta_var)
        self.bed_eta_show.pack()
        
        # Set the on_time variable to true.
        self.bed_on_time = True

        for item in inv_dct:
            on_hand = inv_dct[item].get_on_hand()
            min_need = inv_dct[item].get_min_need()

            # If the min_need < on_hand value, the on_time variable is set to false
            # which will display the updated eta.
            if min_need < on_hand:
                self.bed_on_time = False

        if self.bed_on_time:
            self.bed_eta_var.set("The estimated time from order to delivery is 3 weeks.")
        else:
            self.bed_eta_var.set("The estimated time from order to delivery is 4 weeks.")

        self.quit_button = tkinter.Button(self.bottom_frame, text='Quit', \
            command=self.main_window.destroy)
        self.quit_button.pack()

        self.top_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()