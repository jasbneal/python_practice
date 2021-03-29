# The DeleteBuildComponent module holds the DeleteComponent class which allows the user to delete
# an InventoryLevels obj from the dedicated inventory file.

import tkinter
import pickle
import InventoryLevels

class DeleteComponent:

    def __init__(self, FILE_NAME):
        self.main_window = tkinter.Toplevel()
        self.FILE_NAME = FILE_NAME

        # The top frame holds the window title. The mid1 frame holds the label
        # and entry widgets to retrieve the name of the component being deleted.
        # The mid2 frame holds the quit and delete buttons. The bottom frame holds
        # the response label widget.
        self.top_frame = tkinter.Frame(self.main_window)
        self.mid1_frame = tkinter.Frame(self.main_window)
        self.mid2_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.descr_label = tkinter.Label(self.top_frame, text='Delete a Build Component')

        self.descr_label.pack()

        self.name_label = tkinter.Label(self.mid1_frame, text="Enter the name of the item in inventory " + \
            "that you'd like to delete:")
        self.name_entry = tkinter.Entry(self.mid1_frame, width=20)

        self.name_label.pack(side='left')
        self.name_entry.pack(side='left')

        self.delete_button = tkinter.Button(self.mid2_frame, text='Delete', \
            command=self.delete_comp)
        self.quit_button = tkinter.Button(self.mid2_frame, text='Quit', \
            command=self.main_window.destroy)

        self.quit_button.pack(side='left')
        self.delete_button.pack(side='left')

        self.response_var = tkinter.StringVar()

        self.response_show = tkinter.Label(self.bottom_frame, textvariable=self.response_var)

        self.response_show.pack()

        self.top_frame.pack()
        self.mid1_frame.pack()
        self.mid2_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    def delete_comp(self):
        # Callback function for the Delete button. It retrieves the info entered in the
        # name Entry widgets and determines if it's in the dct in the given file. If so, it
        # deletes the entry from the dct and writes the new dct to the file. If it isn't in 
        # the dct, it displays an error message indicating that the item doesn't exist in the
        # system.
        try:
            input_file = open(self.FILE_NAME, 'rb')
            inv_dct = pickle.load(input_file)
            input_file.close()
        except FileNotFoundError:
            inv_dct = {}
        name = self.name_entry.get()
        if name in inv_dct:
            del inv_dct[name]
            self.response_var.set("This item has been deleted from inventory.")
        else:
            self.response_var.set("This item does not exist in the system. Please add it.")
        output_file = open(self.FILE_NAME, 'wb')
        pickle.dump(inv_dct, output_file)
        output_file.close()
