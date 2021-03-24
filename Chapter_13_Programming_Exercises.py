# 22 March 2021
# Starting Out With Python Exercise #1
# Write a GUI program that displays a name and address when a button is
# clicked. The program should only display the Show Info and Quit buttons
# when it runs. When the user clicks the Show Info button, the program should
# display your name and address.

    # Steven Marcus
    # 274 Baily Drive
    # Waynesville, NC 27999

import tkinter

class NameAndAddress:

    def __init__(self):
        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # Creates a StringVar object to associate with the info_label.
        self.info = tkinter.StringVar()

        self.info_label = tkinter.Label(self.top_frame, textvariable=self.info)

        self.info_label.pack()

        # Show Info button will display the text stored in the self.info obj when
        # clicked. The info_display function sets the contents of the self.info obj.
        self.show_info_button = tkinter.Button(self.bottom_frame, text='Show Info', \
            command=self.info_display)
        self.quit_button = tkinter.Button(self.bottom_frame, text='Quit', \
            command=self.main_window.destroy)

        self.show_info_button.pack(side='left')
        self.quit_button.pack(side='left')

        self.top_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    def info_display(self):
        # Assigns the name and address to the info variable. Passes the info
        # variable as an argument for the StringVar's (info.set) set method
        info = 'Steven Marcus \n274 Baily Drive' + \
            '\nWaynesville, NC 27999'
        self.info.set(info)

S_Marcus = NameAndAddress()

# 22 March 2021
# Starting Out With Python Exercise #2
# Look at the following list of Latin words and their meanings.
#      Latin       English
#      sinister    left
#      dexter      right
#      medium      center
# Write a GUI program that translates the Latin words to English. The
# window should have three buttons, one for each Latin word. When the 
# user clicks a button, the program displays the English translation in 
# a label.

import tkinter

class LatinToEng:

    def __init__(self):
        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # Top frame has a left aligned label (ans_label) and a label to
        # the right of it (ans_output) that's associated with the eng_word StringVar
        # object
        self.ans_label = tkinter.Label(self.top_frame, \
            text='English Translation:')
        self.eng_word = tkinter.StringVar()
        self.ans_output = tkinter.Label(self.top_frame, \
            textvariable=self.eng_word)

        self.ans_label.pack(side='left')
        self.ans_output.pack(side='left')

        # Bottom frame has three buttons: Sinister (displays the eng translation of sinister), 
        # Dexter (displays the eng translation of dexter), Medium (displays the eng translation of medium) 
        # and Quit (closes the entire program)
        self.sinister_button = tkinter.Button(self.bottom_frame, \
            text='Sinister', command=self.sinister_to_eng)
        self.dexter_button = tkinter.Button(self.bottom_frame, \
            text='Dexter', command=self.dexter_to_eng)
        self.medium_button = tkinter.Button(self.bottom_frame, \
            text='Medium', command=self.medium_to_eng)
        self.quit_button = tkinter.Button(self.bottom_frame, \
            text='Quit', command=self.main_window.destroy)

        self.sinister_button.pack(side='left')
        self.dexter_button.pack(side='left')
        self.medium_button.pack(side='left')
        self.quit_button.pack(side='bottom')

        self.top_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    # Assigns the eng translation of the respective latin word to the eng_word variable. 
    # Passes the info variable as an argument for the StringVar's 
    # (eng_word) set method.
    def sinister_to_eng(self):
        self.eng_word.set('Left')

    def dexter_to_eng(self):
        self.eng_word.set('Right')
        
    def medium_to_eng(self):
        self.eng_word.set('Center')

Translater = LatinToEng()

# 23 March 2021
# Starting Out With Python Exercise #3
# Write a GUI program that calculates a car's gas mileage. The program's window
# should have Entry widgets that let the user enter the number of gallons of gas
# the car holds, and the number of miles it can be driven on a full tank. When a 
# Calculate MPG button is clicked, the program should display the number of miles
# that the car may be driven per gallon of gas.
#   MPG = miles / gallons

import tkinter

class MPG:

    def __init__(self):
        self.main_window = tkinter.Tk()

        # Top frame gets the gallons input from the user, middle_frame1 gets the miles
        # input from the user, middle_frame2 displays the MPG, bottom_frame has the 
        # Calculate MPG and Quit buttons
        self.top_frame = tkinter.Frame(self.main_window)
        self.middle_frame1 = tkinter.Frame(self.main_window)
        self.middle_frame2 = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.gallons_label = tkinter.Label(self.top_frame, \
            text='Enter the number of gallons the car holds:')
        self.gallons_entry = tkinter.Entry(self.top_frame)

        self.gallons_label.pack(side='left')
        self.gallons_entry.pack(side='left')

        self.miles_label = tkinter.Label(self.middle_frame1, \
            text='Enter the number of miles the car can drive on ' + \
                'a full tank: ')
        self.miles_entry = tkinter.Entry(self.middle_frame1)

        self.miles_label.pack(side='left')
        self.miles_entry.pack(side='left')

        # Middle_frame2 has a left aligned label (mpg_label) and a label to
        # the right of it (mpg_ans) that's associated with the mpg_var StringVar
        # object
        self.mpg_label = tkinter.Label(self.middle_frame2, \
            text='Miles Per Gallon:')
        self.mpg_var = tkinter.StringVar()
        self.mpg_ans = tkinter.Label(self.middle_frame2, \
            textvariable=self.mpg_var)

        self.mpg_label.pack(side='left')
        self.mpg_ans.pack(side='left')

        # The calc_button calculates + displays the MPG, the quit_button ends
        # the entire program
        self.calc_button = tkinter.Button(self.bottom_frame, \
            text='Calculate MPG', command=self.calc_mpg)
        self.quit_button = tkinter.Button(self.bottom_frame, \
            text='Quit', command=self.main_window.destroy)

        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')

        self.top_frame.pack()
        self.middle_frame1.pack()
        self.middle_frame2.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    def calc_mpg(self):
        # Gets the input from the gallons and miles Entry widgets,
        # calculates the MPG and passes a formated response into the 
        # mpg_var set method (StringVar variable)
        gallons = float(self.gallons_entry.get())
        miles = float(self.miles_entry.get())
        mpg = miles / gallons
        self.mpg_var.set(format(mpg, ',.1f'))

mpg_gui = MPG()

# 23 March 2021
# Starting Out With Python Exercise #4
# Write a GUI program that converts Celsius temperatures to Farenheit temperatures.
# The user should be able to enter a Celsius temperature, click a button, and then
# see the equivalent Farenheit temperature. Use the following formula to make the
# coversion:
# F = (9/5)C + 32
# F is the Farenheit temperature and C is the Celsius temperature.

import tkinter

class FarenheitToCelsius:

    def __init__(self):

        # The top frame allows the user to enter a temperature in Celsius,
        # the middle frame displays the temperature converted to Farenhet,
        # and the bottom frame has the calculate and quit buttons.
        self.main_window = tkinter.Tk()
        self.top_frame = tkinter.Frame(self.main_window)
        self.middle_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.celsius_label = tkinter.Label(self.top_frame, \
            text='Enter a temperature in Celsius:')
        self.celsius_entry = tkinter.Entry(self.top_frame)

        self.celsius_label.pack(side='left')
        self.celsius_entry.pack(side='left')

        # Create the StringVar obj to be associated with the faren_show label.
        self.faren_var = tkinter.StringVar()
        self.faren_label = tkinter.Label(self.middle_frame, \
            text='Temperature Converted to Farenheit:')
        self.faren_show = tkinter.Label(self.middle_frame, \
            textvariable=self.faren_var)

        self.faren_label.pack(side='left')
        self.faren_show.pack(side='left')

        self.calc_button = tkinter.Button(self.bottom_frame, \
            text='Calculate Farenheit \nTemperature', command=self.calc_faren_temp)
        self.quit_button = tkinter.Button(self.bottom_frame, \
            text='Quit', command=self.main_window.destroy)

        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')

        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()
    
        tkinter.mainloop()

    def calc_faren_temp(self):
        # Gets the user's input, converts it to a Farenheit temperature and passes the ans
        # as an arg to the StringVar obj's set method (faren_var)
        celsius = float(self.celsius_entry.get())
        faren = ((9/5) * celsius) + 32
        self.faren_var.set(format(faren, ',.1f'))

faren_celsius_gui = FarenheitToCelsius()

# 23 March 2021
# Starting Out With Python Exercise #5
# A county collects property taxes on the assessment value of property, which is
# 60 percent of the property's actual value. If an acre of land is valued at 
# $10,000, its assessment value is $6,000. The property tax is then $0.75 for each
# $100 of the assessment value. The tax for the acre assessed will be $45.00.
# Write a GUI program that displays the assessment value and property tax when a 
# user enters the actual value of the property. 

import tkinter

class PropertyTax:

    def __init__(self):
        self.main_window = tkinter.Tk()

        # The top frame gets the property value from the user. The mid1 frame displays
        # the property's assessment value. The mid2 frame displays the property's property
        # tax and the bottom frame has the calc and quit buttons.
        self.top_frame = tkinter.Frame(self.main_window)
        self.mid1_frame = tkinter.Frame(self.main_window)
        self.mid2_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.value_label = tkinter.Label(self.top_frame, \
            text='Enter the value of the property:')
        self.value_entry = tkinter.Entry(self.top_frame)

        self.value_label.pack(side='left')
        self.value_entry.pack(side='left')

        # Create 2 StringVar objs to be associated with the self.assess_output label
        # and the self.p_tax_output label.
        self.assess_var = tkinter.StringVar()
        self.p_tax_var = tkinter.StringVar()

        self.assess_label = tkinter.Label(self.mid1_frame, \
            text='Assessment Value of the Property:')
        self.assess_output = tkinter.Label(self.mid1_frame, \
            textvariable=self.assess_var)

        self.assess_label.pack(side='left')
        self.assess_output.pack(side='left')

        self.p_tax_label = tkinter.Label(self.mid2_frame, \
            text='Property Tax:')
        self.p_tax_output = tkinter.Label(self.mid2_frame, \
            textvariable=self.p_tax_var)

        self.p_tax_label.pack(side='left')
        self.p_tax_output.pack(side='left')

        self.calc_button = tkinter.Button(self.bottom_frame, \
            text='Calculate Assessment Value \nAnd Property Tax', \
                command=self.calc_assess_p_tax)
        self.quit_button = tkinter.Button(self.bottom_frame, \
            text='Quit', command=self.main_window.destroy)

        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')

        self.top_frame.pack()
        self.mid1_frame.pack()
        self.mid2_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    def calc_assess_p_tax(self):
        # Gets the property value from the user (via value entry widget). Calculates
        # the assessment value and passes the ans as an arg to the assess_var's set method.
        # Calculates the property tax and passes the ans as an arg to the p_tax_var's set
        # method
        value = float(self.value_entry.get())
        assess = .6 * value
        assess_str = '$' + str(format(assess, ',.2f'))
        p_tax = (assess / 100) * .75 
        p_tax_str = '$' + str(format(p_tax, ',.2f'))
        self.assess_var.set(assess_str)
        self.p_tax_var.set(p_tax_str)

my_property_gui = PropertyTax()

# 24 March 2021
# Starting Out With Python Exercise #6
# Joe's Automotive performs the following routine maintenance services:
#   Oil Change: $30.00
#   Lube Job: $20.00
#   Radiator Flush: $40.00
#   Transmission Flush: $100.00
#   Inspection: $35.00
#   Muffler Replacement: $200.00
#   Tire Rotation: $20.00
# Write a GUI program with check buttons that allow the user to selecty any
# or all of these services. When the user clicks a button the total charges
# should be displayed.

import tkinter

class MaintenanceServices:

    def __init__(self):
        self.main_window = tkinter.Tk()

        self.top_frame = tkinter.Frame(self.main_window)
        self.mid1_frame = tkinter.Frame(self.main_window)
        self.mid2_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.intro_label = tkinter.Label(text='Select the service(s) that you would ' + \
            'like performed on your car:')
        
        self.intro_label.pack()

        # Create 3 IntVar objs to use with the Checkbuttons and set the IntVar objs to 0.
        self.cb_oil_var = tkinter.IntVar()
        self.cb_oil_var.set(0)
        
        self.cb_lube_var = tkinter.IntVar()
        self.cb_lube_var.set(0)
        
        self.cb_radiator_var = tkinter.IntVar()
        self.cb_radiator_var.set(0)
        
        self.cb_transmission_var = tkinter.IntVar()
        self.cb_transmission_var.set(0)
        
        self.cb_inspection_var = tkinter.IntVar()
        self.cb_inspection_var.set(0)
        
        self.cb_muffler_var = tkinter.IntVar()
        self.cb_muffler_var.set(0)
        
        self.cb_tire_var = tkinter.IntVar()
        self.cb_tire_var.set(0)

        # Create the Checkbutton widgets in the mid1 frame.
        self.cb_oil = tkinter.Checkbutton(self.mid1_frame, text='Oil Change: $30.00', \
            variable=self.cb_oil_var)
        self.cb_lube = tkinter.Checkbutton(self.mid1_frame, text='Lube Job: $20.00', \
            variable=self.cb_lube_var)
        self.cb_radiator = tkinter.Checkbutton(self.mid1_frame, text='Radiator Flush: $40.00', \
            variable=self.cb_radiator_var)
        self.cb_transmission = tkinter.Checkbutton(self.mid1_frame, text='Transmission Flush: $100.00', \
            variable=self.cb_transmission_var)
        self.cb_inspection = tkinter.Checkbutton(self.mid1_frame, text='Inspection: $35.00', \
            variable=self.cb_inspection_var)
        self.cb_muffler = tkinter.Checkbutton(self.mid1_frame, text='Muffler Replacement: $200.00', \
            variable=self.cb_muffler_var)
        self.cb_tire = tkinter.Checkbutton(self.mid1_frame, text='Tire Rotation: $20.00', \
            variable=self.cb_tire_var)
        
        self.cb_oil.pack()
        self.cb_lube.pack()
        self.cb_radiator.pack()
        self.cb_transmission.pack()
        self.cb_inspection.pack()
        self.cb_muffler.pack()
        self.cb_tire.pack()
        
        self.total_label = tkinter.Label(self.mid2_frame, text='Maintenance Services Total:')
        # Create a StringVar obj to be associated with the total_show label
        self.total_var = tkinter.StringVar()
        self.total_show = tkinter.Label(self.mid2_frame, textvariable=self.total_var)

        self.total_label.pack(side='left')
        self.total_show.pack(side='left')
        
        self.calc_button = tkinter.Button(self.bottom_frame, text='Calculate Total', \
            command=self.calc_total)
        self.quit_button = tkinter.Button(self.bottom_frame, text='Quit', \
            command=self.main_window.destroy)

        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')

        self.top_frame.pack()
        self.mid1_frame.pack()
        self.mid2_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    def calc_total(self):
        # Calculates the total of maintenance services based on which Checkbuttons 
        # are selected. Passes the total as an arg to the StringVar obj's (total_var)
        # set method.
        total = 0.0
        
        if self.cb_oil_var.get() == 1:
            total += 30
        if self.cb_lube_var.get() == 1:
            total += 20
        if self.cb_radiator_var.get() == 1:
            total += 40
        if self.cb_transmission_var.get() == 1:
            total += 100
        if self.cb_inspection_var.get() == 1:
            total += 35
        if self.cb_muffler_var.get() == 1:
            total += 200
        if self.cb_tire_var.get() == 1:
            total += 20
        
        str_total = '$' + str(format(total, ',.2f'))
        self.total_var.set(str_total)

joe_maint_gui = MaintenanceServices()
