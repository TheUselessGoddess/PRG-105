import tkinter
import tkinter.messagebox


class Miles_Per_Gallon:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.top_frame = tkinter.Frame(self.main_window)
        self.middle_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.calc_button = tkinter.Button(self.bottom_frame, text = 'Convert', command = self.calculate)
        self.quit_button = tkinter.Button(self.bottom_frame, text = 'Quit', command = self.main_window.destroy)

        self.gallons = tkinter.Label(self.top_frame, text = 'Enter how many gallons your car holds:')
        self.miles = tkinter.Label(self.middle_frame, text = 'Enter how many miles you have driven:')
        self.output_label = tkinter.Label(self.bottom_frame, text = 'Converted to miles per gallons: ')

        self.gallon_entry = tkinter.Entry(self.top_frame, width = 10)
        self.miles_entry = tkinter.Entry(self.middle_frame, width = 10)
        #Frame Packing
        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()
        #Labels
        self.gallons.pack()
        self.miles.pack()
        self.output_label.pack()
        #Entries
        self.gallon_entry.pack()
        self.miles_entry.pack()
        #Buttons
        self.quit_button.pack(side = 'left')
        self.calc_button.pack(side = 'right')

        tkinter.mainloop()

    def calculate(self):
        gallons = float(self.gallon_entry.get())
        miles = float(self.miles_entry.get())
        self.output_label.config(text = 'Converted to miles per gallons: ' + str(format((miles / gallons), '.2f')))


converter = Miles_Per_Gallon()
