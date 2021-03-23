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