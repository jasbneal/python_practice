# The AddBuildComponent module holds the AddComponent class which allows the user to create
# an InventoryLevels obj and add it to the dedicated inventory file.

import tkinter
import pickle
import InventoryLevels

class AddComponent:

    def __init__(self, FILE_NAME):
        self.main_window = tkinter.Toplevel()
        self.FILE_NAME = FILE_NAME

        # The top frame holds the title. The mid1, mid2 and mid3 frames hold the label
        # and entry widgets for the component's name, on-hand amount and min_need for a
        # single unit build. The mid4 frame holds the quit and add buttons. The bottom
        # frame holds the response message label widget.
        self.top_frame = tkinter.Frame(self.main_window)
        self.mid1_frame = tkinter.Frame(self.main_window)
        self.mid2_frame = tkinter.Frame(self.main_window)
        self.mid3_frame = tkinter.Frame(self.main_window)
        self.mid4_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.title_label = tkinter.Label(self.top_frame, text='Add a Build Component')

        self.title_label.pack()

        self.name_label = tkinter.Label(self.mid1_frame, \
            text="Enter the name of the component you'd like to add:")
        self.name_entry = tkinter.Entry(self.mid1_frame, width=20)

        self.name_label.pack(side='left')
        self.name_entry.pack(side='left')

        self.on_hand_label = tkinter.Label(self.mid2_frame, \
            text='Enter the current on-hand amount in inventory of that component:')
        self.on_hand_entry = tkinter.Entry(self.mid2_frame, width=20)

        self.on_hand_label.pack(side='left')
        self.on_hand_entry.pack(side='left')

        self.min_need_label = tkinter.Label(self.mid3_frame, \
            text='Enter the needed minimum amount of this component to build a single unit:')
        self.min_need_entry = tkinter.Entry(self.mid3_frame, width=20)

        self.min_need_label.pack(side='left')
        self.min_need_entry.pack(side='left')

        self.add_button = tkinter.Button(self.mid4_frame, text='Add', command=self.add_comp)
        self.quit_button = tkinter.Button(self.mid4_frame, text='Quit', \
            command=self.main_window.destroy)

        self.quit_button.pack(side='left')
        self.add_button.pack(side='left')

        # Create a StringVar obj that displys the response of the action (error or success
        # message)
        self.response_var = tkinter.StringVar()
        
        self.response_show = tkinter.Label(self.bottom_frame, textvariable=self.response_var)

        self.response_show.pack()

        self.top_frame.pack()
        self.mid1_frame.pack()
        self.mid2_frame.pack()
        self.mid3_frame.pack()
        self.mid4_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    def add_comp(self):
        # Callback function for the Add button. It retrieves the info entered in the
        # name, on_hand and min_need Entry widgets, creates an InventoryLevels obj
        # adds it to the dct from the given file and writes the new dct to the file.
        # Response messages indicates if the add is successful.
        name = self.name_entry.get()
        on_hand = float(self.on_hand_entry.get())
        min_need = float(self.min_need_entry.get())
        inv_obj = InventoryLevels.InventoryLevels(name, on_hand, min_need)
        try:
            input_file = open(self.FILE_NAME, 'rb')
            inv_dct = pickle.load(input_file)
            input_file.close()
        except FileNotFoundError:
            inv_dct = {}
        inv_dct[name] = inv_obj
        output_file = open(self.FILE_NAME, 'wb')
        pickle.dump(inv_dct, output_file)
        output_file.close()
        self.response_var.set("You've added this item to inventory.")
    