# Inventory Management Program

### Introduction

The Inventory Management Program is a simple GUI program that gives the user a comprehensive way to manage the components needed to build a given product. The main functionalities of the program include:

- Adding a product component's name, on-hand amount and minimum amount needed to build a single product 
- Delete a product component that may no longer be needed 
- Update an existing product component's on-hand amount or minimum amount needed to build a single product
- Determine the estimated time from order placement to product arrival
- View the complete list of product components (on-hand amounts and minimum amount needed for a single build)

<p align="center">
	<img width="382" height="177" src="https://github.com/jasbneal/python_practice/blob/main/Inventory_Management_Program/img/Screen_Shot_2021-03-30_at_1.52.47_PM.png?raw=true">	
</p>

### How It Works

1. The Inventory Management Program has seven different modules. The `Main.py` module creates an instance of the `SelectionMenu` class which creates an instance of the tkinter's Tk class as the main window that holds the selection `Radiobutton` widgets. Five modules hold the `Toplevel` widgets that are opened after a selection is made  (`AddBuildComponent.py`, `DeleteBuildComponent.py`, `UpdateInv.py`, `BedETA.py`, and `ViewInv.py`). The `InventoryLevels.py` module contains the `InventoryLevels` class that creates a component object with the name, on_hand and min_need attributes. 
2. The global `FILE_NAME` variable allows the user to write the name of the file that will hold the inventory data. This variable is passed as an argument for all modules other than the [`Main.py`](http://main.py) module so that the file name only needs to be changed once and it trickles down through the connected modules.
3. When the user selects one of the options in the main window, the action triggers a callback function that creates an instance of a class within the corresponding module of the action. 
4. When a module's callback function executes, the new `inv_dct` dictionary which contains a product's components data, is rewritten to the given file name to reflect the changes made.

EXAMPLE: Execution of the Add a Build Component GUI from `Main.py`'s Select button's callback function

<p align="center">
	<img width="656" height="174" src=https://github.com/jasbneal/python_practice/blob/main/Inventory_Management_Program/img/Screen%20Shot%202021-03-31%20at%2012.24.31%20PM.png?raw=true>
</p>

```python
self.add_rb = tkinter.Radiobutton(self.middle_frame, \ 
    text='Add a build component', variable=self.select_var, value=1)

self.select_button = tkinter.Button(self.bottom_frame, text='Select', command=self.select_option)

def select_option(self):
	  # Get the value of the self.select_var to determine which action to take.
    action = self.select_var.get()

    if action == 1:
    # Open AddComponent Toplevel widget.
    add_comp_gui = AddBuildComponent.AddComponent(FILE_NAME)
```

```python
def add_comp(self):     
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
```

### Technologies Used

The program use's Python's built-in **pickle module** to serialize the `inv_dct` contents and write it to the specified file and the built-in **tkinter module** for the user interfaces.
