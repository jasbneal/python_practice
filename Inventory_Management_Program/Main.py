# The Main module holds the main window which allows the user to select their
# choice in the inventory management program (add a component, delete a component,
# update a component's inventory levels, determine order to delivery eta, and view
# view current inventory).

import tkinter
import pickle
import AddBuildComponent
import DeleteBuildComponent
import UpdateInv
import ViewInv
import BedETA

# Global constant to represent the file linked to the program (that holds the
# inventory data). The FILE_NAME var is passed as an arg in the triggered
# actions so if it is changed here, it is changed in the entire program.
FILE_NAME = 'Inv.dat'

class SelectionMenu:

    def __init__(self):
        self.main_window = tkinter.Tk()

        # The top frame holds the title. The middle frame holds the Radiobutton 
        # widgets. #The bottom frame holds the quit button and select button (the select
        # button triggers the opening of a Toplevel widget for its corresponding action).
        self.top_frame = tkinter.Frame(self.main_window)
        self.middle_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.menu_label = tkinter.Label(self.top_frame, \
            text="Select the action you'd like to take:")

        self.menu_label.pack()

        # Create an IntVar obj to use with the Radiobuttons
        self.select_var = tkinter.IntVar()
        self.select_var.set(0)

        # Radiobutton widgets that allow the user to select between "Add a build
        # component", "Delete a build component", "Update inventory levels", "Determine
        # the estimated time from order to bed arrival", and "View current inventory levels."
        self.add_rb = tkinter.Radiobutton(self.middle_frame, text='Add a build component', \
            variable=self.select_var, value=1)
        self.delete_rb = tkinter.Radiobutton(self.middle_frame, text='Delete a build component', \
            variable=self.select_var, value=2)
        self.update_inv_rb = tkinter.Radiobutton(self.middle_frame, text='Update inventory levels', \
            variable=self.select_var, value=3)
        self.eta_rb = tkinter.Radiobutton(self.middle_frame, text='Determine the estimated time from ' + \
            'order to bed arrival', variable=self.select_var, value=4)
        self.view_inv_rb = tkinter.Radiobutton(self.middle_frame, text='View current inventory levels', \
            variable=self.select_var, value=5)

        self.add_rb.pack()
        self.delete_rb.pack()
        self.update_inv_rb.pack()
        self.eta_rb.pack()
        self.view_inv_rb.pack()

        # The Select button creates an instance of the appropriate class based on the chosen option.
        # The quit button exits out of the main window. 
        self.select_button = tkinter.Button(self.bottom_frame, text='Select', command=self.select_option)
        self.quit_button = tkinter.Button(self.bottom_frame, text='Quit', command=self.main_window.destroy)

        self.quit_button.pack(side='left')
        self.select_button.pack(side='left')

        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    def select_option(self):
        # Get the value of the self.select_var to determine which action to take.
        action = self.select_var.get()

        if action == 1:
            # Open AddComponent Toplevel widget.
            add_comp_gui = AddBuildComponent.AddComponent(FILE_NAME)
        elif action == 2:
            # Open DeleteComponent Toplevel widget.
            delete_comp_gui = DeleteBuildComponent.DeleteComponent(FILE_NAME)
        elif action == 3:
            # Open UpdateInv Toplevel widget.
            update_inv_gui = UpdateInv.UpdateInv(FILE_NAME)
        elif action == 4:
            # Open BedETA Toplevel widget.
            eta_gui = BedETA.BedETA(FILE_NAME)
        elif action == 5:
            # Open ViewInv Toplevel widget.
            view_inv_gui = ViewInv.ViewInv(FILE_NAME)

inv_management_gui = SelectionMenu()
